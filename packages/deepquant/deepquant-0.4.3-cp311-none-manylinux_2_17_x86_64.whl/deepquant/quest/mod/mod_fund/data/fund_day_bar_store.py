#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2020/8/7 14:58
# @File    : day_bar_store.py
import copy

import numpy
import deepquant.quest.datac
from abc import ABC
from functools import lru_cache
from deepquant.quest.data.base_data_source.storage_interface import AbstractDayBarStore
from deepquant.quest.environment import Environment
from deepquant.quest.utils.datetime_func import convert_date_to_int


class BaseFundDayBarStore(AbstractDayBarStore, ABC):
    """基金日线信息"""
    # @formatter:off
    FIELD_MAP = {
        'datetime': ('<u8', lambda df: convert_date_to_int(df.index).values),
        "volume": ('<f8', lambda _: numpy.nan,),
        "total_turnover": ('<f8', lambda _: numpy.nan,),
        "high_limited": ('<f8', lambda _: numpy.nan,),
        "low_limited": ('<f8', lambda _: numpy.nan,),
        "subscribe_upper_limit": ('<f8', lambda df: df['subscribe_upper_limit'].values if 'subscribe_upper_limit' in df.columns.to_list() else numpy.nan,),
        "subscribe_lower_limit": ('<f8', lambda df: df['subscribe_lower_limit'].values if 'subscribe_lower_limit' in df.columns.to_list() else numpy.nan,),
        "redeem_lower_limit": ('<f8', lambda df: df['redeem_lower_limit'].values if 'redeem_lower_limit' in df.columns.to_list() else numpy.nan,),
    }
    # @formatter:on

    START_DATE = "20050104"
    END_DATE = "29991231"

    FIELD_MAP_ACCRUED_DAILY = FIELD_MAP.copy()
    FIELD_MAP_ACCRUED_DAILY.update({
        "open": ('<u8', lambda _: 1,),
        "high": ('<f8', lambda _: 1,),
        "low": ('<f8', lambda _: 1,),
        "close": ('<f8', lambda _: 1,),
        "prev_close": ('<f8', lambda _: 1,),
        "isnan": ('<f8', lambda df: numpy.isnan(df["daily_profit"]),),
        "daily_profit": ('<f8', lambda df: df['daily_profit'].values,),
        "weekly_yield": ('<f8', lambda df: df['weekly_yield'].values,),
    })

    def __init__(self, fund_nav_type):
        # 净值类型 unit(单位净值) / adjusted(复权净值)
        _nav_type_map = {"unit": "unit_net_value", "adjusted": "adjusted_net_value"}
        if fund_nav_type not in _nav_type_map.keys():
            raise KeyError("mod fund 参数fund_nav_type输入错误({}),请输入:unit (单位净值) / adjusted (复权净值)")
        self._nav_type = _nav_type_map[fund_nav_type]

    def _get_nav(self, market_code):
        raise NotImplementedError()

    @lru_cache(2048)
    def get_bars(self, market_code):
        df = self._get_nav(market_code)

        if df is None or df.empty:
            return numpy.empty(0, dtype=[(field, d_type) for field, d_type, func in self.FIELD_MAP])

        env = Environment.get_instance()
        instrument = env.get_instrument(market_code)

        if instrument.accrued_daily:
            # 货币基金
            FIELD_MAP = copy.copy(self.FIELD_MAP_ACCRUED_DAILY)
        else:  # 非货币基金
            FIELD_MAP = copy.copy(self.FIELD_MAP)
            FIELD_MAP.update({
                "open": ('<f8', lambda _df: _df[self._nav_type].values,),
                "high": ('<f8', lambda _df: _df[self._nav_type].values,),
                "low": ('<f8', lambda _df: _df[self._nav_type].values,),
                "close": ('<f8', lambda _df: _df[self._nav_type].values,),
                "prev_close": ('<f8', lambda _df: _df[self._nav_type].shift(1).values,),
                "isnan": ('<f8', lambda _df: numpy.isnan(_df[self._nav_type]),),
            })

        if "subscribe_status" in df.columns.to_list():
            # @formatter:off
            FIELD_MAP.update({
                "suspended": ('bool', lambda _df: (_df["redeem_status"] == _df["subscribe_status"]) & _df["redeem_status"].isin(["Suspended", "Close"]),),
                "subscribe_status": ('S10', lambda _df: _df["subscribe_status"].values,),
                "redeem_status": ('S10', lambda _df: _df['redeem_status'].values,),
            })
            # @formatter:on

        _d_type = numpy.dtype([(field, d_type) for field, (d_type, func) in FIELD_MAP.items()])
        ret = numpy.ndarray(df.shape[0], dtype=_d_type)
        for field, (d_type, rqd_field) in FIELD_MAP.items():
            ret[field] = rqd_field(df)

        env = Environment.get_instance()

        if env.get_instrument(market_code).exchange and instrument.accrued_daily:
            ret["open"] = ret["high"] = ret["low"] = ret["close"] = ret["prev_close"] = 100

        return ret


class RqdataFundDayBarStore(BaseFundDayBarStore):
    """基金日线信息 rqdata 版本"""

    def __init__(self, fund_nav_type, investor='institution'):
        super().__init__(fund_nav_type)
        # for fund.get_transaction_status ,not use
        if investor not in ["institution", "retail"]:
            raise ValueError("investor(投资者身份)可选为institution(机构)/retail(个人)，当前为{}".format(investor))
        self.investor = investor

    def _get_nav(self, market_code):
        df_nav = deepquant.quest.datac.fund.get_nav(market_code, start_date=self.START_DATE, end_date=self.END_DATE)

        if df_nav is None or df_nav.empty:
            raise ValueError("基金标的{} 在rqdata.fund.get_nav无数据".format(market_code))
        # deepquant.quest.datac会去掉这两个字段
        if 'subscribe_status' in df_nav.columns:
            del df_nav['subscribe_status']
            del df_nav['redeem_status']
        if hasattr(deepquant.quest.datac.fund, "get_transaction_status"):
            try:
                df_transaction_status = self._get_transaction_status(market_code)
                df = df_nav.join(df_transaction_status, how='inner')
            except deepquant.quest.datac.share.errors.BadRequest:
                df = df_nav
        else:
            df = df_nav
        return df

    @lru_cache(1024)
    def _get_transaction_status(self, market_code):
        df = deepquant.quest.datac.fund.get_transaction_status(market_code, start_date=self.START_DATE, end_date=self.END_DATE)

        if df is None or df.empty:
            raise ValueError("基金标的{} 在rqdata.fund.get_transaction_status数据".format(market_code))
        return df.reset_index(level="market_code", drop=True)

    def get_date_range(self, market_code):
        df = self._get_nav(market_code)
        start = convert_date_to_int(df.index[0])
        end = convert_date_to_int(df.index[-1])
        return start, end
