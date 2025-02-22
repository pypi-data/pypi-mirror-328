# -*- coding: utf-8 -*-
from datetime import date, datetime
from functools import lru_cache

import pandas as pd
from deepquant.quest.utils.datetime_func import convert_date_to_date_int
from deepquant.quest.const import INSTRUMENT_TYPE, POSITION_EFFECT, SIDE, TRADING_CALENDAR_TYPE
from deepquant.quest.environment import Environment
from deepquant.quest.mod.mod_sys_accounts.position_model import StockPosition, StockPositionProxy
from deepquant.quest.model.trade import Trade
from deepquant.quest.portfolio.position import Position


@lru_cache(1)
def _get_trading_dates():
    trading_dates = Environment.get_instance().data_source.get_trading_calendars()[TRADING_CALENDAR_TYPE.EXCHANGE]
    trading_dates_df = pd.DataFrame({"trading_date": trading_dates})
    return trading_dates_df


@lru_cache(1024)
def _get_daily_profit(market_code):
    """ 可能在非交易日功分红，把非交易日的分红在下个交易日一并给了 """
    bars = Environment.get_instance().mod_dict["fund"].get_bars(market_code)
    df = pd.DataFrame(bars[["datetime", "daily_profit"]])
    df["datetime"] = pd.to_datetime(df["datetime"] / 1000000, format="%Y%m%d")
    trading_dates_df = _get_trading_dates()
    df = pd.merge_asof(df, trading_dates_df, left_on="datetime", right_on="trading_date", direction="forward")
    df = df.groupby("trading_date", as_index=False).agg({"daily_profit": "sum"})
    df["trading_date"] = df["trading_date"].map(convert_date_to_date_int)
    return df.to_records(index=False)


