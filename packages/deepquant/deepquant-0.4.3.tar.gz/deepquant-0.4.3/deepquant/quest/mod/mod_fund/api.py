# -*- coding: utf-8 -*-
"""基金相关api"""
from typing import Optional, Union
from decimal import Decimal

from deepquant.quest.api import export_as_api
from deepquant.quest.apis.api_abstract import order, order_percent, order_shares, order_target_percent, order_target_value, \
    order_to, order_value
from deepquant.quest.const import EXECUTION_PHASE, INSTRUMENT_TYPE
from deepquant.quest.core.execution_context import ExecutionContext
from deepquant.quest.model.instrument import Instrument
from deepquant.quest.utils.arg_checker import apply_rules, verify_that

from deepquant.quest.model.order import MarketOrder
from deepquant.quest.apis.api_base import assure_instrument
from deepquant.quest.const import DEFAULT_ACCOUNT_TYPE, ORDER_TYPE, POSITION_DIRECTION, POSITION_EFFECT, SIDE
from deepquant.quest.environment import Environment
from deepquant.quest.model.order import Order
from deepquant.quest.utils import is_valid_price
from deepquant.quest.utils.i18n import gettext as _
from deepquant.quest.utils.logger import user_system_log
from deepquant.quest.core.events import Event, EVENT

from .transaction import FundTransactionDecider


def _get_account_position_ins(id_or_ins):
    """通过oder_book_id 获取持仓"""
    ins = assure_instrument(id_or_ins)
    account = Environment.get_instance().portfolio.accounts[DEFAULT_ACCOUNT_TYPE.STOCK]
    position = account.get_position(ins.market_code, POSITION_DIRECTION.LONG)
    return account, position, ins


def _submit_order(ins, amount, side, position_effect, position, fee=None):
    """提交一个特定份额的订单"""
    env = Environment.get_instance()
    price = env.data_proxy.get_last_price(ins.market_code)
    if not is_valid_price(price):
        reason = _(u"Order Creation Failed: [{market_code}] No market data").format(market_code=ins.market_code)
        env.order_creation_failed(ins.market_code, reason=reason)
        return

    if not (side == SIDE.SELL and amount == position.closable):
        amount = round(amount, 4)

    if amount == 0:
        reason = _(u"Order Creation Failed: 0 order quantity")
        env.order_creation_failed(ins.market_code, reason=reason)
        return
    if fee is None:
        fee = round(amount * price * env.config.mod.fund.fee_ratio, 4) if side == SIDE.BUY else 0
    order = Order.__from_create__(ins.market_code, abs(amount), side, MarketOrder(), position_effect, fee=fee)
    order.set_frozen_price(price)
    if env.can_submit_order(order):
        env.broker.submit_order(order)
        return order


def _order_shares(ins, amount, position, fee=None):
    """按份额下单"""
    side, position_effect = (SIDE.BUY, POSITION_EFFECT.OPEN) if amount > 0 else (SIDE.SELL, POSITION_EFFECT.CLOSE)
    return _submit_order(ins, amount, side, position_effect, position, fee)


def _order_value(account, position, ins, cash_amount):
    """按资金下单 产生的费用（包括手续费）将小于设定资金"""
    if account.cash < cash_amount:
        user_system_log.warn(_(
            "insufficient cash, use all remaining cash({}) to create order"
        ).format(account.cash))
        return _order_value(account, position, ins, account.cash)

    env = Environment.get_instance()
    price = env.data_proxy.get_last_price(ins.market_code)
    if cash_amount > 0:
        fee = round(cash_amount - cash_amount / (1 + env.config.mod.fund.fee_ratio), 4)
        shares = round((cash_amount - fee) / price - 0.00005, 4)
        return _order_shares(ins, shares, position, fee)
    else:
        shares = round(cash_amount / price + 0.00005, 4)
        if shares * price < cash_amount:
            # 避免大于需要赎回金额
            shares += 0.001
        if position.quantity < shares:
            user_system_log.warn(_(
                "insufficient cash, use all remaining cash({}) to create order"
            ).format(position.quantity))
            shares = position.quantity
        return _order_shares(ins, shares, position, 0)


@export_as_api
@ExecutionContext.enforce_phase(
    EXECUTION_PHASE.OPEN_AUCTION,
    EXECUTION_PHASE.ON_BAR,
    EXECUTION_PHASE.ON_TICK,
    EXECUTION_PHASE.SCHEDULED,
    EXECUTION_PHASE.GLOBAL
)
@apply_rules(
    verify_that("market_code").is_valid_instrument([INSTRUMENT_TYPE.PUBLIC_FUND]),
    verify_that('cash_amount').is_number(), )
def subscribe_value(market_code, cash_amount):
    # type: (Union[str, Instrument], float) -> Optional[Order]
    """
    按申购金额申购基金

    :param market_code: 申购基金
    :param cash_amount: 申购所用资金
    :return: None or Order

    :example:

    .. code-block:: python

        # 申购五千块的'华夏成长混合'(000001)
        order = subscribe_value('000001', 5000)
        assert order.avg_price * order.quantity + order.transaction_cost <= 5000
    """
    account, position, ins = _get_account_position_ins(market_code)
    return _order_value(account, position, ins, cash_amount)


@export_as_api
@apply_rules(
    verify_that("market_code").is_valid_instrument([INSTRUMENT_TYPE.PUBLIC_FUND]),
    verify_that('percent').is_number(), )
