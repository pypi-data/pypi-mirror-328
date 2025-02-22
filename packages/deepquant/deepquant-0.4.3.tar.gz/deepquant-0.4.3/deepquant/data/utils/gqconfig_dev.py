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
server_dev: Dict[str, object] = dict(protocol='http',
                                     host='10.4.47.17', port='8000',
                                     wshost='10.4.47.17', wsport='8000',
                                     verify_ssl=False)

log_dev: Dict[str, object] = dict(level=logging.INFO,
                                  console=True,
                                  file=True)

switch_dev: Dict[str, object] = dict(debug='1')

if 'dev' == ENV:
    print('update_config env =', ENV)
    configs.update_config('server', server_dev)
    configs.update_config('log', log_dev)
    configs.update_config('switch', switch_dev)
