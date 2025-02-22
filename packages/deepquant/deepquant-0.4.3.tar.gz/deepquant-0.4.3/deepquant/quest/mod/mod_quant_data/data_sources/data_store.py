import os
import glob
import datetime
from typing import Container, Optional, Tuple, List
from collections import namedtuple

import h5py
import hdf5plugin  # noqa for hdf5-blosc
import numpy as np
import pandas as pd
import deepquant.quest.datac as yhdatac
from deepquant.quest.data.base_data_source.storages import h5_file, FuturesTradingParameters
from deepquant.quest.utils.logger import system_log
from deepquant.quest.utils.functools import lru_cache
from . import utils
from deepquant.quest.utils.i18n import gettext as _

from deepquant.quest.const import ALGO, COMMISSION_TYPE
from deepquant.quest.utils.logger import user_system_log
from deepquant.quest.utils import safe_div
from deepquant.quest.data.bundle import AutomaticUpdateBundle
from deepquant.quest.environment import Environment
from deepquant.quest.model.instrument import Instrument


@lru_cache(1024)
def date_to_number(dt):
    # return date 18-12-15 like 181215
    return dt.year * 10000 + dt.month * 100 + dt.day


@lru_cache(1024)
def time_to_number(dt):
    # return time 18:12:15 like 181250000
    return dt.hour * 10 ** 7 + dt.minute * 10 ** 5 + dt.second * 10 ** 3 + dt.microsecond / 1000


class AbstractMinBarStore:
    def get_minute_bar(self, market_code, date, fields):
        # type: (str, int, Optional[Container]) -> np.ndarray
        raise NotImplementedError

    def get_date_range(self, market_code):
        # type: (str) -> Tuple[int, int]
        raise NotImplementedError

    def get_empty(self, fields, instrument_type):
        raise NotImplementedError


class H5MinBarStore(AbstractMinBarStore):
    def __init__(self, directory, dtypes_map=utils.DTYPE_MAP):
        self._directory = directory
        self._dtypes_map = dtypes_map
        self._file_map = {}
        for root, dirs, files in os.walk(self._directory):
            for file in files:
                self._file_map[file] = os.path.join(root, file)

    @lru_cache(1024)
    def _get_h5_file_path(self, market_code):
        for file_name in (market_code + ".h5", market_code + "-sample.h5"):
            h5_file_path = self._file_map.get(file_name)
            if h5_file_path:
                return h5_file_path
        else:
            raise RuntimeError("Missing data for {}.".format(market_code))

    @lru_cache(None)
    def _get_index(self, market_code):
        with h5_file(self._get_h5_file_path(market_code)) as h5:
            try:
                return h5["index"][()]
            except KeyError:
                # index 不存在，可能是更新 bundle 时 get_price 返回为空，即行情不存在
                return

    def get_minute_bar(self, market_code, date, fields):
        try:
            index = self._get_index(market_code)
            if index is None:
                return
        except RuntimeError:
            return None
        pos = index["date"].searchsorted(date)
        if pos == len(index) or index["date"][pos] != date:
            return
        left = index["line_no"][pos]
        with h5_file(self._get_h5_file_path(market_code)) as h5:
            data = h5["data"]
            try:
                right = index["line_no"][pos + 1]
            except IndexError:
                # real IO hear
                right = len(data)

            # real IO hear
            data = data[left:right]
            fields = fields or data.dtype.names

            # change type
            dtype = [("high_limited", np.float64), ("low_limited", np.float64)]
            for field in fields:
                if field == 'orig_time':
                    dtype.append((field, np.uint64))
                elif field == 'volume':
                    dtype.append((field, np.float64))
                elif field in {"high_limited", "low_limited"}:
                    continue
                else:
                    dtype.append((field, data.dtype[field]))
            dtype = np.dtype(dtype)

            result = np.empty(shape=(len(data),), dtype=dtype)
            for f in fields:
                result[f][:] = data[f]
            if len(fields) == 1:
                return result[fields[0]]
            return result

    def get_date_range(self, market_code):
        try:
            with h5_file(self._get_h5_file_path(market_code)) as h5:
                data = h5["data"]
                return int(data["datetime"][0] / 1000000), int(data["datetime"][-1] / 1000000)
        except RuntimeError:
            return 19800101, 19800101

    def get_empty(self, fields, instrument_type):
        return self._get_empty(tuple(fields), instrument_type)

    @lru_cache(None)
    def _get_empty(self, fields, instrument_type):
        dtypes = self._dtypes_map[instrument_type]
        if not fields:
            dtype = dtypes.dtype
        else:
            dtype = []
            for field in fields:
                if field == "datetime":
                    dtype.append((field, np.uint64))
                elif field == 'volume':
                    dtype.append((field, np.float64))
                elif field in {"high_limited", "low_limited"}:
                    dtype.append((field, np.float64))
                else:
                    try:
                        dtype.append((field, dtypes[field]))
                    except KeyError:
                        return None
            dtype = np.dtype(dtype)
        return np.empty(0, dtype=dtype)


