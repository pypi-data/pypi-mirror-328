from typing import Optional, Iterable

from deepquant.quest.model.instrument import Instrument
from deepquant.quest.data.base_data_source.storages import AbstractDayBarStore
from deepquant.quest.const import INSTRUMENT_TYPE
from deepquant.quest.apis.api_abstract import order, order_to, buy_open, buy_close, sell_open, sell_close, exercise

from .data import OptionInstrumentStore


PERMISSION_ERROR = None


def raise_error(*_, **__):
    raise PERMISSION_ERROR


for api in (order, order_to, buy_open, buy_close, sell_open, sell_close, exercise):
    api.register(INSTRUMENT_TYPE.OPTION)(raise_error)


class DummyDayBarStore(AbstractDayBarStore):
    get_bars = raise_error


class DummyInstrumentStore(OptionInstrumentStore):
    def get_instruments(self, id_or_syms):
        # type: (Optional[Iterable[str]]) -> Iterable[Instrument]
        return raise_error()
