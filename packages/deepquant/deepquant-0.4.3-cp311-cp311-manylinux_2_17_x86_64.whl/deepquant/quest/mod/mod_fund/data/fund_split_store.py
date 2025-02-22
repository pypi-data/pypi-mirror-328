#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/8/7 15:03
# @File    : fund_split_store.py
from functools import lru_cache

import numpy

import deepquant.quest.datac
from deepquant.quest.data.base_data_source.storage_interface import AbstractSimpleFactorStore
from deepquant.quest.utils.datetime_func import convert_date_to_int


class RqdataFundSplitStore(AbstractSimpleFactorStore):
    """基金拆分信息"""
    DATA_TYPE = numpy.dtype([('ex_date', '<i8'), ('split_factor', '<f8')])

    @lru_cache(None)
    def get_factors(self, market_code):
        df = deepquant.quest.datac.fund.get_split(market_code)
        if df is not None and not df.empty:
            df = df.reset_index()
            ret = numpy.ndarray(df.shape[0], dtype=self.DATA_TYPE)
            ret['ex_date'] = df.ex_dividend_date.apply(convert_date_to_int).values
            ret['split_factor'] = df.split_ratio.values
            return ret
        else:
            return None
