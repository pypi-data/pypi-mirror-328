#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from enum import Enum


class DataType(Enum):
    """
    返回数据类型
    """
    DATAFRAME = 0  #: 返回dataframe
    JSON = 10  #: 返回json，如[{'symbol':'SH600000','price':10.0},{'symbol':'SZ000001','price':10.0}]
    PROTO_BUF = 11  #: 返回数据为protocol buffer

    @staticmethod
    def get(name='', code=''):
        for item in DataType:
            if name is not None and item.name == name:
                return item
            elif code is not None and item.value == code:
                return code
        return DataType.JSON


class ApiReqMethod(Enum):
    """
    API请求类型：POST、GET
    """
    POST = 0
    GET = 1

    @staticmethod
    def get(name='', code=''):
        for item in ApiReqMethod:
            if name is not None and item.name == name:
                return item
            elif code is not None and item.value == code:
                return item
        return ApiReqMethod.POST


class ApiEncrypt(Enum):
    """
    API是否加密：不加密/请求相应加密/...
    """
    NO = 0
    # TODO 加解密功能待实现
    ENCRY_REQ_RSP = 10

    @staticmethod
    def get(name='', code=''):
        for item in ApiEncrypt:
            if name is not None and item.name == name:
                return item
            elif code is not None and item.value == code:
                return item
        return ApiEncrypt.NO


class ApiRspCode(Enum):
    SUCCESS = '00000'
    HTTP_ERROR = 'H0001'
    HTTP_TIMEOUT = 'H0002'
    # HTTP返回码如果是非200，则错误码为HC404之类
    HTTP_ERRCODE_PRE = 'HC{}'

    NOT_AUTH = 'U0404'

    PARAM_ERROR = 'P0001'

    RSP_ERROR = 'RT999'

    SDK_ERROR = 'SDK99'

    @staticmethod
    def is_succ(code):
        if ApiRspCode.SUCCESS == code or ApiRspCode.SUCCESS.value == code or 200 == code or 0 == code or '0' == code:
            return True
        else:
            return False


class ApiAggregateType(Enum):
    # 不需要聚合
    NO = 0
    # 分批聚合
    BATCH = 1

    # 分页聚合，TODO，本期暂不实现

    @staticmethod
    def get(name='', code=''):
        for item in ApiAggregateType:
            if name is not None and item.name == name:
                return item
            elif code is not None and item.value == code:
                return item
        return ApiAggregateType.NO


class ApiRspMode(Enum):
    # 处理后返回，默认选项
    PROCESSED = 0
    # 透传
    PASSED = 1


class ApiResponse:
    """
    Api响应返回对象
    """

    def __init__(self, code, msg, data, **kwargs):
        """
        :param code:    返回码，0-成功，其他相关错误码
        :param msg:     返回提示
        :param data:    返回数据
        """
        self.code = code
        self.msg = msg
        self.data = data
        self.extra = kwargs

    @staticmethod
    def assemble_succ_resp(data, **kwargs):
        response = ApiResponse(code=ApiRspCode.SUCCESS, msg='success', data=data, **kwargs)
        return response

    @staticmethod
    def assemble_err_resp(code, msg):
        response = ApiResponse(code=code, msg=msg, data=None)
        return response

    def is_success(self):
        return ApiRspCode.is_succ(self.code)

    def __str__(self):
        _str = self.__class__.__name__ + '(' + \
               ','.join([key + '=' + str(value) for key, value in self.__dict__.items() if value is not None]) \
               + ')'
        return _str


