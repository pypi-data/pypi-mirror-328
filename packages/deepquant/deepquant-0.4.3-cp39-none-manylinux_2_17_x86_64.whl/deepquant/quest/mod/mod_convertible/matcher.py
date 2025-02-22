from deepquant.quest.const import POSITION_EFFECT, SIDE
from deepquant.quest.portfolio.account import Account
from deepquant.quest.model.order import Order
from deepquant.quest.model.trade import Trade
from deepquant.quest.interface import AbstractPosition
from deepquant.quest.core.events import EVENT, Event
from deepquant.quest.mod.mod_sys_simulation.matcher import DefaultBarMatcher, DefaultTickMatcher, CounterPartyOfferMatcher


def exercise(account, order, env):
    position = account.get_position(order.market_code, order.position_direction)  # type: AbstractPosition
    if position.closable == 0:
        order.mark_cancelled("订单已撤销：{} 没有可行权仓位".format(order.market_code))
        return

    trade = Trade.__from_create__(
        order.order_id, order.frozen_price, min(position.closable, order.quantity), order.side,
        order.position_effect, order.market_code,
    )

    # 目前并未在交易所税费条款中找到有关说明，鉴于转股并不是经常发生，这里将暂时不考虑转股费用，应对回测结果无重大影响。
    if order.side != SIDE.CONVERT_STOCK:
        trade._commission = env.get_trade_commission(trade)
        trade._tax = env.get_trade_tax(trade)
    order.fill(trade)
    env.event_bus.publish_event(Event(EVENT.TRADE, account=account, trade=trade, order=order))

    if order.unfilled_quantity != 0:
        order.mark_cancelled(
            "{} 的可行权仓位 {} 低于目标行权仓位 {}".format(order.market_code, position.closable, order.quantity)
        )


class ConvertibleBarMatcher(DefaultBarMatcher):
    def __init__(self, env, mod_config):
        super(ConvertibleBarMatcher, self).__init__(env, mod_config)
        self._price_limit = False

    def match(self, account, order, open_auction):
        # type: (Account, Order, bool) -> None
        if order.position_effect != POSITION_EFFECT.EXERCISE:
            return super(ConvertibleBarMatcher, self).match(account, order, open_auction)

        exercise(account, order, self._env)


class ConvertibleTickMatcher(DefaultTickMatcher):
    def __init__(self, env, mod_config):
        super(ConvertibleTickMatcher, self).__init__(env, mod_config)
        self._price_limit = False

    def match(self, account, order, open_auction):
        # type: (Account, Order, bool) -> None
        if order.position_effect != POSITION_EFFECT.EXERCISE:
            return super(ConvertibleTickMatcher, self).match(account, order, open_auction)

        exercise(account, order, self._env)


class ConvertibleCounterPartyMatcher(CounterPartyOfferMatcher):
    def match(self, account, order, open_auction):
        # type: (Account, Order, bool) -> None
        if order.position_effect != POSITION_EFFECT.EXERCISE:
            return super(ConvertibleCounterPartyMatcher, self).match(account, order, open_auction)

        exercise(account, order, self._env)
