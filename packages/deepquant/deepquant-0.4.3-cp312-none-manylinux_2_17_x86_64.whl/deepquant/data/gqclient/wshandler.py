#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: zhangluping_it
@time: 2024/8/2 9:45
@description: 
"""
from abc import ABC, abstractmethod
from enum import Enum

from ..proto.data_type_pb2 import L2_SNAPSHOT,\
    L2_KLINE_MIN, L2_KLINE_3MIN, L2_KLINE_5MIN, L2_KLINE_10MIN, L2_KLINE_15MIN, L2_KLINE_30MIN,\
    L2_KLINE_60MIN, L2_KLINE_120MIN
from ..proto.data_type_pb2 import STOCK as VC_STOCK, FUND as VC_FUND, BOND as VC_BOND, INDEX as VC_INDEX
from ..utils.log_writer import log


class SubDataType(Enum):
    """
    行情订阅数据类型
    """
    SNAPSHOT = L2_SNAPSHOT  # 快照
    KLINE_1m = L2_KLINE_MIN  # 1m K线
    KLINE_3m = L2_KLINE_3MIN  # 3m K线
    KLINE_5m = L2_KLINE_5MIN  # 5m K线
    KLINE_10m = L2_KLINE_10MIN  # 10m K线
    KLINE_15m = L2_KLINE_15MIN  # 15m K线
    KLINE_30m = L2_KLINE_30MIN  # 30m K线
    KLINE_60m = L2_KLINE_60MIN  # 60m K线
    KLINE_120m = L2_KLINE_120MIN  # 120m K线


class MarketType(Enum):
    """
    市场类别
    """
    SZ = 'SZ'  # 深圳
    SH = 'SH'  # 上海


class VarietyCategoryType(Enum):
    """
    品种类别
    """
    STOCK = VC_STOCK
    FUND = VC_FUND
    BOND = VC_BOND
    INDEX = VC_INDEX


class ReplayCondition:

    def __init__(self, data_type: SubDataType,
                 replay_fields=None):
        self.data_type = data_type
        self.replay_fields = replay_fields


class LogHandler(ABC):
    def on_push_log(self, log_level, log_timestamp, trace_id, srv_name, message, error_code):
        print('LogHandler.on_push_log', log_level, log_timestamp, trace_id, srv_name, message, error_code)


class BaseDataHandler(ABC):

    def on_message(self, msg, error):
        print('on_message', 'msg:', msg, 'error:', error)

    def on_user_report(self, data, error):
        log.info('on_user_report：%s, error=%s', data, error)


class BaseMDPushSpi(ABC):
    """
    行情订阅的回调接口，增加行情数据类型时，需要扩展该接口
    """

    def on_message(self, msg, error):
        print('on_message', 'msg:', msg, 'error:', error)

    def on_subscribe_res(self, data, error):
        print('on_subscribe_res', 'data:', data, 'error:', error)

    @abstractmethod
    def on_snapshot(self, data, error, **kwargs):
        pass

    @abstractmethod
    def on_execution(self, data, error):
        pass

    @abstractmethod
    def on_order(self, data, error):
        pass

    @abstractmethod
    def on_orderqueue(self, data, error):
        pass

    @abstractmethod
    def on_kline(self, data, error):
        pass

    @abstractmethod
    def on_index(self, data, error):
        pass

    @abstractmethod
    def on_factor(self, data, error):
        pass

    def on_factor_sub_res(self, data, error):
        print('on_factor_sub_res', 'data:', data, 'error:', error)
