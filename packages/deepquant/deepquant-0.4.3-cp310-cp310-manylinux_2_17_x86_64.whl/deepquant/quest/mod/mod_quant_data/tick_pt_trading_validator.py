import datetime
from typing import Optional

from deepquant.quest.interface import AbstractFrontendValidator
from deepquant.quest.model.order import Order
from deepquant.quest.portfolio.account import Account

from deepquant.quest.utils.i18n import gettext as _


class TickPTIsTradingValidator(AbstractFrontendValidator):
    def __init__(self, env):
        self._env = env

    def validate_submission(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        market_code = order.market_code
        instrument = self._env.data_proxy.instruments(order.market_code)
        if instrument.type == 'stock':
            dt = self._env.calendar_dt
            if market_code.endswith(".SE") or market_code.endswith(".SH"):
                t = dt.time()
                fail_cond = not (datetime.time(9, 30) <= t < datetime.time(11, 30)
                                 or datetime.time(13, 0) <= t < datetime.time(15, 0))
                fail_cond = fail_cond or market_code.endswith(".XSHE") and datetime.time(14, 47) <= t <= datetime.time(15, 0)
                if fail_cond:
                    reason = _(u"Not supported trading period for {market_code} on {date}").format(
                        market_code=market_code,
                        date=self._env.trading_dt,
                    )
                    return reason
        return None
    
    def validate_cancellation(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        return None
