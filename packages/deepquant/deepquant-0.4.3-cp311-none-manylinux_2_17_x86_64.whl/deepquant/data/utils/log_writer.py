#!/usr/bin/python
# _*_coding:utf-8_*_

import logging
import os
import time
from .gqconfig import configs

log_config = configs.get_log_config()

LOG_LEVEL_FILE = log_config[0]
LOG_LEVEL_CONSOLE = log_config[0]

WITH_CONSOLE = log_config[1]
WITH_LOG_FILE = log_config[2]


class Logger:
    def __init__(self, name=__name__):
        # 创建一个logger
        self.__name = name
        self.logger = logging.getLogger(self.__name)
        self.logger.setLevel(logging.INFO)  # Log等级总开关
        self.console_logger = logging.getLogger(self.__name)
        # 定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s\t[%(levelname)s]\t[%(filename)s][%(lineno)d][%(funcName)s] "
                                      "%(message)s")

        # 将logger添加到handler里面
        if not self.logger.handlers:
            if WITH_CONSOLE:
                # 创建一个handler，用于将日志输出到控制台
                ch = logging.StreamHandler()
                ch.setLevel(LOG_LEVEL_CONSOLE)
                ch.setFormatter(formatter)
                self.logger.addHandler(ch)
            if WITH_LOG_FILE:
                # 创建一个handler，用于写入日志文件
                log_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/logs/'
                if not os.path.exists(log_path):
                    os.makedirs(log_path) 
                logfile = log_path + time.strftime('%Y%m%d', time.localtime(time.time())) + '_out.log'
                # 创建一个handler，用于写入日志文件
                fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')  # 不拆分日志文件，a指追加模式,w为覆盖模式
                fh.setLevel(LOG_LEVEL_FILE)  # 输出到file的log等级的开关
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)

    @property
    def get_log(self):
        """定义一个函数，回调logger实例"""
        return self.logger


log = Logger().get_log
