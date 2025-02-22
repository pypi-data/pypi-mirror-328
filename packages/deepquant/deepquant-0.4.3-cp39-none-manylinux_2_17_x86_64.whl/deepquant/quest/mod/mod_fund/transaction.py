# -*- coding: utf-8 -*-
from deepquant.quest.interface import AbstractTransactionCostDecider


class FundTransactionDecider(AbstractTransactionCostDecider):
    @classmethod
    def calc_commission(cls, amount):
        return amount * cls.fee_ratio

    def get_trade_commission(self, trade):
        raise NotImplementedError

    def get_order_transaction_cost(self, order):
        return order.fee

    def get_trade_tax(self, trade):
        raise NotImplementedError