class H5TicksLoader(object):
    DISH_COUNT = 5

    FIELDS = [
                 ('date', '<u4', 1),
                 ('time', '<u4', 1),
                 ('last_price', '<f8', 1),
                 ('high_price', '<f8', 1),
                 ('low_price', '<f8', 1),
                 ('volume', '<f8', 1),
                 ('open_interest', '<f8', 1),
                 ('total_turnover', '<f8', 1),
             ] + [
                 (tmpl.format(i), '<f8', 1) for i in range(1, 1 + DISH_COUNT) for tmpl in ('a{}', 'b{}')
             ] + [
                 (tmpl.format(i), '<f8', 1) for i in range(1, 1 + DISH_COUNT) for tmpl in ('a{}_v', 'b{}_v')
             ]

    DTYPES = [(name, dt) for name, dt, scale in FIELDS]
    COLUMNS = [i[0] for i in FIELDS]

    def __init__(self, h5_tick_path):
        self._path = h5_tick_path

    @lru_cache(1024)
    def _get_h5_file_path(self, market_code):
        for file_name in (market_code + ".h5", market_code + "-sample.h5"):
            path = os.path.join(self._path, file_name)
            if os.path.exists(path):
                return path
        else:
            raise RuntimeError("Missing data for {}.".format(market_code))

    @lru_cache(1024)
    def get_ticks_by_date(self, market_code, date):
        with h5_file(self._get_h5_file_path(market_code)) as h5:
            try:
                tick = h5[str(date)][()]
                ticks = tick[(tick['time'] >= 9150000) & (tick['time'] <= 150003000)]
            except KeyError:
                return None
            new_ticks = np.zeros(len(ticks), dtype=self.DTYPES)
            for name, _, scale in self.FIELDS:
                try:
                    new_ticks[name] = ticks[name] / float(scale)
                except ValueError:
                    pass
            return new_ticks


class RqdataTicksLoader(object):
    """通过访问tickd获取tick相关数据"""
    DISH_COUNT = 5

    DTYPES = [
                 ('date', '<u4'),
                 ('time', '<u4'),
                 ('last_price', '<f8'),
                 ('high_price', '<f8'),
                 ('low_price', '<f8'),
                 ('volume', '<f8'),
                 ('open_interest', '<f8'),
                 ('total_turnover', '<f8'),
             ] + [
                 (tmpl.format(i), '<f8') for i in range(1, 1 + DISH_COUNT) for tmpl in ('a{}', 'b{}')
             ] + [
                 (tmpl.format(i), '<f8') for i in range(1, 1 + DISH_COUNT) for tmpl in ('a{}_v', 'b{}_v')
             ]
    FIELD_NAMES = [f[0] for f in DTYPES]

    def __init__(self):
        system_log.debug("RqdataTicksLoader initiated")

    def get_ticks_by_date(self, market_code, date):
        try:
            # 通过yhdatac底层拿到未处理数据(直接访问rqdatad) ENG-9124
            return self.get_data_by_client(market_code, date)
        except:
            # yhdatac的底层已经改变 数据将通过api获得
            system_log.info('The underlying layer of yhdatac has changed and the data will be obtained through api')
            self.get_ticks_by_date = self.get_ticks_by_api
            return self.get_ticks_by_api(market_code, date)

    def get_data_by_client(self, market_code, date):
        client = yhdatac.client.get_client()
        data = client.execute("get_tickbar", market_code, date, date, list(self.FIELD_NAMES), "cn")
        if len(data) == 0:
            return None
        data = data[0][1]
        data = [np.frombuffer(*data[name]) for name in self.FIELD_NAMES]
        data = np.array(list(zip(*data)), dtype=self.DTYPES)
        return data

    def get_ticks_by_api(self, market_code, date):
        # noinspection PyUnresolvedReferences
        df = yhdatac.get_price(market_code, date, date, "tick")
        if df is None:
            return None
        df = df.reset_index()
        df["date"] = df.orig_time.dt.date.apply(date_to_number)
        df["time"] = df.orig_time.dt.time.apply(time_to_number)
        if not "open_interest" in df.columns:
            df["open_interest"] = 0.0
        df = df[self.FIELD_NAMES]
        new_ticks = np.array([tuple(d) for d in df.values], dtype=self.DTYPES)
        return new_ticks


