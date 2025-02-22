#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: zhangluping_it
@time: 2024/7/15 11:18
@description: 
"""
import logging
from typing import Dict
from .gqconfig import configs
from .gqconfig import ENV

# 环境配置项
server_test: Dict[str, object] = dict(protocol='http',
                                      host='apisix.prodxc.chinastock.com.cn', port='80',
                                      wshost='apisix.prodxc.chinastock.com.cn', wsport='80',
                                      verify_ssl=False)

log_test: Dict[str, object] = dict(level=logging.INFO,
                                   console=False,
                                   file=True)

switch_test: Dict[str, object] = dict(debug='0')

if 'prod' == ENV:
    print('update_config env =', ENV)
    configs.update_config('server', server_test)
    configs.update_config('log', log_test)
    configs.update_config('switch', switch_test)
