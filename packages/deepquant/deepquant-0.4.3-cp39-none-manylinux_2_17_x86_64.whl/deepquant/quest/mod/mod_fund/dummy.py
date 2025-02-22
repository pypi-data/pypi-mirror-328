from typing import Optional, Iterable

from deepquant.quest.model.instrument import Instrument
import deepquant.quest.datac
from deepquant.quest.data.base_data_source.storages import AbstractDayBarStore
from deepquant.quest.data.base_data_source.storage_interface import AbstractInstrumentStore, AbstractDividendStore, \
    AbstractSimpleFactorStore
from deepquant.quest.const import INSTRUMENT_TYPE
from deepquant.quest.apis.api_abstract import order, order_percent, order_shares, order_target_percent, order_target_value, \
    order_to, order_value


PERMISSION_ERROR = None


def raise_error(*_, **__):
    raise PERMISSION_ERROR


for api in (order, order_percent, order_shares, order_target_percent, order_target_value, order_to, order_value):
    api.register(INSTRUMENT_TYPE.PUBLIC_FUND)(raise_error)


class DummyDayBarStore(AbstractDayBarStore):
    get_bars = raise_error


class DummyInstrumentStore(AbstractInstrumentStore):
    @property
    def instrument_type(self):
        # type: () -> INSTRUMENT_TYPE
        return INSTRUMENT_TYPE.PUBLIC_FUND

    def get_instruments(self, id_or_syms):
        # type: (Optional[Iterable[str]]) -> Iterable[Instrument]
        return raise_error()

    @property
    def all_id_and_syms(self):
        # type: () -> Iterable[str]
        return deepquant.quest.datac.client.get_client().execute("__internal__get_instrument_list", "PublicFund")


class DummyDividendStore(AbstractDividendStore):
    def get_dividend(self, market_code):
        return raise_error()


class DummySplitStore(AbstractSimpleFactorStore):
    def get_factors(self, market_code):
        return raise_error()
