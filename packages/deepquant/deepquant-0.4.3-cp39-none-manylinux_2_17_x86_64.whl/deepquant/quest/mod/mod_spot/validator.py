from typing import Optional
from collections import ChainMap

from deepquant.quest.utils.logger import system_log
from deepquant.quest.model.order import Order
from deepquant.quest.portfolio import Account
from deepquant.quest.interface import AbstractFrontendValidator

ORDER_MAX_QUANTITY_REVERSE_MAP = {
    200: ("IAU995.SGEX", "AU995.SGEX", "AUTD.SGEX"),
    500: ("AU9995.SGEX", ),
    1000: ("PT9995.SGEX", "IAU100G.SGEX", "AU100G.SGEX", "PGC30G.SGEX", "AU50G.SGEX", "AG9999.SGEX", "AG999.SGEX"),
    2000: ("AUTN1.SGEX", "AUTN2.SGEX", "MAUTD.SGEX"),
    10000: ("AGTD.SGEX", ),
    50000: ("IAU9999.SGEX", "AU9999.SGEX")
}

ORDER_MAX_QUANTITY_MAP = ChainMap(*({obid: q for obid in obids} for q, obids in ORDER_MAX_QUANTITY_REVERSE_MAP.items()))


class SpotFrontendValidator(AbstractFrontendValidator):
    def validate_submission(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        try:
            max_quantity = ORDER_MAX_QUANTITY_MAP[order.market_code]
        except KeyError:
            system_log.warning("no max quantity data, market_code: {}".format(order.market_code))
        else:
            if order.quantity > max_quantity:
                reason = "订单创建失败，下单量 {} 超过单笔最大下单数 {}".format(order.quantity, max_quantity)
                return reason
        return None
    
    def validate_cancellation(self, order: Order, account: Optional[Account] = None) -> Optional[str]:
        return None