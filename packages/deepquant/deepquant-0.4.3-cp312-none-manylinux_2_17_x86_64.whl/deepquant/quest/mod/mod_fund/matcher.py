import numpy

from deepquant.quest.const import SIDE
from deepquant.quest.model.trade import Trade
from deepquant.quest.utils.logger import user_system_log
from deepquant.quest.portfolio.account import Account
from deepquant.quest.environment import Environment
from deepquant.quest.model.order import Order
from deepquant.quest.core.events import Event, EVENT

from deepquant.quest.mod.yhalpha_mod_sys_simulation.matcher import AbstractMatcher


class FundMatcher(AbstractMatcher):
    def __init__(self, env, subscription_limit):
        self._env = env  # type: Environment
        self._subscription_limit = subscription_limit  # type: bool

    def match(self, account, order, open_auction):
        # type: (Account, Order, bool) -> None
        fill = order.unfilled_quantity
        bar = self._env.get_bar(order.market_code)
        if self._subscription_limit:
            total_cost = round(bar.last * order.unfilled_quantity + 0.00005, 4)
            if order.side == SIDE.BUY:
                if not numpy.isnan(bar.subscribe_upper_limit) and bar.subscribe_upper_limit < total_cost:
                    round_lot = self._env.data_proxy.instruments(order.market_code).round_lot
                    fill = int(bar.subscribe_upper_limit / bar.last / round_lot) * round_lot
                    user_system_log.warn("申购金额 {} 超过上限 {}，实际成交数量：{}".format(
                        total_cost, bar.subscribe_upper_limit, fill
                    ))
                elif not numpy.isnan(bar.subscribe_lower_limit) and bar.subscribe_lower_limit > total_cost:
                        order.mark_rejected("申购失败：申购金额{}低于申购下限{}".format(total_cost, bar.subscribe_lower_limit))
                        return

        trade = Trade.__from_create__(
            order_id=order.order_id,
            price=bar.last,
            amount=fill,
            side=order.side,
            position_effect=order.position_effect,
            frozen_price=order.frozen_price,
            market_code=order.market_code
        )
        trade._commission = fill / order.quantity * order.fee
        order.fill(trade)
        self._env.event_bus.publish_event(Event(EVENT.TRADE, account=account, trade=trade, order=order))
        if order.unfilled_quantity != 0:
            order.mark_cancelled(None, user_warn=False)

    def update(self, event):
        pass

