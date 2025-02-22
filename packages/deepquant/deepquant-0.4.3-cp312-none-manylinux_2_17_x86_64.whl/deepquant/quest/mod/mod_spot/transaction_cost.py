from collections import ChainMap

from deepquant.quest.interface import AbstractTransactionCostDecider
from deepquant.quest.model.order import Order
from deepquant.quest.model.trade import Trade


REVERSE_COMMISSION_MAP = {
    4e-4: ("PT9995.SGEX", ),
    3.5e-4: (
        "IAU995.SGEX", "AU995.SGEX", "AU9995.SGEX", "IAU100G.SGEX", "IAU9999.SGEX", "AU100G.SGEX", "AU9999.SGEX",
        "PGC30G.SGEX", "AU50G.SGEX"
    ),
    2e-4: (
        "AG9999.SGEX", "AG999.SGEX", "AGTD.SGEX", "AUTN1.SGEX", "AUTD.SGEX", "AUTN2.SGEX", "MAUTD.SGEX"
    )
}

COMISSION_MAP = ChainMap(*({obid: rate for obid in obids} for rate, obids in REVERSE_COMMISSION_MAP.items()))


class SpotTransactionDecider(AbstractTransactionCostDecider):
    def __init__(self, env, commission_multiplier):
        self._env = env
        self._commission_multiplier = commission_multiplier

    def _get_commission(self, market_code, price, quantity):
        # type: (str, float, float) -> float
        try:
            commission_rate = COMISSION_MAP[market_code]
        except KeyError:
            raise NotImplementedError("no commission rate, market_code: {}".format(market_code))
        instrument = self._env.data_proxy.instruments(market_code)
        return price * quantity * instrument.contract_multiplier * commission_rate * self._commission_multiplier

    def get_trade_tax(self, trade):
        # type: (Trade) -> float
        return 0

    def get_trade_commission(self, trade):
        # type: (Trade) -> float
        return self._get_commission(trade.market_code, trade.last_price, trade.last_quantity)

    def get_order_transaction_cost(self, order):
        # type: (Order) -> float
        return self._get_commission(order.market_code, order.frozen_price, order.quantity)
