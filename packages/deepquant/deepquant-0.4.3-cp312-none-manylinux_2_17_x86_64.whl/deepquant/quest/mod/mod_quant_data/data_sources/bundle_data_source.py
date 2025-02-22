# -*- coding: utf-8 -*-
import datetime
import os
from bisect import bisect_right
from typing import Container, Dict, Iterable, Optional

import numpy as np
import numpy.lib.recfunctions as nprf
from deepquant.quest.const import INSTRUMENT_TYPE, DEFAULT_ACCOUNT_TYPE
from deepquant.quest.core.events import EVENT
from deepquant.quest.data.base_data_source import BaseDataSource
from deepquant.quest.data.base_data_source.adjust import FIELDS_REQUIRE_ADJUSTMENT, PRICE_FIELDS
from deepquant.quest.data.trading_dates_mixin import TradingDatesMixin
from deepquant.quest.data.base_data_source.storages import FuturesTradingParameters
from deepquant.quest.environment import Environment
from deepquant.quest.interface import AbstractDataSource
from deepquant.quest.model.bar import NANDict
from deepquant.quest.model.tick import TickObject
from deepquant.quest.model.instrument import Instrument
from deepquant.quest.utils.datetime_func import convert_date_time_ms_int_to_datetime
from deepquant.quest.utils.exception import RQInvalidArgument
from deepquant.quest.utils.functools import lru_cache

from .data_store import AbstractMinBarStore, H5MinBarStore, H5TicksLoader, RqdataTicksLoader, AlgoStore, OpenAuctionVolumeStore, FuturesTradingParametersStore
from .lazy_tick import LazyTick
from .resample_helper import resample_bars


def convert_dt_to_int(dt):
    # 1e10 for float 1**10 fot int
    return dt.year * 10 ** 10 + dt.month * 10 ** 8 + dt.day * 10 ** 6 + dt.hour * 10 ** 4 + dt.minute * 10 ** 2 + dt.second


def convert_date_to_int(date):
    return date.year * 1e10 + date.month * 1e8 + date.day * 1e6


def to_date_int(date):
    return date.year * 10000 + date.month * 100 + date.day


def int_to_date(dt):
    year, dt = divmod(dt, 10000)
    month, day = divmod(dt, 100)
    return datetime.date(year, month, day)


def intersection(s1, e1, s2, e2):
    return max(s1, s2), min(e1, e2)


