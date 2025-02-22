from functools import lru_cache
from typing import Dict

import deepquant.quest.datac
from deepquant.quest.interface import AbstractTransactionCostDecider
from deepquant.quest.const import INSTRUMENT_TYPE, POSITION_EFFECT, SIDE
from deepquant.quest.environment import Environment

from .data import Instrument


class CommissionRate:  # commission rate
    def __init__(self, open, close, exercise, close_today):
        self.open = open
        self.close = close
        self.exercise = exercise
        self.close_today = close_today

    def __repr__(self):
        r = f"开仓手续费{self.open}/手,平仓手续费{self.close}/手,行权手续费{self.exercise}/手"
        if self.close_today != self.close:
            r += f",平今仓手续费{self.close_today}/手"
        return r


CUSTOM_COMMISSION_RATES: Dict[str, CommissionRate] = {}
COMMISSION_RATES: Dict[str, CommissionRate] = {}


class OptionTransactionCostDecider(AbstractTransactionCostDecider):
    def __init__(self, env, commission_multiplier):
        # type: (Environment, float) -> OptionTransactionCostDecider
        self._commission_multiplier = commission_multiplier
        self._env = env

    @lru_cache(2048)
    def _get_commission_rate(self, market_code: str) -> CommissionRate:
        ins = self._env.data_proxy.instruments(market_code)
        if not isinstance(ins, Instrument):
            raise RuntimeError("expect mod_option.Instrument, got {}, type {}".format(ins, type(ins)))
        underlying_symbol = ins.underlying_symbol

        # 如果客户自定义了费率，按客户的
        if underlying_symbol in CUSTOM_COMMISSION_RATES:
            return CUSTOM_COMMISSION_RATES[underlying_symbol]

        if underlying_symbol not in COMMISSION_RATES:
            commission_df = deepquant.quest.datac.options.get_commission(underlying_symbols=underlying_symbol)
            if commission_df is not None:
                row = commission_df.iloc[0]
                rate = CommissionRate(
                    open=row["open_commission"], close=row["close_commission"], exercise=row["strike_commission"],
                    close_today=row["close_commission_today"]
                )
                COMMISSION_RATES[underlying_symbol] = rate

        try:
            return COMMISSION_RATES[underlying_symbol]
        except KeyError:
            raise NotImplementedError("unknown commission rate, market_code={} underlying_symbol={}".format(
                market_code, underlying_symbol
            ))

    def _get_commission(self, market_code, position_effect, quantity, close_today_quantity):
        rate = self._get_commission_rate(market_code)
        if position_effect == POSITION_EFFECT.EXERCISE:
            commission = quantity * rate.exercise
        elif position_effect == POSITION_EFFECT.OPEN:
            commission = quantity * rate.open
        else:
            commission = (quantity - close_today_quantity) * rate.close + close_today_quantity * rate.close_today
        return commission * self._commission_multiplier

    def get_order_transaction_cost(self, order):
        close_today_quantity = order.quantity if order.position_effect == POSITION_EFFECT.CLOSE_TODAY else 0
        return self._get_commission(
            order.market_code, order.position_effect, order.quantity, close_today_quantity
        )

    def get_trade_commission(self, trade):
        if trade.side == SIDE.BUY and trade.position_effect == POSITION_EFFECT.EXERCISE:
            # 义务方行权不手续
            return 0
        return self._get_commission(
            trade.market_code, trade.position_effect, trade.last_quantity, trade.close_today_amount
        )

    def get_trade_tax(self, trade):
        return 0


def add_custom_commission(underlying_symbol, commission):
    CUSTOM_COMMISSION_RATES[underlying_symbol] = CommissionRate(
        open=commission.get("open", 0),
        close=commission.get("close", 0),
        exercise=commission.get("exercise", 0),
        close_today=commission.get("close_today", 0)
    )

