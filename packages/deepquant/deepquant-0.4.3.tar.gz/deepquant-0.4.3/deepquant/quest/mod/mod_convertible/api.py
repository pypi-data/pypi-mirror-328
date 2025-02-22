from functools import lru_cache
from typing import List, Tuple
from datetime import date

import deepquant.quest.datac

from deepquant.quest.environment import Environment
from deepquant.quest.core.events import Event, EVENT
from deepquant.quest.model.order import Order, LimitOrder
from deepquant.quest.const import INSTRUMENT_TYPE, SIDE, POSITION_EFFECT
from deepquant.quest.apis.api_base import assure_market_code
from deepquant.quest.utils.logger import user_system_log
from deepquant.quest.apis.api_abstract import (
    order, order_to, order_shares, order_value, order_target_value, order_percent, order_target_percent, exercise
)

from deepquant.quest.mod.mod_sys_accounts.api.api_stock import (
    stock_order, stock_order_to, stock_order_shares, stock_order_value, stock_order_target_value, stock_order_percent,
    stock_order_target_percent
)


@lru_cache(512)
def get_put_info(market_code):
    # type: (str) -> List[Tuple[date, date, float]]
    df = deepquant.quest.datac.convertible.get_put_info(market_code, "20000104", "29991231")
    if df is None or df.empty:
        return []
    return [(
        t.enrollment_start_date.to_pydatetime().date(), t.enrollment_end_date.to_pydatetime().date(), t.exercise_price
    ) for t in df.itertuples()]


order.register(INSTRUMENT_TYPE.CONVERTIBLE)(stock_order)
order_to.register(INSTRUMENT_TYPE.CONVERTIBLE)(stock_order_to)
order_shares.register(INSTRUMENT_TYPE.CONVERTIBLE)(stock_order_shares)
order_value.register(INSTRUMENT_TYPE.CONVERTIBLE)(stock_order_value)
order_percent.register(INSTRUMENT_TYPE.CONVERTIBLE)(stock_order_percent)
order_target_value.register(INSTRUMENT_TYPE.CONVERTIBLE)(stock_order_target_value)
order_target_percent.register(INSTRUMENT_TYPE.CONVERTIBLE)(stock_order_target_percent)


@exercise.register(INSTRUMENT_TYPE.CONVERTIBLE)
def convertible_exercise(id_or_ins, amount, convert=False):
    market_code = assure_market_code(id_or_ins)
    amount = int(amount)
    env = Environment.get_instance()
    if convert:
        order = Order.__from_create__(market_code, amount, SIDE.CONVERT_STOCK, None, POSITION_EFFECT.EXERCISE)
    else:
        for enrollment_start_date, enrollment_end_date, exercise_price in get_put_info(market_code):
            if enrollment_start_date <= env.calendar_dt.date() <= enrollment_end_date:
                order = Order.__from_create__(
                    market_code, amount, SIDE.SELL, LimitOrder(exercise_price), POSITION_EFFECT.EXERCISE
                )
                break
        else:
            reason = "回售失败，当前时间不在可转债 {} 回售登记日期范围内".format(market_code)
            env.order_creation_failed(market_code=market_code, reason=reason)
            return

    if env.can_submit_order(order):
        env.broker.submit_order(order)
        return order