class ApiInfo:
    def __init__(self, mod_type, func_name, api_uri,
                 req_method=ApiReqMethod.POST.name,
                 req_data_type=DataType.JSON.name,
                 rsp_data_type=DataType.JSON.name,
                 ret_data_node=None,
                 aggregate_type=ApiAggregateType.NO.name,
                 encrypt_type=ApiEncrypt.NO.name,
                 extras=None, comment=None):
        """
        HTTP API信息
        :param mod_type:    API所属模块类型，比如数据-Data、因子-Factor
        :param func_name:     API的唯一名称，模块内唯一，比如getBars
        :param api_uri:     API对应网关的URI
        :param req_method:  请求方式
        :param req_data_type:   请求数据格式
        :param rsp_data_type:   响应数据格式
        :param ret_data_node:   返回数据的节点，比如返回json或pb根目录下的datas

        :param aggregate_type:      是否需要批量聚合，0-不需要，1-分批聚合，2-分页聚合
        :param encrypt_type:      加解密类型
        :param extras:          扩展字段，作为预留
        """
        # API类型，比如data/factor...
        self.mod_type = mod_type
        self.func_name = func_name
        self.api_uri = api_uri
        self.req_method = ApiReqMethod.get(req_method)
        self.req_data_type = DataType.get(req_data_type)
        self.rsp_data_type = DataType.get(rsp_data_type)
        self.ret_data_node = ret_data_node

        # 分批聚合功能已支持
        self.aggregate_type = ApiAggregateType.get(aggregate_type)
        self.encrypt_type = ApiEncrypt.get(encrypt_type)
        self.extras = extras
        self.comment = comment

    @staticmethod
    def gen_from_json_item(_json_config):
        mod_type = _json_config.get('modType')
        if mod_type is None:
            mod_type = _json_config.get('mod_type')

        func_name = _json_config.get('funcName')
        if func_name is None:
            func_name = _json_config.get('func_name')

        api_uri = _json_config.get('apiUri')
        if api_uri is None:
            api_uri = _json_config.get('api_uri')

        req_method = _json_config.get('reqMethod')
        if req_method is None:
            req_method = _json_config.get('req_method')

        req_data_type = _json_config.get('reqDataType')
        if req_data_type is None:
            req_data_type = _json_config.get('req_data_type')

        rsp_data_type = _json_config.get('rspDataType')
        if rsp_data_type is None:
            rsp_data_type = _json_config.get('rsp_data_type')

        ret_data_node = _json_config.get('retDataNode')
        if ret_data_node is None:
            ret_data_node = _json_config.get('ret_data_node')

        encrypt_type = _json_config.get('encryptType')
        if encrypt_type is None:
            encrypt_type = _json_config.get('encrypt_type')

        comment = _json_config.get('remark')
        if comment is None:
            comment = _json_config.get('comment')

        return ApiInfo(mod_type=mod_type, func_name=func_name, api_uri=api_uri, req_method=req_method,
                       req_data_type=req_data_type, rsp_data_type=rsp_data_type, ret_data_node=ret_data_node,
                       encrypt_type=encrypt_type,
                       comment=comment)

    @staticmethod
    def default(mod_type, func_name, api_uri, method="POST"):
        return ApiInfo(mod_type=mod_type, func_name=func_name, api_uri=api_uri, req_method=method)

    def set_req_method(self, req_method):
        self.req_method = req_method
        return self

    def set_data_type(self, data_type):
        self.req_data_type = data_type
        self.rsp_data_type = data_type
        return self

    def set_ret_data_node(self, ret_data_node):
        self.ret_data_node = ret_data_node
        return self

    def has_data_node(self):
        if self.ret_data_node is not None and len(self.ret_data_node) > 0:
            return True
        else:
            return False

    def __str__(self):
        _str = self.__class__.__name__ + '(' + \
               ','.join([key + '=' + str(value) for key, value in self.__dict__.items() if value is not None]) \
               + ')'
        return _str


class TTLCache(object):
    """
    TTL缓存，用于token缓存等
    """
    NOT_FOUND = None

    def __init__(self):
        # 记录key-value数据
        self.datas = dict()
        # 记录key-expire失效时间
        self.expires = dict()

    def check_and_remove_key_expires(self, key):
        if key in self.datas:
            if key in self.expires:
                now = time.time()
                expire_time = self.expires[key]
                if expire_time > now:
                    # 超时时间>当前时间，则返回数据
                    return self.datas[key]
                else:
                    print('[check_key_expires]key-expired:' + key + ', ' + self.datas[key])
                    del self.datas[key]
                    del self.expires[key]
                    return TTLCache.NOT_FOUND
            else:
                del self.datas[key]
                return TTLCache.NOT_FOUND
        else:
            return TTLCache.NOT_FOUND

    def get(self, key):
        return self.check_and_remove_key_expires(key)

    def set(self, key, value, ttl=86400):
        now = time.time()
        self.datas[key] = value
        self.expires[key] = now + ttl


class FunctionMode(Enum):
    # 无上传参数模式
    SIMPLE = 1
    # 无上传参数模式
    COMPLEX = 2