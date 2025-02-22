from typing import Optional

from deepquant.quest.model.order import Order
from deepquant.quest.environment import Environment
from deepquant.quest.interface import AbstractFrontendValidator
from deepquant.quest.const import POSITION_EFFECT, INSTRUMENT_TYPE, SIDE
from deepquant.quest.portfolio.account import Account

from .data import Instrument, EXERCISE_TYPE


class OptionValidator(AbstractFrontendValidator):
    def __init__(self, env):
        self._env = env  # type: Environment

    def _validate_exercise_order(self, instrument: Instrument, order: Order) -> Optional[str]:
        if order.side == SIDE.BUY:
            reason = "行权失败，卖方（义务方）仓位不可主动触发行权"
            return reason
        if instrument.exercise_type == EXERCISE_TYPE.EUROPEAN and self._env.trading_dt.date() != instrument.maturity_date.date():
            reason = "行权失败，欧式期权 {} 仅可在到期日 {} 行权".format(instrument.market_code, instrument.maturity_date.date())
            return reason
        return None
    
    def validate_submission(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        ins = self._env.data_proxy.instruments(order.market_code)
        if ins.type != INSTRUMENT_TYPE.OPTION:
            return None
        if order.position_effect == POSITION_EFFECT.EXERCISE:
            return self._validate_exercise_order(ins, order)
        return None
    
    def validate_cancellation(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        return None