class AlgoStore:

    def __init__(self, path, min_path):
        self._path = path
        os.makedirs(path, exist_ok=True)
        self._file_map = {}
        for file in glob.glob(os.path.join(min_path, "**/*.h5"), recursive=True):
            market_code, _ = os.path.splitext(os.path.basename(file))
            self._file_map[market_code] = file

    def _get_algo_file_path(self, start_min, end_min):
        return os.path.join(self._path, "algo_{}_{}.h5".format(start_min, end_min))

    def _is_latest(self, market_code, start_min, end_min):
        """ algo数据是否已最新 """
        min_h5 = self._file_map.get(market_code)
        algo_h5 = self._get_algo_file_path(start_min, end_min)
        if not (min_h5 and os.path.exists(min_h5) and algo_h5 and os.path.exists(algo_h5)):
            return False
        with h5py.File(min_h5, mode="r") as h5:
            latest_date = h5["index"][-1]["date"]
        with h5py.File(algo_h5, mode="r") as h5:
            if market_code not in h5.keys():
                return False
            algo_latest_date = h5[market_code][-1]["date"]
            if algo_latest_date < latest_date:
                return False
        return True

    DTYPES = {
        "date": "<u4",
        "VWAP": "<f8",
        "TWAP": "<f8",
        "volume": "<u8",
    }

    @staticmethod
    def _append(origin, new):
        origin_len, new_len = len(origin), len(new)
        origin.resize(origin_len + new_len, axis=0)
        origin[origin_len: origin_len + new_len] = new

    def _update(self, instrument, start_min, end_min):
        market_code = instrument.market_code
        file = self._file_map.get(market_code)
        if not file:
            return
        algo_file = self._get_algo_file_path(start_min, end_min)
        user_system_log.info("正在计算算法单数据，请稍后.")
        last_date = None
        if os.path.exists(algo_file):
            with h5py.File(algo_file, mode="r") as h5:
                if market_code in h5.keys() and len(h5[market_code]) > 0:
                    last_date = h5[market_code][-1]["date"]
        with h5py.File(file, mode="r") as h5:
            index = h5["index"][:]
            if last_date:
                index = index[index["date"] > last_date]
            df = pd.DataFrame(h5["data"]["datetime", "close", "volume", "total_turnover"][index[0]["line_no"]:])
        df.index += index[0]["line_no"]
        df.loc[index["line_no"], "date"] = index["date"]
        df["date"].fillna(method="ffill", inplace=True)
        _date = df["datetime"] // 1000000 * 1000000
        _start_dt, _end_dt = _date + start_min * 100, _date + end_min * 100
        df = df[(df["datetime"] >= _start_dt) & (df["datetime"] <= _end_dt)]
        if df.empty and last_date is None:
            # 无效的分钟时间范围
            return
        algo_df = pd.DataFrame()
        algo_func_map = {
            ALGO.VWAP: lambda _df: safe_div(_df["total_turnover"].sum(), _df["volume"].sum()) / instrument.contract_multiplier,
            ALGO.TWAP: lambda _df: _df["close"].mean(),
        }
        if df.empty:
            for algo in algo_func_map.keys():
                algo_df[algo.value] = np.nan
            algo_df["volume"] = np.nan
        else:
            group = df.groupby("date")
            for algo, func in algo_func_map.items():
                algo_df[algo.value] = group.apply(func)
            algo_df["volume"] = group["volume"].sum()
        # 存在某些日期数据交易时段会变化，如节假日后第一天缺失夜盘或者某些合约突然就取消夜盘了，计算夜盘时段无数据，则会漏了一些日期，
        # 补全日期方便后续比较是否更新到最新
        algo_df = algo_df.reindex(index["date"])
        algo_df["volume"] = algo_df["volume"].fillna(value=0)
        algo_df.reset_index(inplace=True)
        records = algo_df.to_records(index=False, column_dtypes=self.DTYPES)
        with h5py.File(algo_file, mode="a") as h5:
            if market_code in h5.keys():
                self._append(h5[market_code], records)
            else:
                h5.create_dataset(
                    name=market_code, data=records, chunks=True, compression=9, shuffle=False, maxshape=(None,)
                )
        return records

    @lru_cache(1024)
    def get_bars(self, instrument, start_min, end_min):
        market_code = instrument.market_code
        if self._is_latest(market_code, start_min, end_min):
            with h5_file(self._get_algo_file_path(start_min, end_min), mode="r") as h5:
                return h5[market_code][:]
        else:
            return self._update(instrument, start_min, end_min)


