from itertools import chain

import numpy as np
import deepquant.quest.datac
from deepquant.quest.const import DEFAULT_ACCOUNT_TYPE
from deepquant.quest.const import INSTRUMENT_TYPE
from deepquant.quest.const import POSITION_DIRECTION
from deepquant.quest.data.base_data_source.storages import AbstractDayBarStore
from deepquant.quest.data.base_data_source.storages import AbstractInstrumentStore
from deepquant.quest.environment import Environment
from deepquant.quest.model.instrument import Instrument
from deepquant.quest.utils.datetime_func import convert_date_to_int
from deepquant.quest.datac.errors import PermissionDenied

from deepquant.quest.utils.functools import lru_cache


class SpotInstrument(Instrument):
    def __init__(self, dic, tick_size):
        super(SpotInstrument, self).__init__(dic)
        self._tick_size = tick_size

    type = property(lambda self: INSTRUMENT_TYPE.SPOT)

    @property
    def account_type(self):
        return DEFAULT_ACCOUNT_TYPE.STOCK

    def tick_size(self):
        return self._tick_size
    
    def get_long_margin_ratio(self, dt):
        # type: (datetime.date) -> float
        return self.margin_rate
    
    def get_short_margin_ratio(self, dt):
        # type: (datetime.date) -> float
        return self.margin_rate

    def calc_cash_occupation(self, price, quantity, direction, dt):
        # type: (float, float, POSITION_DIRECTION, datetime.date) -> float
        if self.type != INSTRUMENT_TYPE.SPOT:
            return super(SpotInstrument, self).calc_cash_occupation(price, quantity, direction, dt)
        margin_multiplier = Environment.get_instance().config.base.margin_multiplier
        return price * quantity * self.contract_multiplier * self.margin_rate * margin_multiplier


class SpotInstrumentStore(AbstractInstrumentStore):
    def __init__(self):
        self._sym_id_map = {data.security_name: data.market_code for index, data in
                            deepquant.quest.datac.all_instruments("Spot").iterrows()}

    @property
    def instrument_type(self):
        # type: () -> INSTRUMENT_TYPE
        return INSTRUMENT_TYPE.SPOT

    @property
    def all_id_and_syms(self):
        # type: () -> Iterable[str]
        return chain(self._sym_id_map.keys(), self._sym_id_map.values())

    def get_instruments(self, id_or_syms):
        # type: (Optional[Iterable[str]]) -> Iterable[SpotInstrument]
        if id_or_syms is None:
            id_or_syms = deepquant.quest.datac.all_instruments("Spot").market_code.to_list()
        for obid in id_or_syms:
            ins = deepquant.quest.datac.instruments(obid)
            ins_dict = ins.__dict__.copy()
            yield SpotInstrument(ins_dict, ins.tick_size())


class SpotDaybarStore(AbstractDayBarStore):
    DTYPE = np.dtype([
        ("orig_time", np.uint64),
        ("open_price", np.float64),
        ("close_price", np.float64),
        ("high_price", np.float64),
        ("low_price", np.float64),
        ("volume", np.float64),
        ("total_turnover", np.float64),
    ])

    @lru_cache(128)
    def get_bars(self, market_code):
        # type: (str) -> np.ndarray
        try:
            df = deepquant.quest.datac.get_price(market_code, "20000104", "29991231", expect_df=True)
            df = df.droplevel(0)
        except PermissionDenied as err:
            raise PermissionError("无spot数据权限，请联系米筐技术支持。\n{}".format(err))
        if df is None or df.empty:
            return np.empty(0, dtype=self.DTYPE)
        ret = np.ndarray(df.shape[0], dtype=self.DTYPE)
        for field in self.DTYPE.names:
            if field == "datetime":
                ret[field] = convert_date_to_int(df.index)
            else:
                ret[field] = df[field].values
        return ret
