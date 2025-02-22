#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: zhangluping_it
@time: 2024/8/8 13:09
@description:
"""
import threading
import time

import sys
import os

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(project_path)
sys.path.append(project_path)

from src.utils import gqconfig
from src.gqclient.hclient import GidHClient
from src.gqclient.wsclient import WsClient, SubDataType, MarketType, VarietyCategoryType, ReplayCondition
from src.samples.md_handler_demo import MarketDataPushHandler

securities = ['000001.SZ', '600000.SH']


def monitor_thread():
    global keep_running
    # 监控线程逻辑
    print("数据回放-监控线程启动")
    while True:
        try:
            user_input = input("输入'stop'来停止订阅，exit退出程序: ")
            if user_input.strip().lower() == 'exit':
                print("数据回放-准备退出程序")
                replay_client.stop()
                keep_running = False
                break
            if user_input.strip().lower() == 'start':
                print("数据回放-开启连接...")
                replay_client.start()
            if user_input.strip().lower() == 'stop':
                print("数据回放-断开连接...")
                replay_client.stop()
                replay_handler.clear_stat()
                print("数据回放-已断开连接")
            if user_input.strip().lower() == 'sub':
                print("数据回放-回放股票池:", securities)
                replay_client.replay_req(
                    replay_conditions=[
                        ReplayCondition(SubDataType.SNAPSHOT,
                                        ['security_code', 'open_price', 'high_price', 'last_price',
                                         'bid_price', 'bid_volume', 'offer_price', 'offer_volume',
                                         'total_volume_trade', 'total_value_trade', 'orig_time']),
                        ReplayCondition(SubDataType.KLINE_1m,
                                        ['security_code', 'open_price', 'high_price', 'close_price',
                                         'volume', 'value', 'orig_time']),
                    ],
                    security_codes=securities,
                    start_time='2024-08-09 00:00:00.000',
                    end_time='2024-08-11 23:59:59.999',
                )
                replay_handler.clear_stat()
        except Exception as e:
            print(e)
        time.sleep(1)
    print("数据回放-退出程序")


if __name__ == '__main__':
    print("数据回放-开始运行")
    gqconfig.reload_config('dev')

    # 全局标志变量
    keep_running = True
    # 创建监控线程
    monitor_thread = threading.Thread(target=monitor_thread)
    monitor_thread.start()

    reqClient = GidHClient()
    reqClient.init('gidtest', 'gid#2024')

    # 自定义行情数据处理类
    replay_handler = MarketDataPushHandler()
    # 行情连接客户端
    replay_client = WsClient()
    replay_client.init(reqClient)
    replay_client.add_replay_handler(replay_handler)
    # 启动行情连接
    replay_client.start()

    while keep_running:
        time.sleep(1)
