from typing import Optional

from deepquant.quest.interface import AbstractFrontendValidator
from deepquant.quest.utils.logger import user_system_log
from deepquant.quest.model.order import Order
from deepquant.quest.portfolio.account import Account


class MarginInstrumentValidator(AbstractFrontendValidator):
    """ 融资下单品种限制: 当开启股票池限制且有融资余额时只能交易股票和ETF """

    def validate_submission(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        if account.cash_liabilities > 0:
            reason = "Order Creation Failed: cash liabilities > 0, {} not support submit order".format(order.market_code)
            return reason
        else:
            return None
    
    def validate_cancellation(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        return None