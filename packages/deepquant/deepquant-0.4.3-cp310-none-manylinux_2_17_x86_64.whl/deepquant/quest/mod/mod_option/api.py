from deepquant.quest.api import register_api
from deepquant.quest.environment import Environment
from deepquant.quest.const import INSTRUMENT_TYPE, SIDE, POSITION_EFFECT
from deepquant.quest.apis.api_abstract import order, order_to, buy_open, buy_close, sell_open, sell_close, exercise
from deepquant.quest.apis.api_base import assure_market_code
from deepquant.quest.utils.exception import RQInvalidArgument
from deepquant.quest.model.order import Order

from deepquant.quest.mod.mod_sys_accounts.api.api_future import (
    future_order, future_order_to, future_buy_open, future_buy_close, future_sell_open, future_sell_close
)

from .data import OPTION_TYPE, EXERCISE_TYPE

order.register(INSTRUMENT_TYPE.OPTION)(future_order)
order_to.register(INSTRUMENT_TYPE.OPTION)(future_order_to)
buy_open.register(INSTRUMENT_TYPE.OPTION)(future_buy_open)
buy_close.register(INSTRUMENT_TYPE.OPTION)(future_buy_close)
sell_open.register(INSTRUMENT_TYPE.OPTION)(future_sell_open)
sell_close.register(INSTRUMENT_TYPE.OPTION)(future_sell_close)

register_api("EXERCISE_TYPE", EXERCISE_TYPE)
register_api("OPTION_TYPE", OPTION_TYPE)


@exercise.register(INSTRUMENT_TYPE.OPTION)
def option_exercise(id_or_ins, amount, convert=False):
    if convert:
        raise RQInvalidArgument("期权行权 convert 参数不能为 True")
    amount = int(amount)
    market_code = assure_market_code(id_or_ins)
    order = Order.__from_create__(market_code, amount, SIDE.SELL, None, POSITION_EFFECT.EXERCISE)
    env = Environment.get_instance()
    if env.can_submit_order(order):
        env.broker.submit_order(order)
        return order
