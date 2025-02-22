#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: zhangluping_it
@time: 2024/7/15 11:18
@description:  此配置不打包到sdk中
"""
import logging
from typing import Dict
from .gqconfig import configs
from .gqconfig import ENV

# 环境配置项
#if ENV != 'test':
#    server_hub: Dict[str, object] = dict(protocol='http',
#                                     host='10.4.47.17', port='8000',
#                                     wshost='10.4.47.17', wsport='8000',
#                                     verify_ssl=False)
#else:
server_hub: Dict[str, object] =  dict(protocol='http',
                                      host='apisix.tsxcph.chinastock.com.cn', port='80',
                                      wshost='apisix.tsxcph.chinastock.com.cn', wsport='80',
                                      verify_ssl=False)



log_hub: Dict[str, object] = dict(level=logging.WARN,
                                  console=True,
                                  file=False)

switch_hub: Dict[str, object] = dict(debug='0')


def key_to_encrypt(app_key):
    """
    对于hub中，增加一步判断app_key是否为sha256之后结果，如果是，则不再做加密
    """
    if app_key is not None and len(app_key) == 64:
        try:
            int(app_key, 16)
            return False
        except ValueError as e:
            print(e)
            return True
    else:
        return True


#if 'hub' == ENV:
    #print('update_config env =', ENV)
    #configs.update_config('server', server_hub)
    #configs.update_config('log', log_hub)
    #configs.update_config('switch', switch_hub)
    #configs.key_to_encrypt = key_to_encrypt