def subscribe_percent(market_code, percent):
    # type: (Union[str, Instrument], float) -> Optional[Order]
    """
    按账户资金百分比申购基金

    :param market_code: 申购基金
    :param percent: 可用资金权重
    :return: None or Order

    :example:

    .. code-block:: python

        # 用当前账户资金的20%申购
        order = subscribe_percent('000001', 0.2)
    """
    account, position, ins = _get_account_position_ins(market_code)
    return _order_value(account, position, ins, account.cash * percent)


@export_as_api
@apply_rules(
    verify_that("market_code").is_valid_instrument([INSTRUMENT_TYPE.PUBLIC_FUND]),
    verify_that('shares').is_number(), )
def subscribe_shares(market_code, shares):
    # type: (Union[str, Instrument], int) -> Optional[Order]
    """
    按照份额申购

    :param market_code: 申购基金
    :param shares: 份额
    :return: None or Order

    :example:

    .. code-block:: python

        # 申购3000份'华夏成长混合'(000001)
        order = subscribe_shares('000001', 3000)
    """
    account, position, ins = _get_account_position_ins(market_code)
    return _order_shares(ins, shares, position)


@export_as_api
@apply_rules(
    verify_that("market_code").is_valid_instrument([INSTRUMENT_TYPE.PUBLIC_FUND]),
    verify_that('percent').is_number(), )
def redeem_percent(market_code, percent):
    # type: (Union[str, Instrument], float) -> Optional[Order]
    """
    按权重赎回基金，需要根据赎回总金额，计算份额。
    按比例赎回时，不足0.01份则不赎回

    :param market_code: 赎回基金
    :param percent: 可赎回份额权重
    :return: None or Order

    :example:

    .. code-block:: python

        # 赎回20%的'华夏成长混合'(000001)
        order = redeem_percent('000001', 0.2)

    """
    account, position, ins = _get_account_position_ins(market_code)
    return _order_shares(ins, position.quantity * percent * -1, position)


@export_as_api
@apply_rules(
    verify_that("market_code").is_valid_instrument([INSTRUMENT_TYPE.PUBLIC_FUND]),
    verify_that('shares').is_number(), )
def redeem_shares(market_code, shares):
    # type: (Union[str, Instrument], float) -> Optional[Order]
    """
    按份额赎回基金

    :param market_code: 赎回基金
    :param shares: 赎回份额
    :return: None or Order

    :example:

    .. code-block:: python

        # 赎回200份'华夏成长混合'(000001)
        order = redeem_shares('000001', 200)
    """
    account, position, ins = _get_account_position_ins(market_code)
    return _order_shares(ins, shares * -1, position)


@export_as_api
@apply_rules(
    verify_that("market_code").is_valid_instrument([INSTRUMENT_TYPE.PUBLIC_FUND]),
    verify_that('cash_amount').is_number(), )
def redeem_value(market_code, cash_amount):
    # type: (Union[str, Instrument], float) -> Optional[Order]
    """
    根据赎回总金额计算份额

    :param market_code: 赎回基金
    :param cash_amount: 赎回金额
    :return: None or Order

    :example:

    .. code-block:: python

        # 赎回价值5000块'华夏成长混合'(000001)
        order = redeem_value('000001', 5000)
    """
    account, position, ins = _get_account_position_ins(market_code)
    return _order_value(account, position, ins, -1 * cash_amount)


# not export_as_api
@apply_rules(
    verify_that("market_code").is_valid_instrument([INSTRUMENT_TYPE.PUBLIC_FUND]),
    verify_that('shares').is_number(), )
def subscribe_to_target_value(market_code, value):
    """申购目标价值"""
    account, position, ins = _get_account_position_ins(market_code)
    cash_amount = value - (position.equity - position.receivable_cash)
    if value == 0:
        # 平仓直接调用 order_shares，避免 _order_value 导致平不干净的情况
        return _order_shares(ins, -position.quantity, position)
    return _order_value(account, position, ins, cash_amount)


@apply_rules(
    verify_that("market_code").is_valid_instrument([INSTRUMENT_TYPE.PUBLIC_FUND]),
    verify_that('shares').is_number(), )
def subscribe_to_target_percent(market_code, percent):
    """申购仓位到占有一个目标价值"""
    account, position, ins = _get_account_position_ins(market_code)
    value = account.total_value * percent
    cash_amount = value - (position.equity - position.receivable_cash)
    if percent == 0:
        # 平仓直接调用 order_shares，避免 _order_value 导致平不干净的情况
        return _order_shares(ins, -position.quantity, position)
    return _order_value(account, position, ins, cash_amount)


@apply_rules(
    verify_that("market_code").is_valid_instrument([INSTRUMENT_TYPE.PUBLIC_FUND]),
    verify_that('shares').is_number(), )
def subscribe_to_shares(market_code, shares):
    """调仓函数到指定份额"""
    account, position, ins = _get_account_position_ins(market_code)
    to_shares = shares - position.quantity - position.receivable_quantity
    return _order_shares(ins, to_shares, position)


def init_fund_api(_):
    order.register(INSTRUMENT_TYPE.PUBLIC_FUND)(subscribe_shares)
    order_value.register(INSTRUMENT_TYPE.PUBLIC_FUND)(subscribe_value)
    order_percent.register(INSTRUMENT_TYPE.PUBLIC_FUND)(subscribe_percent)
    order_shares.register(INSTRUMENT_TYPE.PUBLIC_FUND)(subscribe_shares)
    order_to.register(INSTRUMENT_TYPE.PUBLIC_FUND)(subscribe_to_shares)
    order_target_value.register(INSTRUMENT_TYPE.PUBLIC_FUND)(subscribe_to_target_value)
    order_target_percent.register(INSTRUMENT_TYPE.PUBLIC_FUND)(subscribe_to_target_percent)
