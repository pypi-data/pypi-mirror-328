import pickle
from functools import lru_cache
from typing import Optional, Iterable
from numbers import Real
import datetime
from itertools import chain

import numpy as np
import deepquant.quest.datac

from deepquant.quest.model.instrument import Instrument as BaseInstrument
from deepquant.quest.const import CustomEnum, INSTRUMENT_TYPE, POSITION_DIRECTION, DEFAULT_ACCOUNT_TYPE, EXCHANGE
from deepquant.quest.data.base_data_source.storages import AbstractInstrumentStore, AbstractDayBarStore
from deepquant.quest.environment import Environment
from deepquant.quest.utils.datetime_func import convert_date_to_int
from deepquant.quest.utils.functools import lru_cache


def calc_margin(instrument, quantity, underlying_price, underlying_prev_close, prev_settlement):
    underlying = instrument.underlying_instrument
    if instrument.option_type == OPTION_TYPE.CALL:
        otm_value = max(instrument.strike_price - underlying_price, 0)
    else:
        otm_value = max(underlying_price - instrument.strike_price, 0)
    if underlying.type == INSTRUMENT_TYPE.FUTURE:
        margin_rate = instrument.underlying_instrument.margin_rate
        margin = prev_settlement + max(underlying_price * margin_rate - 0.5 * otm_value, 0.5 * underlying_price * margin_rate)
    elif underlying.type == INSTRUMENT_TYPE.ETF:
        if instrument.option_type == OPTION_TYPE.CALL:
            margin = prev_settlement + max(0.12 * underlying_prev_close - otm_value, 0.07 * underlying_prev_close)
        else:
            margin = min(
                prev_settlement + max(0.12 * underlying_prev_close - otm_value, 0.07 * instrument.strike_price),
                instrument.strike_price
            )
    elif underlying.type == INSTRUMENT_TYPE.INDX:
        if instrument.option_type == OPTION_TYPE.CALL:
            margin = prev_settlement + max(0.1 * underlying_prev_close - otm_value, 0.05 * underlying_prev_close)
        else:
            margin = prev_settlement + max(0.1 * underlying_prev_close - otm_value, 0.05 * instrument.strike_price)
    else:
        raise NotImplementedError("unsupported margin calculation of instrument: {}".format(instrument))
    return margin * instrument.contract_multiplier * quantity


# noinspection PyPep8Naming
class EXERCISE_TYPE(CustomEnum):
    AMERICAN = "A"
    EUROPEAN = "E"


# noinspection PyPep8Naming
class OPTION_TYPE(CustomEnum):
    CALL = "C"
    PUT = "P"


class Instrument(BaseInstrument):
    option_type = property(lambda self: OPTION_TYPE[self.__dict__["option_type"]])  # type: OPTION_TYPE
    exercise_type = property(lambda self: EXERCISE_TYPE[self.__dict__["exercise_type"]])  # type: EXERCISE_TYPE
    strike_price = property(lambda self: self.__dict__["strike_price"])  # type: Real

    @property
    def underlying_instrument(self):
        # type: () -> Optional[BaseInstrument]
        try:
            underlying_market_code = self.underlying_market_code
        except AttributeError:
            return
        return Environment.get_instance().data_proxy.instruments(underlying_market_code)

    @property
    def contract_multiplier(self):
        # TODO: dynamic contract_multiplier
        return super(Instrument, self).contract_multiplier

    @property
    def account_type(self):
        if self.exchange in {"SE", "SH"}:
            return DEFAULT_ACCOUNT_TYPE.STOCK
        else:
            return DEFAULT_ACCOUNT_TYPE.FUTURE

    def calc_cash_occupation(self, price, quantity, direction, dt):
        # type: (float, float, POSITION_DIRECTION, datetime.date) -> float
        if self.type != INSTRUMENT_TYPE.OPTION:
            return super(Instrument, self).calc_cash_occupation(price, quantity, direction, dt)
        if direction == POSITION_DIRECTION.LONG:
            return price * quantity * self.contract_multiplier
        else:
            env = Environment.get_instance()
            pos = env.portfolio.get_position(self.market_code, POSITION_DIRECTION.LONG)
            margin = calc_margin(self, quantity, pos.underlying_price, pos.underlying_prev_close, pos.prev_settlement)
            return margin - price * quantity * self.contract_multiplier

    def tick_size(self):
        try:
            return self.__dict__["_tick_size"]
        except KeyError:
            return self.__dict__.setdefault("_tick_size", deepquant.quest.datac.instruments(self.market_code).tick_size())

    def during_call_auction(self, dt):
        """ 是否处于集合竞价交易时段 """
        # 当前的分钟数
        _minute = dt.hour * 60 + dt.minute

        # 期货开盘时间
        start_time = self.trading_hours[0].start

        # -1 是因为获取到的时间都是开盘后1分钟，如 09:31
        start_minute = start_time.hour * 60 + start_time.minute - 1

        if self.exchange in [EXCHANGE.XSHG, EXCHANGE.XSHE]:
            # ETF期权和股票集合竞价时间相同
            return _minute < 9 * 60 + 30 or _minute >= 14 * 60 + 57
        else:
            return start_minute - 5 <= _minute < start_minute


class OptionInstrumentStore(AbstractInstrumentStore):
    def __init__(self):
        self._sym_id_map = deepquant.quest.datac.all_instruments("Option").market_code.to_list()

    @property
    def instrument_type(self):
        # type: () -> INSTRUMENT_TYPE
        return INSTRUMENT_TYPE.OPTION

    @property
    def all_id_and_syms(self):
        # type: () -> Iterable[str]
        return self._sym_id_map

    def get_instruments(self, id_or_syms):
        # type: (Optional[Iterable[str]]) -> Iterable[Instrument]
        if id_or_syms is None:
            id_or_syms = deepquant.quest.datac.all_instruments("Option").market_code.to_list()
        for obid in id_or_syms:
            ins = deepquant.quest.datac.instruments(obid)
            ins_dict = ins.__dict__.copy()
            if not ins_dict["listed_date"]:
                ins_dict["listed_date"] = datetime.datetime(1999, 1, 1)
            if not ins_dict["de_listed_date"]:
                ins_dict["de_listed_date"] = datetime.datetime(2999, 12, 31)
            yield Instrument(ins_dict)


class RQDataDayBarStore(AbstractDayBarStore):
    DTYPE = np.dtype([
        ("orig_time", np.uint64),
        ("open_price", np.float64),
        ("close_price", np.float64),
        ("high_price", np.float64),
        ("low_price", np.float64),
        ("volume", np.float64),
        ("total_turnover", np.float64),
        ("settlement", np.float64),
        ("prev_settlement", np.float64),
        ("open_interest", np.float64),
        ("contract_multiplier", np.float64),
    ])

    @lru_cache(2048)
    def get_bars(self, market_code):
        df = deepquant.quest.datac.get_price(market_code, "20000104", "29991231", expect_df=True)

        df = df.droplevel(0)
        if df is None or df.empty:
            return np.empty(0, dtype=self.DTYPE)
        ret = np.ndarray(df.shape[0], dtype=self.DTYPE)
        for field in self.DTYPE.names:
            if field == "datetime":
                ret[field] = [convert_date_to_int(d) for d in df.index]
            else:
                ret[field] = df[field].values
        return ret
