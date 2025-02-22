# -*- coding: utf-8 -*-

from deepquant.quest.const import SIDE
from deepquant.quest.interface import AbstractTransactionCostDecider


class ConvertibleTransactionDecider(AbstractTransactionCostDecider):
    """
    订单税费计算接口，通过实现次接口可以定义不同市场、不同合约的个性化税费计算逻辑。
    """

    def __init__(self, commission_rate, min_commission):
        self._commission_rate = commission_rate
        self._min_commission = min_commission

    def _get_commission(self, price, quantity):
        commission = price * quantity * self._commission_rate
        return max(commission, self._min_commission)

    def get_trade_tax(self, trade):
        return 0

    def get_trade_commission(self, trade):
        if trade.side == SIDE.CONVERT_STOCK:
            return 0
        return self._get_commission(trade.last_price, trade.last_quantity)

    def get_order_transaction_cost(self, order):
        if order.side == SIDE.CONVERT_STOCK:
            return 0
        return self._get_commission(order.frozen_price, order.quantity)
