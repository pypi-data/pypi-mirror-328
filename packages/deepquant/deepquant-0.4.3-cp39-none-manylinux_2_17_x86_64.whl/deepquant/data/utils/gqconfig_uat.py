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

# UAT互联网环境配置项
server_uat: Dict[str, object] = dict(protocol='https',
                                     host='unitetest.chinastock.com.cn', port='8005',
                                     wshost='unitetest.chinastock.com.cn', wsport='8005',
                                     verify_ssl=True)

log_uat: Dict[str, object] = dict(level=logging.INFO,
                                  console=False,
                                  file=True)

switch_uat: Dict[str, object] = dict(debug='0')

if 'uat' == ENV:
    print('update_config env =', ENV)
    configs.update_config('server', server_uat)
    configs.update_config('log', log_uat)
    configs.update_config('switch', switch_uat)