class BundleDataSource(AbstractDataSource, TradingDatesMixin):
    def __init__(
            self, 
            bundle_path, 
            h5_minbar_path=None, 
            h5_tick_path=None, 
            tick_type=None, 
            custom_future_info=None, 
        ):
        h5_minbar_path = h5_minbar_path or os.path.join(bundle_path, "h5")
        h5_tick_path = h5_tick_path or os.path.join(bundle_path, "ticks")

        root_path = os.path.realpath(bundle_path)

        self._base_data_source = BaseDataSource(root_path, custom_future_info)
        TradingDatesMixin.__init__(self, self._base_data_source.get_trading_calendars())

        self._min_bars = {}  # type: Dict[INSTRUMENT_TYPE, AbstractMinBarStore]
        min_bar_store = H5MinBarStore(h5_minbar_path)
        for instrument_type in (
                INSTRUMENT_TYPE.ETF, INSTRUMENT_TYPE.LOF, INSTRUMENT_TYPE.CS, INSTRUMENT_TYPE.INDX,
                INSTRUMENT_TYPE.FUTURE, INSTRUMENT_TYPE.OPTION, INSTRUMENT_TYPE.CONVERTIBLE,
        ):
            self.register_minbar_store(instrument_type, min_bar_store)
        self.get_dividend = self._base_data_source.get_dividend

        if tick_type == "h5":
            self.tick_loader = H5TicksLoader(h5_tick_path)
        elif tick_type == "yhdata":
            self.tick_loader = RqdataTicksLoader()
        else:
            raise NotImplementedError("tick_type={}".format(tick_type))

        self._tick_board = {}

        self._auto_update_bundle = False
        self._futures_trading_parameters = None
        env = Environment.get_instance()
        if env.config.base.auto_update_bundle:
            self._auto_update_bundle = True
            self.auto_update_bundle_path = env.config.base.auto_update_bundle_path
            if not self.auto_update_bundle_path:
                self.auto_update_bundle_path = bundle_path
            self._open_auction_volumes = OpenAuctionVolumeStore(self.auto_update_bundle_path, env.config.base.end_date)
            
            if env.config.base.futures_time_series_trading_parameters and DEFAULT_ACCOUNT_TYPE.FUTURE in env.config.base.accounts:
                self._futures_trading_parameters = FuturesTradingParametersStore(self.auto_update_bundle_path, env.config.base.end_date, custom_future_info)

        self.get_open_auction_bar = self._base_data_source.get_open_auction_bar

        self._algo_store = AlgoStore(os.path.join(bundle_path, "algo"), h5_minbar_path)

        Environment.get_instance().event_bus.prepend_listener(EVENT.TICK, self._on_tick)

    def get_instruments(self, id_or_syms=None, types=None):
        # type: (Optional[Iterable[str]], Optional[Iterable[INSTRUMENT_TYPE]]) -> Iterable[Instrument]
        return self._base_data_source.get_instruments(id_or_syms, types)

    def get_trading_minutes_for(self, instrument, trading_dt):
        bars = self._minute_bars_of_day(instrument, to_date_int(trading_dt))
        if bars is not None:
            return bars['datetime']
        return None

    def get_trading_calendars(self):
        return self._base_data_source.get_trading_calendars()

    def register_day_bar_store(self, instrument_type, store):
        return self._base_data_source.register_day_bar_store(instrument_type, store)

    def append_suspend_date_set(self, date_set):
        return self._base_data_source.append_suspend_date_set(date_set)

    def register_minbar_store(self, instrument_type, store):
        # type: (INSTRUMENT_TYPE, AbstractMinBarStore) -> None
        self._min_bars[instrument_type] = store

    def register_instruments_store(self, instruments_store):
        return self._base_data_source.register_instruments_store(instruments_store)

    def register_calendar_store(self, calendar_type, calendar_store):
        return self._base_data_source.register_calendar_store(calendar_type, calendar_store)

    def register_dividend_store(self, instrument_type, store):
        return self._base_data_source.register_dividend_store(instrument_type, store)

    def register_split_store(self, instrument_type, store):
        return self._base_data_source.register_split_store(instrument_type, store)

    def _get_minbar_store(self, instrument):
        try:
            return self._min_bars[instrument.type]
        except KeyError:
            raise NotImplementedError("no minute bar for instrument type: {}".format(instrument.type))

    @lru_cache(5000)
    def _minute_bars_of_day(self, instrument, date):
        minbar = self._get_minbar_store(instrument).get_minute_bar(instrument.market_code, date, fields=None)
        daybar = self._base_data_source.get_bar(instrument, int_to_date(date), "1d")
        if daybar is None or minbar is None:
            return
        for field in ("high_limited", "low_limited"):
            if field not in minbar.dtype.names:
                continue
            try:
                minbar[field] = daybar[field]
            except (KeyError, ValueError):
                minbar[field] = 0
        return minbar

    def get_bar(self, instrument, dt, frequency):
        if frequency == '1d':
            return self._base_data_source.get_bar(instrument, dt, frequency)

        trade_date = self.get_future_trading_date(dt)
        bars = self._minute_bars_of_day(instrument, to_date_int(trade_date))
        if bars is None:
            return None

        dt = convert_dt_to_int(dt)
        pos = bars['datetime'].searchsorted(dt)

        if pos >= len(bars):
            # 若dt超过收盘时间,返回收盘的bar
            return bars[-1]
        if bars['datetime'][pos] != dt:
            return None
        return bars[pos]

    def get_settle_price(self, instrument, date):
        return self._base_data_source.get_settle_price(instrument, date)

    def get_commission_info(self, instrument):
        return self._base_data_source.get_commission_info(instrument)
    
    def get_futures_trading_parameters(self, instrument: Instrument, dt: datetime.datetime) -> Optional[FuturesTradingParameters]:
        if self._futures_trading_parameters and self._futures_trading_parameters.init:
            data = self._futures_trading_parameters.get_futures_trading_parameters(instrument, dt)
            if data is None:
                data = self._base_data_source.get_futures_trading_parameters(instrument, dt)
            return data
        return self._base_data_source.get_futures_trading_parameters(instrument, dt)

    def current_snapshot(self, instrument, frequency, dt):
        if frequency == '1d':
            # implemented in wrapper
            raise NotImplementedError

        if frequency == 'tick':
            # 每个tick事件都会缓存 如果查询非订阅tick 则从历史数据中查询
            tick_obj = self._tick_board.get(instrument.market_code, None)
            if tick_obj is None:
                env = Environment.get_instance()
                raw_tick = self.history_ticks(instrument, 1, dt)
                raw_tick = raw_tick[0] if raw_tick else NANDict
                tick_obj = LazyTick(instrument, raw_tick, env.trading_dt)
            return tick_obj

        # min bar
        if instrument.type == 'Future':
            trade_date = self.get_future_trading_date(dt)
        else:
            trade_date = dt.date()

        snapshot = self._snapshot_of_day(instrument, trade_date)
        if snapshot is None:
            return None
        dt1 = convert_dt_to_int(dt)
        pos = snapshot['datetime'].searchsorted(dt1)
        if pos >= len(snapshot) or snapshot['datetime'][pos] != dt1:
            return None
        return TickObject(instrument, snapshot[pos])

    @lru_cache(5000)
    def _snapshot_of_day(self, instrument, date):
        minute_bars = self._minute_bars_of_day(instrument, to_date_int(date))
        if minute_bars is None:
            return None

        day_bar = self._base_data_source.get_bar(instrument, date, '1d')
        if day_bar is None:
            return None
        day_open = day_bar['open']
        try:
            day_high_limited = day_bar['high_limited']
        except (KeyError, ValueError):
            # indexes has no high_limited/low_limited field
            day_high_limited = 0
        try:
            day_low_limited = day_bar['low_limited']
        except (KeyError, ValueError):
            day_low_limited = 0
        prev_bar = self._base_data_source.get_bar(instrument, self.get_previous_trading_date(date), '1d')
        prev_close = prev_bar['close'] if prev_bar else np.nan

        dtype = self._tick_dtype_for(instrument)
        snapshot = np.empty(shape=(minute_bars.size,), dtype=dtype)
        snapshot['datetime'] = minute_bars['datetime']
        snapshot['volume'] = np.cumsum(minute_bars['volume'])
        snapshot['total_turnover'] = np.cumsum(minute_bars['total_turnover'])
        snapshot['prev_close'] = prev_close
        snapshot['last'] = minute_bars['close']
        snapshot['high_limited'] = day_high_limited
        snapshot['low_limited'] = day_low_limited

        i = 0
        while i < len(minute_bars) and minute_bars['volume'][i] == 0:
            i += 1

        if i > 0:
            snapshot['open'][:i] = 0
            snapshot['high'][:i] = 0
            snapshot['low'][:i] = 0

        snapshot['open'][i:] = day_open
        snapshot['low'][i:] = np.minimum.accumulate(minute_bars['low'][i:])
        snapshot['high'][i:] = np.maximum.accumulate(minute_bars['high'][i:])

        if instrument.type == 'Future':
            try:
                snapshot['open_interest'] = minute_bars['open_interest']
            except ValueError:
                # 一些旧合约分钟线中没有 open_interest 字段
                pass
            snapshot['prev_settlement'] = day_bar['prev_settlement']

        return snapshot

    def is_suspended(self, market_code, dates):
        return self._base_data_source.is_suspended(market_code, dates)

    def is_st_stock(self, market_code, dates):
        return self._base_data_source.is_st_stock(market_code, dates)

    @staticmethod
    def _are_fields_valid(fields, valid_fields):
        # type: (Optional[Iterable], Container) -> bool
        if fields is None:
            return True
        if isinstance(fields, str):
            return fields in valid_fields
        for field in fields:
            if field not in valid_fields:
                return False
        return True

    _STOCK_FIELDS = [
        ('datetime', np.uint64),
        ('open', np.float64),
        ('high', np.float64),
        ('low', np.float64),
        ('last', np.float64),
        ('volume', np.float64),
        ('total_turnover', np.float64),
        ('prev_close', np.float64),
        ('high_limited', np.float64),
        ('low_limited', np.float64)
    ]

    _FUTURE_FIELDS = _STOCK_FIELDS + [('open_interest', np.int32), ('prev_settlement', np.float64)]

    _STOCK_FIELD_DTYPE = np.dtype(_STOCK_FIELDS)
    _FUTURE_FIELD_DTYPE = np.dtype(_FUTURE_FIELDS)

    @staticmethod
    def _tick_dtype_for(instrument):
        if instrument.type == 'Future':
            return BundleDataSource._FUTURE_FIELD_DTYPE
        else:
            return BundleDataSource._STOCK_FIELD_DTYPE

    @staticmethod
    def _get_item(obj, key, default):
        if key == 'close':
            # Snapshot 对象没有 close 属性
            key = 'last'

        try:
            result = obj[key]
        except (ValueError, AttributeError, KeyError):
            result = default

        if key == 'datetime':
            if isinstance(result, datetime.datetime):
                result = convert_dt_to_int(result)

        return result

    def _update_last_bar_by_snapshot(self, bars, fields, snapshot):
        if not snapshot:
            return bars
        env = Environment.get_instance()
        result = bars.copy()
        """
        在夜盘的情况下，此处传入的 bars 截止到 calendar_dt 当天，也就是不包含当前交易日的日线。
        所以使用 snapshot 更新的时候需要在 bars 末尾补充一根日线，并砍掉 bars 中的第一根日线。ß
        """
        if isinstance(fields, str):
            if env.trading_dt != env.calendar_dt:
                result[0] = self._get_item(snapshot, fields, np.nan)
                result = np.roll(result, -1, axis=0)
                return result
            result[-1] = self._get_item(snapshot, fields, np.nan)
            return result

        if env.trading_dt != env.calendar_dt:
            for f in bars.dtype.names:
                result[0][f] = self._get_item(snapshot, f, np.nan)
            result = np.roll(result, -1, axis=0)
        else:
            for f in bars.dtype.names:
                result[-1][f] = self._get_item(snapshot, f, np.nan)
        return result

    def history_ticks(self, instrument, count, dt):
        market_code = instrument.market_code
        trading_dt = dt
        if instrument.type == 'Future':
            trading_dt = self.get_future_trading_date(dt)

        results = []
        need = count

        trading_date_int = int(trading_dt.strftime("%Y%m%d"))
        date_int = int(dt.strftime("%Y%m%d"))
        time_int = int(dt.strftime("%H%M%S%f")) // 1000
        ticks_arr = self.tick_loader.get_ticks_by_date(market_code, trading_date_int)

        if ticks_arr is not None:
            arr = ticks_arr[
                ((ticks_arr["date"] == date_int) & (ticks_arr["time"] <= time_int))
            ]
            results.append(arr)
            need -= len(arr)
        original_dt = trading_dt
        trading_dt = self.get_previous_trading_date(trading_dt)
        while need > 0:
            trading_date_int = int(trading_dt.strftime("%Y%m%d"))
            ticks_arr = self.tick_loader.get_ticks_by_date(market_code, trading_date_int)
            if ticks_arr is not None:
                results.append(ticks_arr)
                need -= len(ticks_arr)
            else:
                if (original_dt - trading_dt).days > 31:
                    break

            trading_dt = self.get_previous_trading_date(trading_dt)

        if not results:
            return None

        results_arr = np.concatenate(results[::-1])[-count:]
        if len(results_arr) == 0:
            return

        tick_list = []
        for idx in range(len(results_arr)):
            raw_tick = results_arr[idx]

            trading_dt = convert_date_time_ms_int_to_datetime(raw_tick["date"], raw_tick["time"])
            if instrument.type == 'Future':
                trading_dt = self.get_future_trading_date(trading_dt)

            raw_tick = self._process_raw_tick(raw_tick)

            tick = LazyTick(instrument, raw_tick, trading_dt.date())
            tick_list.append(tick)

        return tick_list

    def history_bars(self, instrument, bar_count, frequency, fields, dt,
                     skip_suspended=True, include_now=False, adjust_type='pre',
                     adjust_orig=None):
        if frequency == '1d':
            env = Environment.get_instance()
            bars = self._base_data_source.history_bars(instrument, bar_count, frequency, fields, dt,
                                                       skip_suspended=skip_suspended, include_now=include_now,
                                                       adjust_type=adjust_type, adjust_orig=adjust_orig)
            if not include_now or len(bars) <= 0:
                return bars

            sys_frequency = env.config.base.frequency
            return self._update_last_bar_by_snapshot(bars, fields, self.current_snapshot(instrument, sys_frequency, dt))

        if frequency == '1w':
            env = Environment.get_instance()
            sys_frequency = env.config.base.frequency

            if sys_frequency == '1m' or sys_frequency == 'tick':
                dt = self.get_previous_trading_date(dt)
                return self._base_data_source.history_bars(instrument, bar_count, frequency, fields, dt,
                                                           skip_suspended=skip_suspended, include_now=include_now,
                                                           adjust_type=adjust_type, adjust_orig=adjust_orig)

            if sys_frequency == '1d':
                return self._base_data_source.history_bars(instrument, bar_count, frequency, fields, dt,
                                                       skip_suspended=skip_suspended, include_now=include_now,
                                                       adjust_type=adjust_type, adjust_orig=adjust_orig)
        resample = int(frequency[:-1])
        original_dt = dt

        if skip_suspended and instrument.type == 'stock':
            # 过滤停牌数据
            while self.is_suspended(instrument.market_code, [dt])[0]:
                dt = self.get_previous_trading_date(dt)
            trade_date = dt
        elif instrument.type in ['Future', 'Option', 'Spot']:
            trade_date = self.get_future_trading_date(dt)
        else:
            trade_date = dt

        results = []
        need = bar_count

        if adjust_type == 'none' or instrument.type in {'Future', 'INDX'} or (
                isinstance(fields, str) and fields not in FIELDS_REQUIRE_ADJUSTMENT):
            def do_adjust(pre_adjust, date):
                return pre_adjust
        else:
            ex_cum_factors = self._base_data_source.get_ex_cum_factor(instrument.market_code)
            if ex_cum_factors is not None:
                dates = ex_cum_factors['start_date']
                factors = ex_cum_factors['ex_cum_factor']

                def _factor_for_date(d):
                    d = np.uint64(convert_date_to_int(d))
                    if d < dates[0]:
                        return 1
                    if d > dates[-1]:
                        return factors[-1]
                    pos = bisect_right(dates, d)
                    return factors[pos - 1]

                if adjust_type == 'pre':
                    base_factor = _factor_for_date(adjust_orig)
                else:
                    base_factor = 1.0

                def do_adjust(pre_adjust, date):
                    factor = _factor_for_date(date)
                    if factor == base_factor:
                        return pre_adjust

                    factor /= base_factor

                    if isinstance(fields, str):
                        if fields in PRICE_FIELDS:
                            return pre_adjust * factor
                        elif fields == 'volume':
                            return pre_adjust * (1 / factor)
                        else:
                            # should not get here
                            return pre_adjust
                    else:
                        result = pre_adjust.copy() if resample == 1 else bars
                        for f in fields:
                            if f in PRICE_FIELDS:
                                result[f] *= factor
                            elif f == 'volume':
                                result[f] *= (1 / factor)

                        return result
            else:
                def do_adjust(pre_adjust, date):
                    return pre_adjust

        def assure_fields(data):
            if isinstance(fields, str):
                return data[fields]
            elif fields is None:
                return data
            else:
                return data[fields]

        bars = self._minute_bars_of_day(instrument, to_date_int(trade_date))
        if bars is not None:
            if not self._are_fields_valid(fields, bars.dtype.names):
                raise RQInvalidArgument("invalid fileds: {}".format(fields))

            # dt 是当天0点0时0分
            # ignore seconds because tick has seconds
            odt = original_dt
            dt1 = odt.year * 1e10 + odt.month * 1e8 + odt.day * 1e6 + odt.hour * 1e4 + odt.minute * 1e2
            dt1 = np.uint64(dt1)
            bars = bars[bars['datetime'] <= dt1]

            if len(bars) > 0:
                include_last = include_now
                if bars['datetime'][-1] != dt1:
                    include_last = True

                if resample != 1:
                    bars = resample_bars(instrument, bars, fields, resample, include_last)
                else:
                    bars = assure_fields(bars)

                if len(bars) > 0:
                    bars = do_adjust(bars, trade_date)
                    results = [bars]
                    need = bar_count - len(bars)

        dt = trade_date

        while need > 0:
            dt = self.get_previous_trading_date(dt)
            if skip_suspended and instrument.type == 'stock':
                while self.is_suspended(instrument.market_code, [dt])[0]:
                    dt = self.get_previous_trading_date(dt.date())

            # 取一天的数据
            bars = self._minute_bars_of_day(instrument, to_date_int(dt))
            if bars is None:
                if (original_dt - dt).days > 31:
                    break
                else:
                    continue
            if not self._are_fields_valid(fields, bars.dtype.names):
                raise RQInvalidArgument("invalid fileds: {}".format(fields))

            if resample != 1:
                bars = resample_bars(instrument, bars, fields, resample)
            else:
                bars = assure_fields(bars)

            bars = do_adjust(bars, dt)
            results.append(bars)
            need -= len(bars)

        if not results:
            return self._get_minbar_store(instrument).get_empty(fields, instrument.type)

        return np.concatenate(results[::-1])[-bar_count:]

    def get_yield_curve(self, start_date, end_date, tenor=None):
        return self._base_data_source.get_yield_curve(start_date, end_date, tenor)

    def get_split(self, market_code):
        return self._base_data_source.get_split(market_code)

    def available_data_range(self, frequency):
        if frequency == 'tick':
            _, e = self._base_data_source.available_data_range('1d')
            return datetime.date(2010, 1, 4), e
        return self._base_data_source.available_data_range('1d')

    def get_merge_ticks(self, market_code_list, trading_date, last_dt=None):
        env = Environment.get_instance()

        trading_date_int = int(trading_date.strftime("%Y%m%d"))
        today_tick_board = {}
        market_code_map = {}

        for idx, market_code in enumerate(sorted(set(market_code_list))):
            market_code_map[idx] = market_code
            ticks_arr = self.tick_loader.get_ticks_by_date(market_code, trading_date_int)
            if ticks_arr is None:
                continue

            # append idx columns
            ticks_arr = nprf.append_fields(ticks_arr, 'market_code', np.full(len(ticks_arr), idx), usemask=False)
            today_tick_board[market_code] = ticks_arr

        # merge ticks arrays into one
        ticks_list = list(today_tick_board.values())
        if len(ticks_list) == 0:
            return
        merge_ticks = np.concatenate(ticks_list)

        merge_ticks.sort(kind='mergesort', order=("date", "time"))

        if last_dt is not None:
            time_arr = merge_ticks["date"].astype(np.uint64) * 10 ** 9 + merge_ticks["time"]
            last_idx = time_arr.searchsorted(convert_dt_to_int(last_dt) * 1000)
            merge_ticks = merge_ticks[last_idx:]
            if len(merge_ticks) > 0:
                merge_ticks = merge_ticks[1:]

        for raw_tick in merge_ticks:
            market_code = market_code_map[raw_tick["market_code"]]
            raw_tick = self._process_raw_tick(raw_tick)
            tick = LazyTick(env.data_proxy.instruments(market_code), raw_tick, trading_date)
            yield tick

    def _process_raw_tick(self, raw_tick):
        raw_tick = dict(zip(raw_tick.dtype.names, raw_tick))
        raw_tick["datetime"] = convert_date_time_ms_int_to_datetime(raw_tick["date"], raw_tick["time"])
        raw_tick["asks"] = [raw_tick["a{}".format(i)] for i in range(1, 6)]
        raw_tick["bids"] = [raw_tick["b{}".format(i)] for i in range(1, 6)]
        raw_tick["ask_vols"] = [raw_tick["a{}_v".format(i)] for i in range(1, 6)]
        raw_tick["bid_vols"] = [raw_tick["b{}_v".format(i)] for i in range(1, 6)]
        return raw_tick

    def _on_tick(self, event):
        tick = event.tick
        self._tick_board[tick.market_code] = tick

    def get_share_transformation(self, market_code):
        return self._base_data_source.get_share_transformation(market_code)

    @lru_cache(1024)
    def get_algo_bar(self, id_or_ins, start_min, end_min, dt):
        if not isinstance(id_or_ins, Instrument):
            id_or_ins = next(iter(self.get_instruments([id_or_ins])), None)
        if id_or_ins is None:
            return
        bars = self._algo_store.get_bars(id_or_ins, start_min, end_min)
        market_code = id_or_ins.market_code
        if bars is None:
            raise RuntimeError(
                "算法单异常:分钟数据缺失或分钟时间范围是非交易时段, 请调整时间范围或尝试更新数据 yhsdk update-data --minbar {}".format(market_code)
            )
        date_int = to_date_int(dt)
        pos = bars["date"].searchsorted(date_int)
        if len(bars) == pos:
            raise RuntimeError("算法单异常:分钟数据缺失, 请更新数据 yhsdk update-data --minbar {}".format(market_code))
        if bars[pos]["date"] != date_int:
            return
        return bars[pos]

    def get_open_auction_volume(self, instrument, dt):
        # type: (Instrument, datetime) -> float
        if self._auto_update_bundle and self._open_auction_volumes.init:
            volume = self._open_auction_volumes.get_open_auction_volume(instrument, dt)
        else:
            volume = self.get_open_auction_bar(instrument, dt)['volume']
        return volume
    