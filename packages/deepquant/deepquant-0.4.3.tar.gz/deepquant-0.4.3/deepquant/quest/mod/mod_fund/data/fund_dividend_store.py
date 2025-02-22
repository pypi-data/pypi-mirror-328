#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2020/8/7 15:02
# @File    : fund_dividend_store.py
from functools import lru_cache

import deepquant.quest.datac

from deepquant.quest.data.base_data_source.storage_interface import AbstractDividendStore
from deepquant.quest.utils.datetime_func import convert_date_to_date_int

from deepquant.quest.environment import Environment

class RqdataFundDividendStore(AbstractDividendStore):
    """基金分红信息"""
    DATA_TYPE = [
        ('book_closure_date', '<i8'),
        ('announcement_date', '<i8'),
        ('dividend_cash_before_tax', '<f8'),
        ('ex_dividend_date', '<i8'),
        ('payable_date', '<i8'),
        ('round_lot', '<f8')
    ]

    def __init__(self):
        ins_df = deepquant.quest.datac.fund.all_instruments()
        self._env = Environment.get_instance()
        _dividend_df = deepquant.quest.datac.fund.get_dividend(ins_df.market_code.to_list())
        if _dividend_df is None:
            self.dividend_df = None
            return
        _dividend_df = _dividend_df.reset_index('ex_dividend_date')
        _dividend_df["ex_dividend_date"] = convert_date_to_date_int(_dividend_df['ex_dividend_date'].dt)
        _dividend_df["book_closure_date"] = convert_date_to_date_int(_dividend_df['book_closure_date'].dt)
        _dividend_df["payable_date"] = convert_date_to_date_int(_dividend_df['payable_date'].dt)
        _dividend_df["announcement_date"] = _dividend_df["book_closure_date"]
        _dividend_df["round_lot"] = 1.0
        _dividend_df["dividend_cash_before_tax"] = _dividend_df['dividend_before_tax']
        _dividend_df = _dividend_df[[k for k, v in self.DATA_TYPE]]
        self.dividend_df = _dividend_df

    @lru_cache(2048)
    def get_dividend(self, market_code):
        if self.dividend_df is None:
            return
        df = self.dividend_df[self.dividend_df.index == market_code]
        ret = df.to_records(index=False)
        for index, row in enumerate(ret):
            # 当前的计算是复用的股票逻辑
            ret[index][0] = int(self._env.data_proxy.get_next_trading_date(str(ret[index][0]), n=-1)
                                 .strftime('%Y%m%d'))
        return ret
