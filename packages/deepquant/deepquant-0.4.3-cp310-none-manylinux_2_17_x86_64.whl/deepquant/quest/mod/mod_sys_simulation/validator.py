from typing import Optional

from deepquant.quest.model.order import ALGO_ORDER_STYLES, Order
from deepquant.quest.interface import AbstractFrontendValidator
from deepquant.quest.portfolio.account import Account


class OrderStyleValidator(AbstractFrontendValidator):

    def __init__(self, frequency):
        self._frequency = frequency

    def validate_submission(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        if isinstance(order.style, ALGO_ORDER_STYLES) and self._frequency in ["1m", "tick"]:
            raise RuntimeError("algo order no support 1m and tick frequency")
        return None
    
    def validate_cancellation(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        return None
    
