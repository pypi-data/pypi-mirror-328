# -*- coding: utf-8 -*-
import datetime
from itertools import groupby
from typing import Dict, Optional, Iterable

import numpy as np
import pandas as pd
import deepquant.quest.datac as yhdatac
from lru import LRU as lru_dict
from deepquant.quest.data.trading_dates_mixin import TradingDatesMixin
from deepquant.quest.const import COMMISSION_TYPE
from deepquant.quest.environment import Environment
from deepquant.quest.core.events import EVENT
from deepquant.quest.interface import AbstractDataSource
from deepquant.quest.model.instrument import Instrument
from deepquant.quest.utils.datetime_func import convert_dt_to_int
from deepquant.quest.utils.logger import system_log
from deepquant.quest.utils.functools import lru_cache
from deepquant.quest.const import TRADING_CALENDAR_TYPE, INSTRUMENT_TYPE
from deepquant.quest.data.base_data_source.data_source import BaseDataSource
from deepquant.quest.data.base_data_source.storages import InstrumentStore
from six import string_types

from .resample_helper import resample_bars


@lru_cache(128)
def _is_suspended(market_code):
    return yhdatac.is_suspended(market_code)[market_code]


@lru_cache(256)
def _get_tick_size(market_code):
    return yhdatac.instruments(market_code).tick_size()


def _is_valid_order_book_ie(market_code):
    return isinstance(market_code, string_types) and bool(market_code)