class OpenAuctionVolumeStore():

    def __init__(self, auto_update_bundle_path: str, end_date: datetime.date) -> None:
        if Environment.get_instance().yhdatac_init:
            try:
                yhdatac.get_open_auction_info("000001.XSHE", datetime.date.today(), datetime.date.today())
                self.init = True
                self._auto_update_bundle_module = AutomaticUpdateBundle(
                    path=auto_update_bundle_path,
                    filename="open_auction_volume.h5",
                    api=self.get_open_auction_info,
                    fields=["volume"],
                    end_date=end_date,
                )
            except yhdatac.errors.PermissionDenied:
                user_system_log.warn(_("deepquant.quest.datac does not have permission to obtain open auction info data, daily bundle will be used for calculation."))
                self.init = False
        else:
            self.init = False
        
    def get_open_auction_volume(self, instrument: Instrument, dt: datetime.datetime) -> float:
        data = self._auto_update_bundle_module.get_data(instrument, dt)
        if data is None:
            # 集合竞价时，如果某个合约没有任何的订单发出，则 rqdata 不会存储数据，此时认为 volume = 0
            volume = 0
        else: # 同上
            volume = 0 if len(data) == 0 else data['volume']
        return volume

    def get_open_auction_info(self, market_code: str, start_date: datetime.date, end_date: datetime.date, fields: List[str]) -> Optional[pd.DataFrame]:
        df = deepquant.quest.datac.get_open_auction_info(market_code, start_date, end_date, fields)
        if not (df is None or df.empty):
            env = Environment.get_instance()
            instrument = env.get_instrument(market_code)
            trading_dt = env.data_proxy._data_source.batch_get_trading_date(df.loc[market_code].index)
            completion_start_date = max(instrument.listed_date.date(), datetime.date(2005, 1, 4))
            completion_end_date = min(instrument.de_listed_date.date(), end_date)
            trading_dates = env.data_proxy._data_source.get_trading_dates(completion_start_date, completion_end_date)
            if len(trading_dt) != len(trading_dates):
                # 将时间点设为每天上午9点，避免当前一日为非交易日时 searchsorted 找错索引
                completion_dt = pd.DatetimeIndex(list(set(trading_dates).difference(set(trading_dt)))) + datetime.timedelta(hours=9)
                arr = df.to_records()
                arr_zero = np.zeros((completion_dt.shape[0], ), dtype=arr.dtype)
                arr_zero['orig_time'] = completion_dt
                arr_zero['market_code'] = instrument.market_code
                arr = np.sort(np.concatenate((arr, arr_zero)))
                df = pd.DataFrame(arr)
                df = df.set_index(['market_code', 'orig_time'])
            return df
        return None


FUTURES_TRADING_PARAMETERS_FIELDS = ["long_margin_ratio", "short_margin_ratio", "commission_type", "open_commission_ratio", "close_commission_ratio", "close_commission_today_ratio"]


