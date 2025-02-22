#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: zhangluping_it
@time: 2024/7/15 11:18
@description: 
"""
import logging
import os

from typing import Dict, Optional

# 默认配置项
server_default: Dict[str, object] =  dict(protocol='https',
                                      host='deepquant.chinastock.com.cn', port='443',
                                      wshost='deepquant.chinastock.com.cn', wsport='443',
                                      verify_ssl=True,
                                      key_encrypt=True)

log_default: Dict[str, object] = dict(level=logging.WARN,
                                      console=True,
                                      file=False)

switch_default: Dict[str, object] = dict(debug='0')


class ConfigMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Configs(metaclass=ConfigMeta):

    def __init__(self):
        self.c_server = {}
        self.c_log = {}
        self.c_switch = {}
        self._configs = {}

    def load_config(self):
        self.c_server.update(server_default)
        self.c_log.update(log_default)
        self.c_switch.update(switch_default)

        self._configs['server'] = self.c_server
        self._configs['log'] = self.c_log
        self._configs['switch'] = self.c_switch

    def update_config(self, config_name, config_dict):
        _config = getattr(self, 'c_' + config_name)
        if _config is not None:
            _config.update(config_dict)

        self._configs[config_name] = config_dict

    def get_server_http_url(self) -> str:
        """
        获取服务器http地址
        """
        protocol = self.c_server.get('protocol')
        if protocol is None:
            protocol = 'https'
        host = self.c_server.get('host')
        port = self.c_server.get('port')
        if host is None:
            raise Exception('服务host未配置')
        if port is None:
            raise Exception('服务port未配置')
        server_url = '{}://{}:{}'.format(protocol, host, port)
        return server_url

    def get_server_ws(self) -> str:
        """
        获取服务器websocket连接地址
        """
        protocol = self.c_server.get('protocol')
        if protocol is None:
            protocol = 'https'
        ws_protocol = 'wss'
        if protocol == 'http':
            ws_protocol = 'ws'

        wshost = self.c_server.get('wshost')
        wsport = self.c_server.get('wsport')
        if wshost is None:
            raise Exception('服务wshost未配置')
        if wsport is None:
            raise Exception('服务wsport未配置')
        server_url = '{}://{}:{}'.format(ws_protocol, wshost, wsport)
        return server_url

    def is_verify_ssl(self) -> bool:
        is_verify = self.c_server.get('verify_ssl')
        if is_verify is not None and False == is_verify:
            return False
        else:
            return True

    @staticmethod
    def key_to_encrypt(app_key) -> bool:
        return True

    def get_log_config(self) -> [int, bool, bool]:
        """
        @returns : logging.level, is_log_console, is_log_file
        """
        log_config = [logging.WARN, True, False]
        level = self.get('log.level')
        is_log_console = self.get('log.console')
        is_log_file = self.get('log.file')
        if level is not None:
            log_config[0] = level
        if is_log_console is not None:
            log_config[1] = is_log_console
        if is_log_file is not None:
            log_config[2] = is_log_file
        print('log_config', log_config)
        return log_config

    def is_debug(self) -> bool:
        is_debug = self.get('switch.debug')
        if is_debug is not None and '1' == is_debug:
            return True
        else:
            return False

    def get(self, get_key, query_level=0, config_dict=None):
        conf_keys = get_key.split('.')
        if len(conf_keys) > 1:
            if query_level >= len(conf_keys):
                return None
            else:
                conf_key = get_key.split('.')[query_level]
        else:
            conf_key = get_key
        if config_dict is None:
            config_dict = self._configs
        if conf_key in config_dict:
            value = config_dict.get(conf_key)
            if get_key == conf_key:
                return value
            elif query_level == len(get_key.split('.')) - 1:
                return value
            elif isinstance(value, dict):
                return self.get(get_key, query_level + 1, value)
            else:
                return None
        else:
            return None


def reload_config(_env=None):
    global ENV
    global configs
    configs.load_config()
    if _env is not None:
        ENV = _env
    if ENV is not None:
        ENV = ENV.lower()
        print('load config env =', ENV)
        try:
            #if 'hub' == ENV:
            #    from . import gqconfig_hub
            if 'prod' == ENV:
                from . import gqconfig_prod
            elif 'inner' == ENV:
                from . import gqconfig_inner 
            elif 'uat' == ENV:
                from . import gqconfig_uat
            elif 'test' == ENV:
                from . import gqconfig_test
            elif 'dev' == ENV:
                from . import gqconfig_dev
        except Exception as e:
            print(e)


ENV = os.getenv('deepquantsdk_env')
configs = Configs()
configs.load_config()
reload_config()
# load param from jupyterhub
#UP_EXEC_ENV = ENV if ENV else None
#if UP_EXEC_ENV is None:
#    UP_EXEC_ENV = os.getenv('UP_EXEC_ENV')
UP_EXEC_ENV = os.getenv('UP_EXEC_ENV')
if UP_EXEC_ENV is not None and 'jupyterhub' == UP_EXEC_ENV:
    #reload_config('hub')
    print(f'UP_EXEC_ENV=="{UP_EXEC_ENV}"')
    from . import gqconfig_hub
    configs.key_to_encrypt = gqconfig_hub.key_to_encrypt

