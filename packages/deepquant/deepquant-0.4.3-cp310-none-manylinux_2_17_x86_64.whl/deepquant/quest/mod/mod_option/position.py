from functools import lru_cache
from datetime import date

from deepquant.quest.environment import Environment
from deepquant.quest.model.trade import Trade
from deepquant.quest.model.order import Order
from deepquant.quest.core.events import EVENT, Event
from deepquant.quest.const import POSITION_DIRECTION, POSITION_EFFECT, SIDE, INSTRUMENT_TYPE
from deepquant.quest.portfolio.position import Position
from deepquant.quest.mod.mod_sys_accounts.position_model import FuturePositionProxy
from deepquant.quest.utils.logger import user_system_log
from deepquant.quest.utils import is_valid_price
from deepquant.quest.utils.i18n import gettext as _

from .data import calc_margin, Instrument, OPTION_TYPE, EXERCISE_TYPE

LONG = POSITION_DIRECTION.LONG
SHORT = POSITION_DIRECTION.SHORT


class OptionPositionProxy(FuturePositionProxy):
    __instrument_types__ = (INSTRUMENT_TYPE.OPTION, )

    type = property(lambda self: INSTRUMENT_TYPE.OPTION)


class OptionPosition(Position):
    exercise_slippage = 0.

    __instrument_types__ = (INSTRUMENT_TYPE.OPTION, )

    __repr_properties__ = (
        "market_code", "direction", "old_quantity", "quantity", "margin", "market_value", "trading_pnl",
        "position_pnl"
    )

    def __init__(self, market_code, direction, init_quantity=0, init_price=None):
        super(OptionPosition, self).__init__(market_code, direction, init_quantity, init_price)
        self._instrument = self._env.data_proxy.instruments(market_code)  # type: Instrument
        self._underlying_price = float("NaN")
        self._underlying_prev_close = float("NaN")
        self._prev_settlement = float("NaN")

    old_quantity = property(lambda self: self._old_quantity)
    today_quantity = property(lambda self: self._quantity - self._old_quantity)
    market_value = property(lambda self: self.last_price * self.quantity * self.contract_multiplier)

    @property
    def underlying_prev_close(self):
        if not is_valid_price(self._underlying_prev_close):
            self._underlying_prev_close = self._env.data_proxy.get_prev_close(
                self._instrument.underlying_market_code, self._env.trading_dt
            )
            if not is_valid_price(self._underlying_prev_close):
                raise RuntimeError(_("invalid price of {market_code}: {price}").format(
                    market_code=self._instrument.underlying_market_code, price=self._underlying_prev_close
                ))
        return self._underlying_prev_close

    @property
    def prev_settlement(self):
        if not is_valid_price(self._prev_settlement):
            self._prev_settlement = self._env.data_proxy.get_prev_settlement(self.market_code, self._env.trading_dt)
            if not is_valid_price(self._prev_settlement):
                raise RuntimeError(_("invalid price of {market_code}: {price}").format(
                    market_code=self._instrument.market_code, price=self._prev_settlement
                ))
        return self._prev_settlement

    @property
    def margin(self):
        if self._direction == POSITION_DIRECTION.LONG:
            return 0
        return calc_margin(
            self._instrument, self.quantity, self.underlying_price, self.underlying_prev_close, self.prev_settlement
        )

    @property
    def equity(self):
        # type: () -> float
        if self._direction == POSITION_DIRECTION.LONG:
            return self.last_price * self.quantity * self.contract_multiplier
        else:
            return -1 * (self.last_price * self.quantity * self.contract_multiplier)

    @property
    def underlying_price(self):
        if self._underlying_price != self._underlying_price:
            if self._instrument.underlying_instrument.type == INSTRUMENT_TYPE.FUTURE:
                self._underlying_price = self._env.data_proxy.get_prev_settlement(self._instrument.underlying_market_code, self._env.trading_dt)
            else:    
                self._underlying_price = self._env.data_proxy.get_last_price(self._instrument.underlying_market_code)
            if self._underlying_price != self._underlying_price:
                raise RuntimeError(
                    _("last price of position {} is not supposed to be nan").format(self._market_code))
        return self._underlying_price

    def update_last_price(self, price):
        self._last_price = price

    def update_underlying_price(self):
        if self._instrument.underlying_instrument.type == INSTRUMENT_TYPE.FUTURE:
            underlying_price = self._env.data_proxy.get_settlement(
                self._instrument.underlying_instrument, self._env.trading_dt
            )
        else:
            underlying_price = self._env.data_proxy.get_last_price(self._instrument.underlying_market_code)
        if underlying_price == underlying_price:
            self._underlying_price = underlying_price

    @property
    @lru_cache()
    def contract_multiplier(self):
        return self._instrument.contract_multiplier

    @property
    def trading_pnl(self):
        trade_quantity = self._quantity - self._logical_old_quantity
        return self.contract_multiplier * (trade_quantity * self.last_price - self._trade_cost) * self._direction_factor

    @property
    def position_pnl(self):
        quantity = self._logical_old_quantity
        if quantity == 0:
            return 0
        return quantity * self.contract_multiplier * (self.last_price - self.prev_close) * self._direction_factor

    @property
    def pnl(self):
        # type: () -> float
        return super(OptionPosition, self).pnl * self.contract_multiplier

    @property
    def _premium(self):
        return self._avg_price * self.quantity

    def calc_close_today_amount(self, trade_amount, position_effect):
        if position_effect == POSITION_EFFECT.CLOSE_TODAY:
            return trade_amount if trade_amount <= self.today_quantity else self.today_quantity
        else:
            return max(trade_amount - self._old_quantity, 0)

    def apply_trade(self, trade):
        # type: (Trade) -> float
        if trade.position_effect == POSITION_EFFECT.OPEN:
            return self._apply_open_trade(trade)
        elif trade.position_effect in {POSITION_EFFECT.CLOSE, POSITION_EFFECT.CLOSE_TODAY}:
            return self._apply_close_trade(trade)
        elif trade.position_effect == POSITION_EFFECT.MATCH:
            return self._apply_match_trade(trade)
        elif trade.position_effect == POSITION_EFFECT.EXERCISE:
            return self._apply_exercise_trade(trade)
        else:
            raise RuntimeError("OptionPosition dose not support position_effect: {}".format(trade.position_effect))

    def _apply_open_trade(self, trade):
        # type: (Trade) -> float
        self._transaction_cost += trade.transaction_cost
        if self.quantity < 0:
            if trade.last_quantity <= -1 * self.quantity:
                self._avg_price = 0
            else:
                self._avg_price = trade.last_price
        else:
            self._avg_price = (self.quantity * self._avg_price + trade.last_quantity * trade.last_price) / (
                    self.quantity + trade.last_quantity
            )
        self._quantity += trade.last_quantity
        self._trade_cost += trade.last_price * trade.last_quantity

        if self._direction == LONG:
            # 权力方开仓，付出权利金
            return -1 * (trade.last_quantity * trade.last_price * self.contract_multiplier + trade.transaction_cost)
        else:
            # 义务方开仓，收到权利金
            return trade.last_quantity * trade.last_price * self.contract_multiplier - trade.transaction_cost

    def _apply_close_trade(self, trade):
        self._transaction_cost += trade.transaction_cost
        if trade.position_effect == POSITION_EFFECT.CLOSE_TODAY:
            self._quantity -= trade.last_quantity
        else:
            # 先平昨，后平今
            self._old_quantity -= min(trade.last_quantity, self._old_quantity)
            self._quantity -= trade.last_quantity
        self._trade_cost -= trade.last_price * trade.last_quantity
        if self._direction == LONG:
            # 权力方平仓，收回权利金
            return trade.last_quantity * trade.last_price * self.contract_multiplier - trade.transaction_cost
        else:
            # 义务方平仓，返还权利金
            return -1 * (trade.last_quantity * trade.last_price * self.contract_multiplier + trade.transaction_cost)

    def _apply_match_trade(self, trade):
        self._transaction_cost += trade.transaction_cost
        self._old_quantity -= min(trade.last_quantity, self._old_quantity)
        self._quantity -= trade.last_quantity
        self._trade_cost -= self.last_price * trade.last_quantity
        return -1 * trade.transaction_cost

    def _apply_exercise_trade(self, trade):
        self._transaction_cost += trade.transaction_cost
        self._old_quantity -= min(trade.last_quantity, self._old_quantity)
        self._quantity -= trade.last_quantity
        self._trade_cost -= trade.last_price * trade.last_quantity
        if self._direction == LONG:
            # trade.price: underlying_price - strike_price if call else strike_price - underlying_price
            return trade.last_price * trade.last_quantity * self.contract_multiplier - trade.transaction_cost
        else:
            return -1 * (trade.last_quantity * trade.last_price * self.contract_multiplier + trade.transaction_cost)

    def settlement(self, trading_date):
        # type: (date) -> float
        super(OptionPosition, self).settlement(trading_date)
        self.update_underlying_price()
        if self.quantity == 0:
            return 0
        next_date = self._env.data_proxy.get_next_trading_date(trading_date)
        delta_cash = 0
        if self._instrument.de_listed_at(next_date):
            # 先尝试轧平
            matched_quantity = min(self.quantity, self._opposite.quantity)
            if matched_quantity:
                match_trade = Trade.__from_create__(
                    None, None, matched_quantity, None, POSITION_EFFECT.MATCH, self._market_code
                )
                self.apply_trade(match_trade)
                self._opposite.apply_trade(match_trade)
                if self.quantity == 0:
                    return delta_cash
            # 自动行权，exercise_slippage 仅影响行权的判断，不影响行权的损益
            strike_price_spread = (self.underlying_price - self._instrument.strike_price) * (
                1 if self._instrument.option_type == OPTION_TYPE.CALL else -1
            )
            if strike_price_spread - self.underlying_price * self.exercise_slippage > 0:
                # 行权
                matched_quantity = self._opposite.quantity
                if matched_quantity:
                    self._opposite.apply_trade(Trade.__from_create__(
                        None, None, matched_quantity, SIDE.BUY if self._direction == LONG else SIDE.SELL,
                        POSITION_EFFECT.MATCH, self._market_code
                    ))
                exercised_quantity = self.quantity - matched_quantity
                if exercised_quantity:
                    self._automatic_exercise(exercised_quantity, strike_price_spread)
            else:
                user_system_log.info("期权 {} 到期，行权价{}合约标的 {} 当前价格，不进行自动行权，将从持仓中移除".format(
                    self._market_code, "大于" if self._direction == LONG else "小于", self._instrument.underlying_market_code
                ))
            self._quantity = self._old_quantity = 0
        return delta_cash


    def _automatic_exercise(self, exercised_quantity, strike_price_spread):
        user_system_log.info("期权 {} 到期，自动行权{}方向 {} 手".format(
            self._market_code, "多" if self._direction == LONG else "空", exercised_quantity
        ))
        account = self._env.get_account(self._market_code)
        side = SIDE.SELL if self._direction == LONG else SIDE.BUY
        exercise_trade = Trade.__from_create__(
            None, strike_price_spread, exercised_quantity, side, POSITION_EFFECT.EXERCISE, self._market_code
        )
        # 美式期权行权时需要支付手续费
        if self._instrument.exercise_type == EXERCISE_TYPE.AMERICAN:
            exercise_trade._commission = self._env.get_trade_commission(exercise_trade)
        self._env.event_bus.publish_event(Event(EVENT.TRADE, account=account, trade=exercise_trade, order=None))


    @property
    def _opposite(self):
        # type: () -> OptionPosition
        if self._direction == LONG:
            opposite_pos = self._env.portfolio.get_position(self._market_code, SHORT)
        else:
            opposite_pos = self._env.portfolio.get_position(self._market_code, LONG)
        if not isinstance(opposite_pos, self.__class__):
            raise RuntimeError("opposite position of {}({}) has wrong type {}".format(
                self.__class__, self.market_code, type(opposite_pos)
            ))
        return opposite_pos

    def before_trading(self, trading_date):
        # type: (date) -> float
        delta = super().before_trading(trading_date)
        self._underlying_prev_close = None
        self._prev_settlement = None
        return delta
