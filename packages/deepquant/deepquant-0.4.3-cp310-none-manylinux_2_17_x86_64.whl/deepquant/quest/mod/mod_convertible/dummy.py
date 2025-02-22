from typing import Iterable, Optional

import deepquant.quest.datac

from deepquant.quest.model.instrument import Instrument
from deepquant.quest.data.base_data_source.storage_interface import AbstractDayBarStore, AbstractInstrumentStore
from deepquant.quest.const import INSTRUMENT_TYPE
from deepquant.quest.apis.api_abstract import (
    order, order_to, order_shares, order_value, order_target_value, order_percent, order_target_percent, exercise
)


PERMISSION_ERROR = None


def raise_error(*_, **__):
    raise PERMISSION_ERROR


for api in (
    order, order_to, order_shares, order_value, order_target_value, order_percent, order_target_percent, exercise
):
    api.register(INSTRUMENT_TYPE.CONVERTIBLE)(raise_error)


class DummyDayBarStore(AbstractDayBarStore):
    get_bars = raise_error


class DummyInstrumentStore(AbstractInstrumentStore):
    @property
    def instrument_type(self):
        # type: () -> INSTRUMENT_TYPE
        return INSTRUMENT_TYPE.CONVERTIBLE

    @property
    def all_id_and_syms(self):
        # type: () -> Iterable[str]
        return deepquant.quest.datac.client.get_client().execute("__internal__get_instrument_list", "Convertible")

    def get_instruments(self, id_or_syms):
        # type: (Optional[Iterable[str]]) -> Iterable[Instrument]
        return raise_error()