class RQDataDataSource(TradingDatesMixin, AbstractDataSource):
    def __init__(self):

        instruments = [
            Instrument(i.__dict__, lambda i: _get_tick_size(i.market_code))
            for i in yhdatac.instruments(list(yhdatac.all_instruments().market_code)) if _is_valid_order_book_ie(
                i.market_code
            )
        ]
        self._ins_id_or_sym_type_map = {}
        self._instruments_stores = {}
        for ins_type in BaseDataSource.DEFAULT_INS_TYPES:
            instruments_store = InstrumentStore(instruments, ins_type)
            for id_or_sym in instruments_store.all_id_and_syms:
                self._ins_id_or_sym_type_map[id_or_sym] = ins_type
            self._instruments_stores[ins_type] = instruments_store

        self._trading_dates = pd.DatetimeIndex(pd.Timestamp(d) for d in deepquant.quest.datac.get_trading_dates('2005-01-04', '2050-01-01'))
        TradingDatesMixin.__init__(self, {TRADING_CALENDAR_TYPE.EXCHANGE: self._trading_dates})

        self._history_cache = {}
        self._minute_bar_cache = lru_dict(512)
        Environment.get_instance().event_bus.add_listener(EVENT.PRE_BEFORE_TRADING,
                                                          lambda e: self._history_cache.clear())

    def get_trading_calendars(self):
        # type: () -> Dict[TRADING_CALENDAR_TYPE, pd.DatetimeIndex]
        return self.trading_calendars

    def get_instruments(self, id_or_syms=None, types=None):
        # type: (Optional[Iterable[str]], Optional[Iterable[INSTRUMENT_TYPE]]) -> Iterable[Instrument]
        if id_or_syms is not None:
            ins_type_getter = lambda i: self._ins_id_or_sym_type_map.get(i)
            type_id_iter = groupby(sorted(id_or_syms, key=ins_type_getter), key=ins_type_getter)
        else:
            type_id_iter = ((t, None) for t in types or self._instruments_stores.keys())
        for ins_type, id_or_syms in type_id_iter:
            if ins_type is not None and ins_type in self._instruments_stores:
                yield from self._instruments_stores[ins_type].get_instruments(id_or_syms)

    def is_st_stock(self, market_code, dates):
        if len(dates) == 1:
            return [yhdatac._is_st_stock(market_code, dates[0])]

        df = yhdatac.is_st_stock(market_code, dates[0], dates[-1])
        if df is None or df.empty:
            return [False] * len(dates)
        return df.values

    def is_suspended(self, market_code, dates):
        env = Environment.get_instance()
        if env.get_instrument(market_code).type != "CS":
            return [False] * len(dates)
        try:
            df = yhdatac.is_suspended(market_code, str(dates[0]), str(dates[-1]))
        # non-cs market_code may cause ValueError
        except ValueError:
            df = None
        if df is None or df.empty:
            return [False] * len(dates)

        return df[market_code].values

    def _get_minute_bars_of_day(self, market_code, day, adjust_type):
        try:
            return self._minute_bar_cache[market_code, day, adjust_type]
        except KeyError:
            v = yhdatac.get_price(market_code, day, day, frequency='1m', adjust_type=adjust_type)
            if v is not None and not v.empty:
                v = v.droplevel(0)
                v = self._ndarray_from_df(v, None)
                self._minute_bar_cache[market_code, day, adjust_type] = v
                return v
            else:
                self._minute_bar_cache[market_code, day, adjust_type] = None
                return None

    def _prepare_for(self, instrument, dates, adjust_type):
        market_code = instrument.market_code
        missing = []
        for d in dates:
            if (market_code, d, adjust_type) not in self._minute_bar_cache:
                missing.append(d)
        if len(missing) < 3 or len(missing) / len(dates) < 0.2:
            return

        trading_dates = self.get_trading_dates(missing[0], missing[-1])
        if len(trading_dates) / len(missing) > 2:
            # 太多空洞了
            return
        df = yhdatac.get_price(market_code, missing[0], missing[-1], frequency='1m', adjust_type=adjust_type)
        df = df.droplevel(0)
        # 如果品种是 future, 则使用交易日作为划分条件, 而不是自然日, 对应 case 6440
        if instrument.type == 'Future':
            for (year, month, day), frame in df.groupby((df.trading_date.dt.year.values, df.trading_date.dt.month.values, df.trading_date.dt.day.values)):
                ts = pd.Timestamp(year=year, month=month, day=day)
                if ts in missing:
                    # copy frame, so the big one can be freed
                    self._minute_bar_cache[market_code, ts, adjust_type] = self._ndarray_from_df(frame, None)
        else:
            for (year, month, day), frame in df.groupby([df.index.year, df.index.month, df.index.day]):
                ts = pd.Timestamp(year=year, month=month, day=day)
                if ts in missing:
                    self._minute_bar_cache[market_code, ts, adjust_type] = self._ndarray_from_df(frame, None)

    def get_dividend(self, instrument):
        df = yhdatac.get_dividend(instrument.market_code, adjusted=False)
        if df is None or df.empty:
            return None
        df = df[df.index <= datetime.datetime.now()]
        table = np.empty((len(df),), dtype=np.dtype([
            ('announcement_date', '<u4'), ('book_closure_date', '<u4'),
            ('ex_dividend_date', '<u4'), ('payable_date', '<u4'),
            ('dividend_cash_before_tax', np.float64), ('round_lot', '<u4')
        ]))
        table['announcement_date'] = [d.year * 10000 + d.month * 100 + d.day for d in df.index]
        table['book_closure_date'] = [d.year * 10000 + d.month * 100 + d.day for d in df['book_closure_date']]
        table['ex_dividend_date'] = [d.year * 10000 + d.month * 100 + d.day for d in df['ex_dividend_date']]
        table['payable_date'] = [d.year * 10000 + d.month * 100 + d.day for d in df['payable_date']]
        table['dividend_cash_before_tax'] = df['dividend_cash_before_tax'].values
        table['round_lot'] = df['round_lot'].values
        return table

    def get_yield_curve(self, start_date, end_date, tenor=None):
        return yhdatac.get_yield_curve(start_date, end_date, tenor)

    def _n_trading_days_before(self, dt, count):
        pos = self._trading_dates.searchsorted(pd.Timestamp(dt), side='right')
        pos -= count
        if pos < 0:
            pos = 0
        return self._trading_dates[pos]

    def __get_day_bars(self, market_code, bar_count, dt, adjust_type):
        start_dt = self._n_trading_days_before(dt, bar_count + 1)
        df = yhdatac.get_price(market_code, start_dt, dt, frequency='1d', adjust_type=adjust_type)
        df = df.droplevel(0)
        return df

    def _get_day_bars(self, instrument, bar_count, dt, adjust_type):
        try:
            r = self._history_cache[instrument.market_code, adjust_type]
            if len(r) >= bar_count or len(r) == 0:
                return r
            end_dt = self.get_previous_trading_date(r.index[0])

            if end_dt <= instrument.listed_date:
                return r

            h = self.__get_day_bars(instrument.market_code, bar_count - len(r), end_dt, adjust_type)
            r = h.append(r)
            self._history_cache[instrument.market_code, adjust_type] = r
            return r
        except KeyError:
            h = self.__get_day_bars(instrument.market_code, bar_count, dt, adjust_type)
            self._history_cache[instrument.market_code, adjust_type] = h
            return h

    @staticmethod
    def _ndarray_from_df(df, fields):
        df_dtype = df.dtypes
        if fields is None:
            fields = ['datetime'] + [f for f in df.columns]
        dtype = np.dtype(([('datetime', np.uint64)] if 'datetime' in fields else []) +
                         [(f, df_dtype[f]) for f in fields if f != 'datetime'])
        result = np.empty(shape=(len(df),), dtype=dtype)
        for f in fields:
            if f == 'datetime':
                result['datetime'] = [convert_dt_to_int(dt) for dt in df.index]
            else:
                result[f] = df[f].values

        return result

    def _history_day_bars(self, instrument, bar_count, fields, dt, skip_suspended, adjust_type):
        if skip_suspended and instrument.type == 'stock':
            suspended = _is_suspended(instrument.market_code)
            active_days = suspended[(suspended == False) & (suspended.index <= dt)].index
            # 多取一个以确保拿到足够多的 bar
            days = active_days[-bar_count - 1:]
            if len(days) == 0:
                # possible for newly listed stock
                return None
            n_trading_dates = len(suspended) - suspended.index.searchsorted(days[0])
            result = self._get_day_bars(instrument, n_trading_dates, dt, adjust_type)
            if result is None:
                return None
            df = result.loc[days]
        else:
            df = self._get_day_bars(instrument, bar_count, dt, adjust_type)

        fields_ = fields
        if isinstance(fields_, str):
            fields_ = [fields_]
        if df is not None and not df.empty:
            r = self._ndarray_from_df(df, fields_)[-bar_count:]
            return r if fields is None else r[fields]
        else:
            return None

    def history_bars(self, instrument, bar_count, frequency, fields, dt,
                     skip_suspended=True, include_now=False, adjust_type='pre', adjust_orig=None):
        if frequency == '1d':
            return self._history_day_bars(instrument, bar_count, fields, dt, skip_suspended, adjust_type)
        if frequency == '1w':
            raise NotImplementedError
        resample = int(frequency[:-1])

        fields_ = fields
        if isinstance(fields_, str):
            fields_ = [fields_]

        if not skip_suspended or instrument.type != 'stock':
            start_date = max(instrument.listed_date, dt - datetime.timedelta(365))
            days = self.get_trading_dates(start_date, dt)
        else:
            suspended = _is_suspended(instrument.market_code)
            days = suspended[suspended == False][:dt].index

        n_days = bar_count * resample // 240 + 1
        self._prepare_for(instrument, days[-n_days:], adjust_type)

        need = bar_count
        results = []
        for i in range(len(days) - 1, 0, -1):
            bars = self._get_minute_bars_of_day(instrument.market_code, days[i], adjust_type)
            if bars is None:
                continue
            if resample != 1:
                bars = resample_bars(instrument, bars, fields_, resample)
            results.append(bars[fields] if fields is not None else bars)
            need -= len(bars)
            if need <= 0:
                break

        if not results:
            return None

        return np.hstack(results[::-1])[-bar_count:]

    def get_trading_minutes_for(self, instrument, trading_dt):
        raise NotImplementedError

    def get_bar(self, instrument, dt, frequency):
        raise NotImplementedError

    def get_last_price(self, instrument, dt):
        raise NotImplementedError

    def get_commission_info(self, instrument):
        return self._get_future_info(instrument, 'speculation')

    @lru_cache(128)
    def _get_future_info(self, instrument, hedge_type):
        result = yhdatac.future_commission_margin(instrument.market_code, hedge_flag=hedge_type)
        if result is None or result.empty:
            return None

        result = result.iloc[0]

        return {
            'close_commission_ratio': result['close_commission_ratio'],
            'close_commission_today_ratio': result['close_commission_today_ratio'],
            'open_commission_ratio': result['open_commission_ratio'],
            'commission_type': COMMISSION_TYPE.BY_MONEY if result['commission_type'] == 'by_money' else COMMISSION_TYPE.BY_VOLUME,
            'short_margin_ratio': result['short_margin_ratio'],
            'long_margin_ratio': result['long_margin_ratio'],
        }

    def current_snapshot(self, instrument, frequency, dt):
        raise NotImplementedError

    def get_settle_price(self, instrument, date):
        raise NotImplementedError

    def get_split(self, instrument):
        df = yhdatac.get_split(instrument.market_code)
        if df is None or df.empty:
            return None

        result = np.empty((len(df), ), dtype=np.dtype([('ex_date', np.int), ('split_factor', np.float64)]))
        result['ex_date'] = [(d.year*10000 + d.month*100 + d.day) * 1000000 for d in df.index]
        result['split_factor'] = df['split_coefficient_to'].values / df['split_coefficient_from'].values

        return result

    def available_data_range(self, frequency):
        prev_dt = self.get_previous_trading_date(datetime.date.today()) - datetime.timedelta(days=7)
        while True:
            result = yhdatac.get_price('000001.SH', prev_dt, datetime.date.today(), fields='ClosingPx',
                                       frequency=frequency, adjust_type='internal')
            if result is not None:
                return datetime.date(2005, 1, 4), result.index[-1].date()
            prev_dt -= datetime.timedelta(days=30)

    def get_share_transformation(self, market_code):
        """
        获取获取转股信息
        deepquant.quest.datac不支持此API时返回 None
        """
        try:
            df = yhdatac.get_share_transformation(market_code)
        except AttributeError:
            system_log.debug("deepquant.quest.datac no api get_share_transformation for get {}".format(market_code))
            return None
        if df is None or df.empty:
            return None
        return df.loc[0, "successor"], df.loc[0, "share_conversion_ratio"]