class FundPosition(StockPosition):
    """
        基金持仓
        _quantity               预期持仓份额 = 已到账份额 + 未到账份额
        _old_quantity           _logical_old_quantity + 今日对昨仓的操作
        _logical_old_quantity   今日开盘时已到账的份额
    """
    __instrument_types__ = (INSTRUMENT_TYPE.PUBLIC_FUND,)

    def __init__(self, market_code, direction, init_quantity=0, init_price=None):
        super().__init__(market_code, direction, init_quantity, init_price)
        env = Environment.get_instance()
        self.subscription_receiving_days = env.config.mod.fund.subscription_receiving_days  # type: int
        self.redemption_receiving_days = env.config.mod.fund.redemption_receiving_days  # type: int

        # 净值类型影响非货币基金能否分红拆分 unit(单位净值) / adjusted(复权净值)
        self._able_dividend = env.config.mod.fund.fund_nav_type == "unit" or self._accrued_fund  # type: bool

        self.subscribe_queue = list()  # (datetime, quantity)
        self.redeem_queue = list()  # (datetime, value)
        self.fund_dividend_reinvestment = env.config.mod.sys_accounts.dividend_reinvestment

        self.accrued_daily = env.data_proxy.instruments(self.market_code).accrued_daily
        self._env = env

    @property
    def equity(self):
        """ 净值 = 预期持仓金额 + 赎回金额 """
        redeem_fund_value = sum(i[1] for i in self.redeem_queue)
        return super(FundPosition, self).equity + redeem_fund_value

    def get_state(self):
        state = super(FundPosition, self).get_state()
        state["subscribe_queue"] = self.subscribe_queue
        state["redeem_queue"] = self.redeem_queue
        return state

    def set_state(self, state):
        super(FundPosition, self).set_state(state)
        self.subscribe_queue = state.get('subscribe_queue') or list()
        self.redeem_queue = state.get('redeem_queue') or list()

    def apply_trade(self, trade):
        # type: (Trade) -> float
        delta_cash = round(super(FundPosition, self).apply_trade(trade), 4)
        self._quantity = round(self._quantity, 4)
        if trade.position_effect == POSITION_EFFECT.OPEN:
            # 延期到账份额
            dt = self._env.data_proxy.get_next_trading_date(trade.trading_datetime, self.subscription_receiving_days)
            dt = dt.to_pydatetime()
            self.subscribe_queue.append((dt, trade.last_quantity))
            self._handle_subscribe_units(trade.trading_datetime.date())
            return delta_cash
        elif trade.position_effect == POSITION_EFFECT.CLOSE:
            # 延期到账金额
            dt = self._env.data_proxy.get_next_trading_date(trade.trading_datetime, self.redemption_receiving_days)
            dt = dt.to_pydatetime()
            self.redeem_queue.append((dt, delta_cash))
            delta_cash = self._handle_redeem_value(trade.trading_datetime.date())
            return delta_cash
        else:
            _message = "{} does not support position effect {}"
            raise NotImplementedError(_message.format(self.__class__.__name__, trade.position_effect))

    def before_trading(self, trading_date):
        # type: (date) -> float
        delta_cash = Position.before_trading(self, trading_date)
        if self._quantity == 0 and len(self.redeem_queue) == 0 and not self._dividend_receivable:
            return 0
        data_proxy = Environment.get_instance().data_proxy
        delta_cash += self._handle_redeem_value(trading_date)                   # 赎回金额
        delta_cash += self._handle_accrued_daily_fund_dividend(trading_date)    # 币基金分红
        if self._able_dividend:
            self._handle_dividend_book_closure(trading_date, data_proxy)        # 获取分红日期
            delta_cash += self._handle_dividend_payable(trading_date)           # 计算可获取的分红
            self._handle_split(trading_date, data_proxy)                        # 基金拆分
        self._handle_subscribe_units(trading_date)
        return delta_cash

    def _date_to_datetime(self, trading_date):
        # type: (date) -> datetime
        return datetime(trading_date.year, trading_date.month, trading_date.day)

    def _handle_dividend_book_closure(self, trading_date, data_proxy):
        # type: (date, DataProxy) -> None
        last_date = data_proxy.get_previous_trading_date(trading_date)
        dividend = data_proxy.get_dividend_by_book_date(self._market_code, last_date)
        if dividend is None:
            return
        dividend_per_share = sum(dividend['dividend_cash_before_tax'] / dividend['round_lot'])
        if dividend_per_share != dividend_per_share:
            raise RuntimeError("Dividend per share of {} is not supposed to be nan.".format(self._market_code))
        self._avg_price -= dividend_per_share

        try:
            payable_date = dividend["payable_date"][0]
        except ValueError:
            payable_date = dividend["ex_dividend_date"][0]
        self._dividend_receivable = (datetime.strptime(str(payable_date), '%Y%m%d').date(),
                                     self._quantity * dividend_per_share)

    def _deal_dividend_reinvestment(self, trading_date):
        dt = self._env.data_proxy.get_next_trading_date(self._dividend_receivable[0], self.subscription_receiving_days)
        dt = dt.to_pydatetime()
        amount = round(self._dividend_receivable[1] / self.last_price, 4)
        self._quantity += amount
        self.subscribe_queue.append((dt, amount))
        self._dividend_receivable = None

    def _handle_dividend_payable(self, trading_date):
        # type: (date) -> float
        """计算可获取的分红"""
        # 返回总资金的变化量
        if not self._dividend_receivable:
            return 0
        payable_date, dividend_value = self._dividend_receivable
        if payable_date != trading_date:
            return 0
        self._dividend_receivable = None
        if self.fund_dividend_reinvestment:
            last_price = 0
            amount = round(dividend_value / self.last_price, 4)
            self.apply_trade(Trade.__from_create__(
                None, last_price, amount, SIDE.BUY, POSITION_EFFECT.OPEN, self._market_code
            ))
            return 0
        else:
            return dividend_value

    def _handle_subscribe_units(self, trading_date):
        """将延期到账的份额增加到账户中"""
        if len(self.subscribe_queue) == 0:
            return

        _index = 0
        for index, data in enumerate(self.subscribe_queue):
            dt, quantity = data
            dt = dt.date()
            if trading_date >= dt:
                self._old_quantity = round(self._old_quantity + quantity, 4)
                self._logical_old_quantity = round(self._logical_old_quantity + quantity, 4)
                _index = index + 1
            else:
                break

        self.subscribe_queue = self.subscribe_queue[_index:]

    def _handle_redeem_value(self, trading_date):
        """将延期到账的"""
        if len(self.redeem_queue) == 0:
            return 0
        ret_value = 0
        _index = 0
        for index, data in enumerate(self.redeem_queue):
            dt, value = data
            if trading_date >= dt.date():
                ret_value += value
                _index = index + 1
            else:
                break
        self.redeem_queue = self.redeem_queue[_index:]
        return round(ret_value, 4)

    def _handle_accrued_daily_fund_dividend(self, trading_date):
        """ 货币基金分红
        通过 fund.get_nav 获取万份/百份收益，将收益以分红再投资的形式应用于持仓
        """
        if not self._accrued_fund:
            return 0
        # 计算已到账资金的份额
        received_equity = self.quantity * self.last_price
        if received_equity == 0:
            return 0
        daily_profit_data = _get_daily_profit(self.market_code)
        trading_date_int = convert_date_to_date_int(trading_date)
        pos = daily_profit_data["trading_date"].searchsorted(trading_date_int)
        if pos == len(daily_profit_data) or daily_profit_data[pos]["trading_date"] != trading_date_int:
            raise RuntimeError("fund daily_profit 应每天都有对应的数据")
        daily_profit = daily_profit_data[pos]["daily_profit"]
        dividend_value = received_equity / 10000 * daily_profit

        # 分红换成quantity
        amount = round(dividend_value / self.last_price, 4)

        dt = self._date_to_datetime(trading_date)
        self._quantity += amount
        self.subscribe_queue.append((dt, amount))
        self._handle_subscribe_units(trading_date)
        return 0

    @property
    @lru_cache(2)
    def _accrued_fund(self):
        # type: () -> bool
        """判断是否非货币基金"""
        return self._env.get_instrument(self._market_code).accrued_daily

    def _handle_split(self, trading_date, data_proxy):
        """处理基金拆分"""
        ratio = data_proxy.get_split_by_ex_date(self._market_code, trading_date)
        if ratio is None:
            return
        self._quantity = round(self._quantity * ratio, 4)
        self._old_quantity = round(self._old_quantity * ratio, 4)
        self._logical_old_quantity = round(self._logical_old_quantity * ratio, 4)
        self._avg_price /= ratio
        # ex_cum_factor 中未保存 公募基金的复权因子, 导致获取到的价格是未复权的，在这里进行复权
        self._prev_close = self.prev_close / ratio

        # 未到账份额进行拆分
        for index, data in enumerate(self.subscribe_queue):
            dt, quantity = data
            self.subscribe_queue[index] = (dt, round(quantity * ratio, 4))

    @property
    def receivable_quantity(self):
        # type: () -> float
        """未到账份额"""
        subscribe_units_value = sum(i[1] for i in self.subscribe_queue)
        return subscribe_units_value

    @property
    def receivable_cash(self):
        # type: () -> float
        """未到账金额"""
        redeem_fund_value = sum(i[1] for i in self.redeem_queue)
        return redeem_fund_value

    @property
    def quantity(self):
        """ 已到账份额 = 预期持有份额 - 未到账份额 """
        return round(self._quantity - self.receivable_quantity, 4)

    @property
    def closable(self):
        # type: () -> float
        return self.quantity

    @property
    def today_closable(self):
        # type: () -> float
        return self.quantity

    def settlement(self, trading_date):
        # type: (date) -> float
        if self._able_dividend and self._dividend_receivable and self.fund_dividend_reinvestment:
            self._deal_dividend_reinvestment(trading_date)  # 计算可获取的分红
            self._handle_subscribe_units(trading_date)
        return 0


class FundPositionProxy(StockPositionProxy):
    __instrument_types__ = (INSTRUMENT_TYPE.PUBLIC_FUND,)

    type = property(lambda self: INSTRUMENT_TYPE.PUBLIC_FUND)