class FuturesTradingParametersStore():
    COMMISSION_TYPE_MAP = {
        0: COMMISSION_TYPE.BY_MONEY,
        1: COMMISSION_TYPE.BY_VOLUME
    }

    futures_trading_parameters_dtype = np.dtype([
        ('market_code', 'O'),
        ('trading_date', 'datetime64[ns]'),
        ('long_margin_ratio', '<f8'),
        ('short_margin_ratio', '<f8'),
        ('commission_type', '<f8'),
        ('open_commission_ratio', '<f8'),
        ('close_commission_ratio', '<f8'),
        ('close_commission_today_ratio', '<f8'),
    ])

    def __init__(self, auto_update_bundle_path: str, end_date: datetime.date, custom_future_info: dict) -> None:
        self._env = Environment.get_instance()
        if self._env.yhdatac_init:
            if yhdatac.__version__ <= "2.11.12":
                user_system_log.warning(_("yhalpha already supports backtesting using futures historical margins and rates, please upgrade deepquant.quest.datac to version 2.11.12 and above to use it"))
            try:
                yhdatac.futures.get_trading_parameters("A2401")
                self.init = True
                self._auto_update_bundle_module = AutomaticUpdateBundle(
                    path=auto_update_bundle_path,
                    filename="futures_trading_parameters.h5",
                    api=self.get_trading_parameters,
                    fields=FUTURES_TRADING_PARAMETERS_FIELDS,
                    end_date=end_date,
                    start_date=20100401,  # futures trading parameters data available since 2010.4
                )
                self._custom_data = custom_future_info
            except yhdatac.errors.PermissionDenied:
                user_system_log.warning(_("YHDatac does not have permission to obtain futures histrical trading parameters, \"config.base.futures_time_series_trading_parameters\" will be disabled."))
                self.init = False
        else:
            self.init = False

    @lru_cache(128)
    def get_futures_trading_parameters(self, instrument: Instrument, dt: datetime.datetime) -> Optional[FuturesTradingParameters]:
        data = self._auto_update_bundle_module.get_data(instrument, dt)
        if data is None:
            user_system_log.warn(_("{}'s trading parameters are abnormal on {}, the lastst parameters will be used for calculations.\nPlease contract RiceQuant to repair: 0755-26569969".format(instrument.market_code, dt)))
            return None
        if self._custom_data:
            custom_info = self._custom_data.get(instrument.market_code) or self._custom_data.get(instrument.underlying_symbol)
            if custom_info:
                data = self._set_custom_info(data, custom_info)
        return self._to_namedtuple(data)
    
    def _set_custom_info(self, data: np.array, custom_info: dict) -> np.array:
        for field in custom_info:
            if field == "commission_type":
                data[field] = 0 if custom_info[field] == COMMISSION_TYPE.BY_MONEY else 1
            else:
                data[field] = custom_info[field]
        return data

    def _to_namedtuple(self, arr: np.array) -> FuturesTradingParameters:
        dic = dict(zip(arr.dtype.names, arr))
        del dic['trading_dt']
        dic['commission_type'] = self.COMMISSION_TYPE_MAP[dic['commission_type']]
        return FuturesTradingParameters(**dic)

    def get_trading_parameters(self, market_code: str, start_date: datetime.date, end_date: datetime.date, fields=None) -> Optional[pd.DataFrame]:
        # yhdatac 数据处理函数，用于将获取到的 rqdata 数据整理为 yhalpha 框架所需的数据结构（部分参数名称会产生变化）
        if ("88" or "888" or "889") in market_code:
            df = self._get_trading_parameters_of_continuous(market_code, start_date, end_date)
        else:
            df = yhdatac.futures.get_trading_parameters(market_code, start_date, end_date, fields=["long_margin_ratio", "short_margin_ratio", "commission_type", "open_commission", "close_commission", "close_commission_today"])
        if not (df is None or df.empty):
            arr = df.to_records()
            new_arr = np.zeros((arr.shape[0]), dtype=self.futures_trading_parameters_dtype)
            new_arr['market_code'] = market_code
            new_arr[['trading_date', 'long_margin_ratio', 'short_margin_ratio', 'open_commission_ratio', 'close_commission_ratio', 'close_commission_today_ratio']] = \
                arr[['trading_date', 'long_margin_ratio', 'short_margin_ratio', 'open_commission', 'close_commission', 'close_commission_today']]
            new_arr['commission_type'] += np.where(arr['commission_type'] == 'by_volume', 1, 0)
            df = pd.DataFrame(new_arr)
            df = df.set_index(['market_code', 'trading_date'])
            return df
        return None
    
    def _get_trading_parameters_of_continuous(self, market_code: str, start_date: datetime.date, end_date: datetime.date) -> Optional[pd.DataFrame]:
        # 获取期货主力连续合约的历史交易参数
        underlying_symbol = self._env.get_instrument(market_code).underlying_symbol
        dominant = yhdatac.futures.get_dominant(underlying_symbol, start_date, end_date)
        if (dominant is None or dominant.empty):
            return None
        slice_list = []
        dominant_market_code, s, e = dominant.values[0], dominant.index[0].to_pydatetime().date(), dominant.index[0].to_pydatetime().date()
        last_date = dominant.index[-1].to_pydatetime().date()
        for i, v in dominant.items():
            if v != dominant_market_code:
                slice_list.append({"market_code": dominant_market_code, "start_date": s, "end_date": e})
                dominant_market_code = v
                s = i.to_pydatetime().date()
            e = i.to_pydatetime().date()
            if e == last_date:
                slice_list.append({"market_code": dominant_market_code, "start_date": s, "end_date": e})
        df = pd.DataFrame()
        for dic in slice_list:
            data = yhdatac.futures.get_trading_parameters(dic['market_code'], dic['start_date'], dic['end_date'], fields=["long_margin_ratio", "short_margin_ratio", "commission_type", "open_commission", "close_commission", "close_commission_today"])
            df = pd.concat([df, data])
        return df

