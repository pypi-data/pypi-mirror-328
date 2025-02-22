# -*- coding: utf-8 -*-\
from datetime import date
from typing import Optional

import numpy as np
import pandas as pd

import deepquant.quest.datac

from deepquant.quest.model.trade import Trade
from deepquant.quest.utils import lru_cache
from deepquant.quest.utils.logger import user_system_log
from deepquant.quest.const import INSTRUMENT_TYPE, POSITION_EFFECT, SIDE, TRADING_CALENDAR_TYPE
from deepquant.quest.portfolio.position import Position
from deepquant.quest.environment import Environment

from deepquant.quest.mod.mod_sys_accounts.position_model import StockPositionProxy

from .data import Instrument, get_conversion_price


REAL_CASH_FLOW_DTYPES = [("record_date", "u4"), ("payment_date", "u4"), ("interest_payment", "f8"), ("principal", "f8")]


@lru_cache(2048)
def date_to_int8(dt):
    return dt.year * 10000 + dt.month * 100 + dt.day


@lru_cache(1024)
def _all_real_cash_flow(market_code):
    # type: (str) -> Optional[np.rec.array]
    df = deepquant.quest.datac.convertible.get_cash_flow(market_code)
    if df is None or len(df) == 0:
        return
    trading_dates = Environment.get_instance().data_source.get_trading_calendars()[TRADING_CALENDAR_TYPE.EXCHANGE]
    trading_dates_df = pd.DataFrame({"trading_date": trading_dates})
    df = df.loc[market_code].reset_index()
    # 有些付息日在周末，延迟到下个交易日
    df = pd.merge_asof(df, trading_dates_df, left_on="payment_date", right_on="trading_date", direction="forward")
    # 交易日历不够长，最新的债会存在一些空的
    df.dropna(subset=["trading_date"], inplace=True)
    ret = np.empty(shape=len(df), dtype=REAL_CASH_FLOW_DTYPES)
    ret["record_date"] = [date_to_int8(d) for d in df["record_date"]]
    ret["payment_date"] = [date_to_int8(d) for d in df["trading_date"]]
    ret["interest_payment"] = df["interest_payment"].fillna(0.0).values
    ret["principal"] = df["principal_payment"].fillna(0.0).values
    ret.sort(order="record_date")
    return ret


class ConvertiblePositionProxy(StockPositionProxy):
    __instrument_types__ = (INSTRUMENT_TYPE.CONVERTIBLE, )

    type = property(lambda self: INSTRUMENT_TYPE.CONVERTIBLE)


class ConvertiblePosition(Position):
    __instrument_types__ = (INSTRUMENT_TYPE.CONVERTIBLE, )

    def __init__(self, market_code, direction, init_quantity=0, init_price=None):
        super(ConvertiblePosition, self).__init__(market_code, direction, init_quantity, init_price)
        self._instrument = self._env.data_proxy.instruments(market_code)  # type: Instrument
        self._payment_receivable = None

    def set_state(self, state):
        super(ConvertiblePosition, self).set_state(state)
        self._payment_receivable = state.get("payment_receivable")

    def get_state(self):
        state = super(ConvertiblePosition, self).get_state()
        state.update({
            "payment_receivable": self._payment_receivable,
        })
        return state

    def before_trading(self, trading_date):
        # type: (date) -> float
        delta_cash = super().before_trading(trading_date)
        # 处理赎回、付息
        if self._payment_receivable and date_to_int8(trading_date) == self._payment_receivable[0]:
            interest_payment = self._payment_receivable[1]
            quantity = self._payment_receivable[2]
            cash = interest_payment * quantity
            user_system_log.debug("债券{}付息，每股{}元，共计{}元".format(self.market_code, interest_payment, cash))
            delta_cash += cash
        return delta_cash

    def apply_trade(self, trade):
        # type: (Trade) -> float
        if trade.position_effect != POSITION_EFFECT.EXERCISE:
            return super(ConvertiblePosition, self).apply_trade(trade)

        self._old_quantity -= min(trade.last_quantity, self._old_quantity)
        self._quantity -= trade.last_quantity
        self._trade_cost -= trade.last_price * trade.last_quantity

        if trade.side == SIDE.CONVERT_STOCK:
            stock_code = self._instrument.stock_code
            conversion_price = get_conversion_price(self._market_code, self._env.calendar_dt.date())
            conversion_amount = int(100 * trade.last_quantity / conversion_price)
            if conversion_amount >= 1:
                self._env.portfolio.get_account(stock_code).apply_trade(Trade.__from_create__(
                    order_id=None,
                    price=conversion_price,
                    amount=conversion_amount,
                    side=SIDE.BUY,
                    position_effect=POSITION_EFFECT.OPEN,
                    market_code=stock_code
                ))
            return 100 * trade.last_quantity
        else:
            return trade.last_price * trade.last_quantity - trade.transaction_cost

    def settlement(self, trading_date):
        # type: (date) -> float
        delta_cash = super(ConvertiblePosition, self).settlement(trading_date)
        if self.quantity == 0:
            return delta_cash
        if self._payment_receivable and self._payment_receivable[3]:
            # 到期返回面纸
            delta_cash += 100 * self.quantity
            self._payment_receivable = None
            self._logical_old_quantity = self._old_quantity = self._quantity = 0
            user_system_log.info("债券{}触发赎回，清空仓位.".format(self._market_code))
            return delta_cash
        is_call, interest_payment, payment_date = self._get_payment(trading_date)
        if interest_payment == 0:
            return delta_cash
        # 按照登记日的持仓数量
        self._payment_receivable = (payment_date, interest_payment, self.quantity, is_call)
        return delta_cash

    def _get_payment(self, trading_date):
        # type: (date) -> (bool, float, int)
        """ 当日的 real interest payment 返回的 payment

        :param trading_date: datetime.datetime
        :return: (call, interest_payment, payment_date)
        :rtype: (bool, float, int)
        """
        all_cash_flow = _all_real_cash_flow(self._market_code)
        if all_cash_flow is None:
            return False, 0.0, -1
        trading_date = date_to_int8(trading_date)
        pos = all_cash_flow["record_date"].searchsorted(trading_date)
        if pos >= len(all_cash_flow) or all_cash_flow["record_date"][pos] != trading_date:
            return False, 0.0, -1
        interest_payment = all_cash_flow[pos]["interest_payment"]
        is_call = all_cash_flow[pos]["principal"] > 0 and pos == len(all_cash_flow) - 1
        return is_call, interest_payment, all_cash_flow[pos]["payment_date"]
