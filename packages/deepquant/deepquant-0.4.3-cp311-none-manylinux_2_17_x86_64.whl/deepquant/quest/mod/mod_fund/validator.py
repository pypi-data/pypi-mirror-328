from typing import Optional

from deepquant.quest.const import SIDE
from deepquant.quest.environment import Environment
from deepquant.quest.interface import AbstractFrontendValidator
from deepquant.quest.model.order import Order
from deepquant.quest.portfolio.account import Account

from .const import FUND_STATUS


class FundStatusValidator(AbstractFrontendValidator):
    def __init__(self, env):
        self._env = env  # type: Environment
    
    def validate_submission(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        current_bar = self._env.get_bar(order.market_code)
        if order.side == SIDE.BUY:
            state = current_bar.subscribe_status
            state_name = "申购"
        elif order.side == SIDE.SELL:
            state = current_bar.redeem_status
            state_name = "赎回"
        else:
            raise ValueError("error SIDE = {}".format(order.side))

        if FUND_STATUS.invalid_state(state):
            reason = u"{}申赎失败,当前时间({}) {}状态={} ".format(
                order.market_code, self._env.trading_dt, state_name, state
            )
            return reason
        return None
    
    def validate_cancellation(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        return None
