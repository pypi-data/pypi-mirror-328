# -*- coding: utf-8 -*-
import copy
import datetime
from typing import Union, Dict

import numpy as np
import pandas as pd
import deepquant.quest.datac as yhdatac
from deepquant.quest.environment import Environment
from deepquant.quest.interface import AbstractDataSource
from deepquant.quest.model.tick import TickObject
from deepquant.quest.model.instrument import Instrument
from deepquant.quest.utils.datetime_func import convert_dt_to_int, convert_ms_int_to_datetime, convert_int_to_datetime
from deepquant.quest.utils.functools import lru_cache
from deepquant.quest.data.base_data_source.data_source import BaseDataSource

from .resample_helper import resample_bars
from .yhdata_data_source import RQDataDataSource


class PTDataSource(AbstractDataSource):
    future_min_field_type_list = [('orig_time', '<u8'), ('low', '<f8'), ('open', '<f8'), ('high', '<f8'),
                                  ('volume', '<f8'), ('close', '<f8'), ("high_limited", '<f8'), ("low_limited", '<f8')]
    future_columns = [i[0] for i in future_min_field_type_list]

    def __init__(self, redis_store, future_info):
        self._rqdata_source = RQDataDataSource()
        self._redis_store = redis_store
        self._customized_future_info = future_info

        self.is_st_stock = self._rqdata_source.is_st_stock
        self.is_suspended = self._rqdata_source.is_suspended
        self.get_instruments = self._rqdata_source.get_instruments
        self.get_trading_calendars = self._rqdata_source.get_trading_calendars

    def get_dividend(self, instrument):
        return self._rqdata_source.get_dividend(instrument)

    def get_trading_minutes_for(self, instrument, trading_dt):
        raise NotImplementedError

    def get_yield_curve(self, start_date, end_date, tenor=None):
        return self._rqdata_source.get_yield_curve(start_date, end_date, tenor)

    def get_bar(self, instrument, dt, frequency='1d'):
        if frequency == '1d':
            raise RuntimeError('get current day bar in pt')

        if instrument.type == 'Future' and instrument.market_code.endswith('88'):
            dominant = self._dominant_future(instrument.underlying_symbol, dt)
            if dominant is None:
                return None
            bar = self._redis_store.get_current_bar(dominant)
        else:
            bar = self._redis_store.get_current_bar(instrument.market_code)

        if bar and convert_int_to_datetime(bar["datetime"]) >= dt:
            return bar

    OPEN_AUCTION_BAR_FIELDS = BaseDataSource.OPEN_AUCTION_BAR_FIELDS + ["last"]

    def get_open_auction_bar(self, instrument, dt):
        # type: (Instrument, Union[datetime.orig_time, datetime.date]) -> Dict
        # warning: 该方法会根据实时行情构造集合竞价 Bar，dt 参数不生效，故该函数仅能在【物理上的】集合竞价阶段被调用
        snapshot = self.current_snapshot(instrument, Environment.get_instance().config.base.frequency, dt)
        return {k: getattr(snapshot, k) for k in self.OPEN_AUCTION_BAR_FIELDS}

    def get_settle_price(self, instrument, date):
        if instrument.type == 'Future' and instrument.market_code.endswith('88'):
            dominant = self._dominant_future(instrument.underlying_symbol, date)
            if dominant is None:
                return np.nan
            return self._redis_store.get_settle_price(dominant)

        return self._redis_store.get_settle_price(instrument.market_code)

    def _filter_out(self, instrument, dt, bars):
        if instrument.type != 'Future':
            # 期货不需要过滤
            day_start = convert_dt_to_int(dt.replace(hour=0, minute=0, second=0))
            return [b for b in bars if b['orig_time'] >= day_start]
        else:
            trading_day = self._rqdata_source.get_future_trading_date(dt)
            trading_day_i = trading_day.year * 10000 + trading_day.month * 100 + trading_day.day
            return [b for b in bars if b['trading_date'] == trading_day_i]

    def _filter_out_ticks(self, instrument, dt, bars):
        if instrument.type != 'Future':
            # 期货不需要过滤
            day_start = convert_dt_to_int(dt.replace(hour=0, minute=0, second=0))
            return [b for b in bars if b['date'] >= day_start]
        else:
            trading_day = self._rqdata_source.get_future_trading_date(dt)
            trading_day_i = trading_day.year * 10000 + trading_day.month * 100 + trading_day.day
            return [b for b in bars if b['trading_date'] == trading_day_i]

    @staticmethod
    def _get_item(obj, key, default):
        if key == 'close':
            # Snapshot 对象没有 close
            key = 'last'

        try:
            if key == 'orig_time':
                res = str(obj[key])
                return int(res[:14])
            return obj[key]
        except KeyError:
            return default

    def _append_snapshot(self, bars, fields, snapshot):
        if not snapshot:
            return bars
        result = np.empty_like(bars)
        result[:-1] = bars[1:]
        if isinstance(fields, str):
            result[-1] = self._get_item(snapshot._tick_dict, fields, np.nan)
            return result

        for f in bars.dtype.names:
            result[-1][f] = self._get_item(snapshot._tick_dict, f, np.nan)
        return result

    def _redis_history(self, instrument, bars_needed, dt):
        if instrument.type == 'Future' and instrument.market_code.endswith('88'):
            dominant = self._dominant_future(instrument.underlying_symbol, dt)
            if dominant is None:
                return []
            return self._redis_store.history(dominant, bars_needed)

        return self._redis_store.history(instrument.market_code, bars_needed)

    def _redis_ticks_history(self, instrument, ticks_needed, dt):
        if instrument.type == 'Future' and instrument.market_code.endswith('88'):
            dominant = self._dominant_future(instrument.underlying_symbol, dt)
            if dominant is None:
                return []
            return self._redis_store.history_ticks(dominant, ticks_needed)

        return self._redis_store.history_ticks(instrument.market_code, ticks_needed)

    @staticmethod
    def _convert_tick_datetime(date, time):
        year, r = divmod(date, 10000)
        month, day = divmod(r, 100)
        hour, r = divmod(time, 10000000)
        minute, r = divmod(r, 100000)
        second, millisecond = divmod(r, 1000)
        return datetime.datetime(year, month, day, hour, minute, second, millisecond * 1000)

    def history_ticks(self, instrument, count, dt):
        tick_dict_list = self._filter_out(instrument, dt, self._redis_ticks_history(instrument, count, dt))

        tick_list = []
        for tick_dict in tick_dict_list:

            try:
                calendar_dt = self._convert_tick_datetime(tick_dict['date'], tick_dict["time"])
            except KeyError:
                calendar_dt = convert_ms_int_to_datetime(tick_dict["datetime"])

            tick_dict["datetime"] = calendar_dt
            # FIXME: 和小杰的名字不一样
            tick_dict["asks"] = tick_dict.get("ask", [])
            tick_dict["bids"] = tick_dict.get("bid", [])
            tick_dict["ask_vols"] = tick_dict.get("ask_vol", [])
            tick_dict["bid_vols"] = tick_dict.get("bid_vol", [])
            tick = TickObject(instrument, tick_dict)
            tick_list.append(tick)

        return tick_list

    def history_bars(self, instrument, bar_count, frequency, fields, dt,
                     skip_suspended=True, include_now=False, adjust_type='pre', adjust_orig=None):
        if frequency == '1d':
            trading_day = Environment.get_instance().trading_dt
            bars = self._rqdata_source.history_bars(instrument, bar_count, frequency, fields,
                                                    self._rqdata_source.get_previous_trading_date(trading_day),
                                                    skip_suspended=skip_suspended, include_now=include_now,
                                                    adjust_type=adjust_type, adjust_orig=adjust_orig)
            if not include_now:
                return bars
            return self._append_snapshot(bars, fields, self.current_snapshot(instrument, '1m', dt))

        if frequency == "1m" and ("high_limited" in fields or "low_limited" in fields):
            _fields = set(fields) - {"high_limited", "low_limited"}
            bars = self._history_bars(instrument, bar_count, frequency, list(_fields), dt, skip_suspended, include_now,
                                      adjust_type, adjust_orig)
            bars = self.add_limit_fields(instrument, dt, adjust_type, bars)
        else:
            bars = self._history_bars(instrument, bar_count, frequency, fields, dt, skip_suspended, include_now,
                                      adjust_type, adjust_orig)
        return bars

    def _history_bars(self, instrument, bar_count, frequency, fields, dt, skip_suspended, include_now, adjust_type,
                      adjust_orig):
        # 如果当天停牌，则认为 rqdata 中包含了所需要的数据
        if skip_suspended and self._rqdata_source.is_suspended(instrument.market_code, [dt.date()])[0]:
            return self._rqdata_source.history_bars(instrument, bar_count, frequency, fields, dt,
                                                    skip_suspended=skip_suspended, include_now=include_now,
                                                    adjust_type=adjust_type, adjust_orig=adjust_orig)
        resample = int(frequency[:-1])
        # 需要一直取到当天开始，考虑期货夜盘，取比较多的为好
        bars_needed = bar_count if resample == 1 else 1000
        bars = self._filter_out(instrument, dt, self._redis_history(instrument, bars_needed, dt))
        # 有可能包含了停牌数据
        dates = set(v['orig_time'] // 1000000 for v in bars)
        for d in dates:
            if self._rqdata_source.is_suspended(instrument.market_code, [d])[0]:
                bars = [v for v in bars if v['orig_time'] // 1000000 != d]
        if not bars:
            return self._rqdata_source.history_bars(instrument, bar_count, frequency, fields, dt,
                                                    skip_suspended=skip_suspended, include_now=include_now,
                                                    adjust_type=adjust_type, adjust_orig=adjust_orig)
        xfields = copy.deepcopy(fields)
        if isinstance(xfields, str):
            xfields = [xfields]
        if 'orig_time' not in xfields:
            xfields.append('orig_time')
        start_dt = self._rqdata_source.get_previous_trading_date(str(bars[0]['trading_date']))

        def _field_type(field_name):
            return np.uint64 if field_name == 'orig_time' else np.float64

        dtype = np.dtype([(f, _field_type(f)) for f in xfields])
        bars = np.array([tuple([v[f] for f in xfields]) for v in bars], dtype=dtype)
        if resample != 1:
            bars = resample_bars(instrument, bars, xfields, resample, include_last=include_now)
        bars = bars if fields is None else bars[fields]
        if len(bars) >= bar_count:
            return bars[-bar_count:]
        needed = self._rqdata_source.history_bars(instrument, bar_count - len(bars), frequency,
                                                  fields, start_dt, skip_suspended=skip_suspended,
                                                  include_now=include_now, adjust_type=adjust_type,
                                                  adjust_orig=adjust_orig)
        if needed is None:
            return bars
        return np.hstack((needed, bars))

    @lru_cache(512)
    def _dominant_future(self, underlying_symbol, date):
        r = yhdatac.get_dominant_future(underlying_symbol, date, date)
        if isinstance(r, pd.Series) and r.size == 1:
            return r.item()

        return None

    def current_snapshot(self, instrument, frequency, dt):
        if instrument.type == 'Future' and instrument.market_code.endswith('88'):
            dominant = self._dominant_future(instrument.underlying_symbol, dt)
            if dominant is None:
                return None
            data_dict = self._redis_store.get_snapshot(dominant)
        else:
            data_dict = self._redis_store.get_snapshot(instrument.market_code)
        if data_dict is None:
            return None
        return TickObject(instrument, data_dict)

    def get_split(self, instrument):
        return self._rqdata_source.get_split(instrument)

    def available_data_range(self, frequency):
        return datetime.date(2005, 1, 4), datetime.date.max

    def get_commission_info(self, instrument):
        underlying_symbol = instrument.underlying_symbol
        try:
            return self._customized_future_info[underlying_symbol]
        except KeyError:
            return self._rqdata_source.get_commission_info(instrument)

    def get_share_transformation(self, market_code):
        return self._rqdata_source.get_share_transformation(market_code)

    def add_limit_fields(self, instrument, day, adjust_type, bars):
        """deepquant.quest.datac分钟线不支持 high_limited low_limited 字段 需要手动添加"""
        env = Environment.get_instance()
        env_trading_dt = pd.Timestamp(env.trading_dt).date()
        f_get_trading_dt = env.get_instance().data_proxy.get_previous_trading_date

        datetime = bars['orig_time'] // 1000000
        dt = set(datetime)
        # dt_table = { 20190716: datetime.date(2019, 7, 16) }
        dt_table = {d: f_get_trading_dt(str(int(d * 1000000)), n=0).date() for d in dt}

        res = self._rqdata_source._get_day_bars(instrument, len(dt), day, adjust_type)
        # dict like {datetime.date(2019, 6, 26): 9631.0}
        high_limited = dict(zip(res.index.date, res["high_limited"].tolist()))
        low_limited = dict(zip(res.index.date, res["low_limited"].tolist()))

        # add today data
        if env_trading_dt in dt_table.values():
            current_snapshot = self.current_snapshot(instrument, "1m", day)
            high_limited[env_trading_dt] = current_snapshot["high_limited"]
            low_limited[env_trading_dt] = current_snapshot["low_limited"]

        # bar数据无序
        bars_1 = bars[['orig_time', 'low_price', 'open_price', 'high_price', 'volume', 'close_price']]
        data = [tuple(bars_1[i]) + (high_limited[dt_table[datetime[i]]], low_limited[dt_table[datetime[i]]])
                for i in range(len(bars))]

        res_bars = np.array(data, dtype=self.future_min_field_type_list)
        return res_bars
