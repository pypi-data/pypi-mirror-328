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
sys.path.append(project_path)

from deepquant.data.gqclient.hclient import GidHClient
from deepquant.data.gqclient.wsclient import WsClient, SubDataType, MarketType, VarietyCategoryType
from deepquant.samples.md_handler_demo import MarketDataPushHandler

securities = ['000001.SZ', '600000.SH']


def monitor_thread():
    global keep_running
    # 监控线程逻辑
    print("实时行情-监控线程启动")
    while True:
        try:
            user_input = input("输入'stop'来停止订阅，exit退出程序: ")
            if user_input.strip().lower() == 'exit':
                print("实时行情-准备退出程序")
                ws_client.stop()
                keep_running = False
                break
            if user_input.strip().lower() == 'start':
                print("实时行情-开启连接...")
                ws_client.start()
            if user_input.strip().lower() == 'stop':
                print("实时行情-断开连接...")
                ws_client.stop()
                md_handler.clear_stat()
                print("实时行情-已断开连接")
            if user_input.strip().lower() == 'sub':
                print("实时行情-发送订阅股票池:", securities)
                ws_client.subscribe_md(SubDataType.SNAPSHOT, securities)
            if user_input.strip().lower() == 'un':
                print("实时行情-取消订阅股票池:", securities)
                ws_client.unsubscribe_md(SubDataType.SNAPSHOT, securities)
            if user_input.strip().lower() == 'subf':
                print("实时因子-发送订阅股票池:", securities)
                ws_client.subscribe_factor('AskVol_1', securities)
            if user_input.strip().lower() == 'unf':
                print("实时因子-取消订阅股票池:", securities)
                ws_client.unsubscribe_factor('AskVol_1', securities)
            if user_input.strip().lower() == 'suball':
                print("实时行情-发送订阅沪深全市场")
                ws_client.subscribe_md(SubDataType.SNAPSHOT,
                                       market=MarketType.SZ,
                                       category_type=VarietyCategoryType.STOCK)
                ws_client.subscribe_md(SubDataType.SNAPSHOT,
                                       market=MarketType.SH,
                                       category_type=VarietyCategoryType.STOCK)
            if user_input.strip().lower() == 'unall':
                print("实时行情-取消订阅沪深全市场")
                ws_client.unsubscribe_md(SubDataType.SNAPSHOT,
                                         market=MarketType.SZ,
                                         category_type=VarietyCategoryType.STOCK)
                ws_client.unsubscribe_md(SubDataType.SNAPSHOT,
                                         market=MarketType.SH,
                                         category_type=VarietyCategoryType.STOCK)
                md_handler.clear_stat()
        except Exception as e:
            print(e)
        time.sleep(1)
    print("实时行情-退出程序")


if __name__ == '__main__':
    print("实时行情-demo开始运行")
    # 全局标志变量
    keep_running = True
    # 创建监控线程
    monitor_thread = threading.Thread(target=monitor_thread)
    monitor_thread.start()

    reqClient = GidHClient()
    reqClient.init('gidtest', 'gid#2024')

    # 自定义行情数据处理类
    md_handler = MarketDataPushHandler()
    # 行情连接客户端
    ws_client = WsClient()
    ws_client.init(reqClient)
    ws_client.add_md_handler(md_handler)
    ws_client.add_factor_handler(md_handler)
    # 启动行情连接
    ws_client.start()

    while keep_running:
        time.sleep(1)
