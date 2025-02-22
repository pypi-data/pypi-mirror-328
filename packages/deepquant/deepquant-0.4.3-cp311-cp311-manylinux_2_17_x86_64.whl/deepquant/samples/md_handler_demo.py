#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: zhangluping_it
@time: 2024/8/1 19:10
@description: 
"""
import time
from datetime import datetime

import numpy as np

from ..data.gqclient.wsclient import BaseMDPushSpi
from ..data.utils.log_writer import log


class MarketDataPushHandler(BaseMDPushSpi):
    """
    实时行情回调
    """

    def __init__(self):
        self.time_costs = []
        self.time_cost_sum = 0
        self.time_cost_count = 0
        self.time_max = 0
        self.time_max_data = None
        self.time_inc_first = None

    def on_subscribe_res(self, data, error):
        if error is not None:
            log.error('MarketDataPushHandler-on_subscribe_res-error: %s', error)
        else:
            log.info('MarketDataPushHandler-on_subscribe_res-data: %s', data)

    def on_index(self, data, error):
        if error is not None:
            print('MarketDataPushHandler', 'on_index', 'error:', error)
        else:
            print('MarketDataPushHandler', 'on_index', 'data:', data)

    def on_snapshot(self, data, error, **kwargs):
        if error is not None:
            print('MarketDataPushHandler', 'on_snapshot', 'error:', error)
        else:
            _t_last = int(time.time() * 1000)
            orig_time = data.get('orig_time')  # int类型
            received_time = data.get('received_time')  # int类型
            if received_time is not None:
                if isinstance(received_time, int):
                    _t_amd_rcv = received_time
                elif isinstance(received_time, str):
                    dt = datetime.strptime(received_time, '%Y-%m-%d %H:%M:%S.%f')
                    _t_amd_rcv = int(dt.timestamp() * 1000)
                else:
                    return
                if _t_amd_rcv > 0:
                    _t_millis = [_t_amd_rcv]
                    if kwargs is not None and 'timestamps' in kwargs:
                        _t_millis.extend(kwargs.get('timestamps'))
                    _cost = int(_t_last) - _t_amd_rcv
                    if self.time_inc_first is None:
                        self.time_inc_first = _cost
                    self.time_cost_sum = self.time_cost_sum + _cost
                    self.time_cost_count = self.time_cost_count + 1
                    self.time_costs.append(_cost)
                    if _cost > self.time_max:
                        self.time_max = _cost
                        self.time_max_data = _t_millis, data
                    log.info('MarketDataPushHandler-on_snapshot: '
                             '{"_cost":%s,"_cost_avg":%s,'
                             ' "_t_last":%s, "_t_amd_rcv":%s, "_t_millis":|%s|,'
                             ' "security_code":"%s" , "orig_time":"%s" }',
                             _cost, round(self.time_cost_sum / self.time_cost_count, 3),
                             _t_last, _t_amd_rcv, _t_millis, data.get('security_code'), orig_time)

    def on_execution(self, data, error):
        if error is not None:
            print(error)
        else:
            print(data)

    def on_order(self, data, error):
        if error is not None:
            print(error)
        else:
            print(data)

    def on_orderqueue(self, data, error):
        if error is not None:
            print(error)
        else:
            print(data)

    def on_kline(self, data, error):
        if error is not None:
            print('MarketDataPushHandler', 'on_kline', 'error:', error)
        else:
            _timestamp = int(time.time() * 1000)
            _time_cost = None
            if data.get('timeStamp') > 0:
                _time_cost = _timestamp - data.get('timeStamp')
                self.time_cost_sum = self.time_cost_sum + _time_cost
                self.time_cost_count = self.time_cost_count + 1
                self.time_costs.append(_time_cost)
            print('MarketDataPushHandler', 'on_kline',
                  '_time_cost', _time_cost, 'avg_cost', round(self.time_cost_sum / self.time_cost_count, 3),
                  'data:', data)

    def on_factor(self, data, error):
        if error is not None:
            print('MarketDataPushHandler', 'on_factor', 'error:', error)
        else:
            print('MarketDataPushHandler', 'on_factor', 'data:', data)

    def clear_stat(self):
        data = np.array(self.time_costs)
        print('count=', len(self.time_costs))
        stat_out = "count={}, min={}, max={}, median={}, avg={}, tp90={}, max_data={}".format(
            len(self.time_costs), np.min(data), np.max(data), np.median(data), np.mean(data), np.percentile(data, 90),
            self.time_max_data)
        print('[clear_stat]', stat_out)
        log.info(stat_out)
        self.time_costs.clear()
        self.time_cost_count = 0
        self.time_cost_sum = 0
        self.time_inc_first = None
