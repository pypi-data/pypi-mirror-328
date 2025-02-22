# -*- coding: utf-8 -*-
from typing import Optional

import pandas as pd

from deepquant.quest.utils.i18n import gettext as _
from deepquant.quest.interface import AbstractFrontendValidator
from deepquant.quest.const import INSTRUMENT_TYPE, POSITION_EFFECT, SIDE
from deepquant.quest.model.order import Order
from deepquant.quest.portfolio.account import Account

from .data import Instrument, get_conversion_price


class ConvertibleValidator(AbstractFrontendValidator):
    def __init__(self, env):
        self._env = env

    def _validate_exercise_order(self, order: Order) -> Optional[str]:
        if order.side == SIDE.CONVERT_STOCK:
            ins = self._env.data_proxy.instruments(order.market_code)  # type: Instrument
            if not (ins.conversion_start_date and ins.conversion_end_date and get_conversion_price(
                    order.market_code, self._env.calendar_dt.date()
            )):
                reason = "转股失败，无法获取 {} 的转股价格".format(order.market_code)
                return reason
            if not ins.conversion_start_date <= self._env.calendar_dt <= ins.conversion_end_date:
                reason = "转股失败，当前日期 {} 不在 {} 的转股期内，转股期为 {} 至 {}".format(
                    self._env.calendar_dt.date(), order.market_code,
                    ins.conversion_start_date.date(), ins.conversion_end_date.date()
                )
                return reason
        return None

    def _validate_open_order(self, order):
        position = self._env.portfolio.get_position(order.market_code, order.position_direction)
        ins = self._env.data_proxy.instruments(order.market_code)  # type: Instrument
        # 债券能够持有的最大数量不得大于 total issue size, 以【持仓数量接近XX债券发行总额上限】原因拒单
        if not pd.isnull(ins.total_issue_size) and ins.issue_price:
            if ins.total_issue_size / ins.issue_price - order.quantity - position.quantity < 0:
                reason = "订单创建失败：持仓数量 {} 接近 {} 债券发行总额上限 {}".format(
                    position.quantity, order.market_code, ins.total_issue_size
                )
                return reason
        return None

    def _validate_close_order(self, order, account):
        # type: (Order, Optional[Account]) -> bool
        if account is None:
            return True
        position = account.get_position(order.market_code, order.position_direction)
        if order.quantity > position.closable:
            reason = "订单创建失败：{market_code} 的仓位不足，目标平仓量为 {quantity}，可平仓量为 {closable}".format(
                market_code=order.market_code, quantity=order.quantity, closable=position.closable
            )
            return reason
        return None

    def validate_submission(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        if self._env.data_proxy.instruments(order.market_code).type != INSTRUMENT_TYPE.CONVERTIBLE:
            return None
        if self._env.data_proxy.is_suspended(order.market_code, self._env.trading_dt):
            reason = _(u"Order Creation Failed: security {market_code} is suspended on {date}").format(
                market_code=order.market_code, date=self._env.trading_dt
            )
            return reason
        if order.position_effect == POSITION_EFFECT.EXERCISE:
            return self._validate_exercise_order(order)
        elif order.position_effect == POSITION_EFFECT.OPEN:
            return self._validate_open_order(order)
        elif order.position_effect == POSITION_EFFECT.CLOSE:
            return self._validate_close_order(order, account)
        
        return None
    
    def validate_cancellation(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        return None