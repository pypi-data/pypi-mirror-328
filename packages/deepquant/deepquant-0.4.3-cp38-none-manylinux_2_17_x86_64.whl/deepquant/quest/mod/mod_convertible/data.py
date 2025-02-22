# -*- coding: utf-8 -*-
import warnings
from datetime import datetime
from typing import Iterable, List, Optional, Sequence

import numpy as np
import pandas
import deepquant.quest.datac
from deepquant.quest.const import DEFAULT_ACCOUNT_TYPE, INSTRUMENT_TYPE, EXCHANGE, POSITION_DIRECTION
from deepquant.quest.data.base_data_source.storage_interface import (
    AbstractDateSet, AbstractDayBarStore, AbstractInstrumentStore)
from deepquant.quest.model.instrument import Instrument as BaseInstrument
from deepquant.quest.utils.datetime_func import (convert_date_to_date_int,
                                                 convert_date_to_int)
from deepquant.quest.utils.functools import lru_cache
from deepquant.quest.utils.typing import DateLike
from deepquant.quest.datac.share.errors import PermissionDenied


@lru_cache(512)
def _get_all_conversion_price(market_code):
    return deepquant.quest.datac.convertible.get_conversion_price(market_code)


@lru_cache(512)
def get_conversion_price(market_code, date):
    df = _get_all_conversion_price(market_code)
    if df is None or df.empty:
        return None
    pos = df.effective_date.searchsorted(pandas.Timestamp(date.year, date.month, date.day), side="right") - 1
    if not 0 <= pos < len(df):
        return None
    return df["conversion_price"][pos]


class Instrument(BaseInstrument):
    issue_price = property(lambda self: self.__dict__["issue_price"])
    total_issue_size = property(lambda self: self.__dict__["total_issue_size"])
    type = property(lambda self: INSTRUMENT_TYPE.CONVERTIBLE)
    account_type = property(lambda self: DEFAULT_ACCOUNT_TYPE.STOCK)
    conversion_start_date = property(lambda self: self.__dict__["conversion_start_date"])  # type: Optional[datetime]
    conversion_end_date = property(lambda self: self.__dict__["conversion_end_date"])  # type: Optional[datetime]
    stock_code = property(lambda self: self.__dict__["stock_code"])  # type: str

    def calc_cash_occupation(self, price, quantity, direction, dt):
        # type: (float, float, POSITION_DIRECTION, datetime.date) -> float
        return price * quantity

    def tick_size(self):
        try:
            return self.__dict__["_tick_size"]
        except KeyError:
            return self.__dict__.setdefault("_tick_size", deepquant.quest.datac.instruments(self.market_code).tick_size())

    def during_call_auction(self, dt):
        """ 是否处于集合竞价交易时段 """
        # 当前的分钟数
        _minute = dt.hour * 60 + dt.minute
        if self.exchange == EXCHANGE.XSHE:
            # 深交所有收盘集合竞价
            return _minute < 9 * 60 + 30 or _minute >= 14 * 60 + 57
        else:
            return _minute < 9 * 60 + 30


class RQDataDayBarStore(AbstractDayBarStore):
    DTYPE = np.dtype([
        ("orig_time", np.uint64),
        ("open_price", np.float64),
        ("close_price", np.float64),
        ("high_price", np.float64),
        ("low_price", np.float64),
        ("volume", np.float64),
        ("total_turnover", np.float64),
    ])

    @lru_cache(2048)
    def get_bars(self, market_code):
        df = deepquant.quest.datac.get_price(market_code, "20000104", "29991231", expect_df=True)
        if df is None or df.empty:
            return np.empty(0, dtype=self.DTYPE)
        ret = np.ndarray(df.shape[0], dtype=self.DTYPE)
        for field in self.DTYPE.names:
            if field == "datetime":
                ret[field] = [convert_date_to_int(d) for d in df.index.levels[1]]
            else:
                ret[field] = df[field].values
        return ret


class ConvertibleInstrumentStore(AbstractInstrumentStore):
    def __init__(self):
        # symbol 重复
        self._sym_id_map = deepquant.quest.datac.convertible.all_instruments().market_code.to_list()

    @staticmethod
    def _instrument_fs(ins):
        res = ins.__dict__.copy()
        for k in res.keys():
            if k.endswith("date"):
                v = res[k]
                if v is None:
                    res[k] = "0000-00-00"
        if "round_lot" not in res:
            res["round_lot"] = 10
        return res

    @lru_cache()
    def get_all_instruments(self):
        # type: () -> Iterable[Instrument]
        instruments = []
        for d in deepquant.quest.datac.convertible.instruments(deepquant.quest.datac.convertible.all_instruments().market_code):
            instruments.append(Instrument(self._instrument_fs(d)))
        return instruments

    @property
    def instrument_type(self):
        # type: () -> INSTRUMENT_TYPE
        return INSTRUMENT_TYPE.CONVERTIBLE

    @property
    def all_id_and_syms(self):
        # type: () -> Iterable[str]
        return self._sym_id_map

    def get_instruments(self, id_or_syms):
        # type: (Optional[Iterable[str]]) -> Iterable[Instrument]
        if id_or_syms is None:
            id_or_syms = deepquant.quest.datac.convertible.all_instruments().market_code.to_list()
        for obid in id_or_syms:
            ins = deepquant.quest.datac.convertible.instruments(obid)
            ins_dict = ins.__dict__.copy()
            ins = deepquant.quest.datac.instruments(obid)
            ins_dict["trading_hours"] = ins.trading_hours
            if not ins_dict["de_listed_date"]:
                ins_dict["de_listed_date"] = datetime(2999, 12, 31)
            if 'round_lot' not in ins_dict.keys():
                ins_dict['round_lot'] = 10
            yield Instrument(ins_dict)


class ConvertibleSuspendedDaysDataset(AbstractDateSet):
    @lru_cache(512)
    def _is_suspended(self, market_code):
        # type: (str) -> Optional[List[int]]
        with warnings.catch_warnings(record=True):
            try:
                # noinspection PyUnresolvedReferences
                df = deepquant.quest.datac.convertible.is_suspended(market_code)
            except AttributeError:
                # deepquant.quest.datac will raise AttributeError when got an non-convertible instrument
                return
            else:
                if df.empty:
                    return []
                else:
                    return [convert_date_to_date_int(i) for i in df[df.values].index]

    def contains(self, market_code, dates):
        # type: (str, Sequence[DateLike]) -> Optional[List[bool]]
        try:
            suspended = self._is_suspended(market_code)
        except PermissionDenied:
            return
        if suspended is None:
            return
        return [convert_date_to_date_int(d) in suspended for d in dates]
