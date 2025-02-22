from typing import Iterable
from deepquant.quest.utils.i18n import gettext as _
from deepquant.quest.environment import Environment
from deepquant.quest.model.order import Order
from deepquant.quest.model.trade import Trade
from deepquant.quest.const import POSITION_EFFECT, INSTRUMENT_TYPE, POSITION_DIRECTION, SIDE
from deepquant.quest.core.events import EVENT, Event
from deepquant.quest.portfolio import Account

from deepquant.quest.mod.mod_sys_simulation.matcher import DefaultBarMatcher, DefaultTickMatcher, CounterPartyOfferMatcher

from .data import Instrument, OPTION_TYPE


def get_underlying_price(env, instrument):
    underlying = instrument.underlying_instrument
    if underlying.type == INSTRUMENT_TYPE.FUTURE:
        return env.data_proxy.get_settlement(underlying, env.trading_dt)
    else:
        return env.data_proxy.get_last_price(underlying.market_code)


def calc_strike_price_spread(env, instrument, slippage=0):
    # type: (Environment, Instrument, float) -> float
    # 计算行权价和标的价格之差
    underlying = instrument.underlying_instrument
    if underlying.type == INSTRUMENT_TYPE.FUTURE:
        underlying_price = env.data_proxy.get_settlement(underlying, env.trading_dt)
    else:
        underlying_price = env.data_proxy.get_last_price(underlying.market_code)
    return (underlying_price - instrument.strike_price) * (
        1 if instrument.option_type == OPTION_TYPE.CALL else -1
    ) - underlying_price * slippage


def _match_exercise(env, account, order):
    # type: (Environment, Account, Order) -> Iterable[Trade]
    instrument = env.data_proxy.instruments(order.market_code)  # type: Instrument

    if order.side == SIDE.SELL:
        exercise_position = account.get_position(order.market_code, POSITION_DIRECTION.LONG)
        match_position = account.get_position(order.market_code, POSITION_DIRECTION.SHORT)
    else:
        exercise_position = account.get_position(order.market_code, POSITION_DIRECTION.SHORT)
        match_position = account.get_position(order.market_code, POSITION_DIRECTION.LONG)

    matched_quantity = min(exercise_position.closable, match_position.closable)
    exercised_quantity = min(order.quantity, exercise_position.closable - matched_quantity)
    if matched_quantity:
        yield Trade.__from_create__(
            order.order_id, None, matched_quantity, order.side, POSITION_EFFECT.MATCH, order.market_code
        )

    if exercised_quantity > 0:
        underlying_price = get_underlying_price(env, instrument)
        price = (underlying_price - instrument.strike_price) * (
            1 if instrument.option_type == OPTION_TYPE.CALL else -1
        )
        exercise_trade = Trade.__from_create__(
            order.order_id, price, exercised_quantity, order.side, POSITION_EFFECT.EXERCISE, order.market_code
        )
        exercise_trade._commission = env.get_trade_commission(exercise_trade)
        exercise_trade._tax = env.get_trade_tax(exercise_trade)
        yield exercise_trade


def _publish_trade_event(env, account, order):
    # type: (Environment, Account, Order) -> None
    for trade in _match_exercise(env, account, order):
        if trade.position_effect == POSITION_EFFECT.EXERCISE:
            order.fill(trade)
        env.event_bus.publish_event(Event(EVENT.TRADE, account=account, trade=trade, order=order))
    if order.unfilled_quantity != 0:
        order.mark_cancelled(_(
            u"exercisable quantity {exercisable_quantity} of {market_code} is less than "
            u"order quantity {order_quantity}"
        ).format(
            exercisable_quantity=order.filled_quantity, market_code=order.market_code,
            order_quantity=order.quantity
        ))


class OptionBarMatcher(DefaultBarMatcher):
    def match(self, account, order, open_auction):
        if order.position_effect != POSITION_EFFECT.EXERCISE:
            return super(OptionBarMatcher, self).match(account, order, open_auction)
        _publish_trade_event(self._env, account, order)


class OptionTickMatcher(DefaultTickMatcher):
    def match(self, account, order, open_auction):
        if order.position_effect != POSITION_EFFECT.EXERCISE:
            return super(OptionTickMatcher, self).match(account, order, open_auction)
        _publish_trade_event(self._env, account, order)


class OptionCounterPartyMatcher(CounterPartyOfferMatcher):
    def match(self, account, order, open_auction):
        # type: (Account, Order, bool) -> None
        if order.position_effect != POSITION_EFFECT.EXERCISE:
            return super(OptionCounterPartyMatcher, self).match(account, order, open_auction)
        _publish_trade_event(self._env, account, order)
