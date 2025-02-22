from typing import Iterable, Optional

import deepquant.quest.datac

from deepquant.quest.model.instrument import Instrument
from deepquant.quest.data.base_data_source.storages import AbstractDayBarStore, AbstractInstrumentStore
from deepquant.quest.const import INSTRUMENT_TYPE
from deepquant.quest.apis.api_abstract import buy_close, buy_open, sell_close, sell_open

PERMISSION_ERROR = None


def raise_error(*args, **kwargs):
    raise PERMISSION_ERROR


for api in (buy_close, buy_open, sell_close, sell_open):
    api.register(INSTRUMENT_TYPE.SPOT)(raise_error)


class DummyDayBarStore(AbstractDayBarStore):
    get_bars = raise_error


class DummyInstrumentStore(AbstractInstrumentStore):
    @property
    def instrument_type(self):
        # type: () -> INSTRUMENT_TYPE
        return INSTRUMENT_TYPE.SPOT

    @property
    def all_id_and_syms(self):
        # type: () -> Iterable[str]
        return deepquant.quest.datac.all_instruments("Spot").market_code

    def get_instruments(self, id_or_syms):
        # type: (Optional[Iterable[str]]) -> Iterable[Instrument]
        return raise_error()
