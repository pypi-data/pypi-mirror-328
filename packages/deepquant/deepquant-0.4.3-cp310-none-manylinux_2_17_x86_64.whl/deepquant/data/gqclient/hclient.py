#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
import traceback

from google.protobuf.message import Message
import requests
import json
import pandas as pd
from itertools import chain

from .commons import ApiInfo, DataType, ApiReqMethod, ApiRspCode, ApiEncrypt, ApiResponse, TTLCache, ApiRspMode
from ..utils.log_writer import log
from ..utils.gqconfig import configs
from ..utils import encrypt_util
from ..proto import proto_utils, common_pb2

func_getToken = 'getToken'
func_querySdkApis = 'querySdkApis'
_is_debug = configs.is_debug()

default_apis = {
    func_getToken: ApiInfo('sdk', func_getToken, "/gid/sdk/api/get-token", ret_data_node='data'),
    func_querySdkApis: ApiInfo('sdk', func_querySdkApis, "/gid/sdk/api/query-all", ret_data_node='data'),
}

global_cache = TTLCache()


class GidHClient:
    """
    Http请求客户端
    """

    def __init__(self, req_cache=None):
        if req_cache is None:
            self.cache = global_cache
        else:
            self.cache = req_cache
        self.session = requests.session()
        self.user_id = None
        self.app_key = None
        self.api_host = None
        self.verify_ssl = True
        self.api_configs = default_apis
        self.is_init = False

    def init(self, user_id=None, app_key=None) -> [bool, str]:
        """
        client初始化
        :return
        """
        if user_id is None:
            return False, '传入用户为空'
        self.user_id = user_id
        if app_key is not None:
            self.app_key = app_key
        # 从配置获取
        self.api_host = configs.get_server_http_url()
        self.verify_ssl = configs.is_verify_ssl()
        # 获取token
        token_rsp = self.get_token()
        if not token_rsp.is_success():
            # token获取失败，则函数跳出
            log.error('init-获取Token失败, user_id=%s, code=%s, msg=%s, token_rsp=%s',
                      self.user_id, token_rsp.code, token_rsp.msg, token_rsp)
            return False, token_rsp.msg
        # 获取api信息
        self._update_apis()
        self.is_init = True
        return True, '初始化完成'

    def get_key(self):
        if not configs.key_to_encrypt(self.app_key):
            return self.app_key
        else:
            encrypt_key = encrypt_util.encrypt(self.app_key)
            return encrypt_key

    def _update_apis(self):
        data, code, msg = self.post(func_querySdkApis, json.dumps({"userId": self.user_id}), df=False)
        if ApiRspCode.is_succ(code):
            for _api_data in data:
                api_info = ApiInfo.gen_from_json_item(_api_data)
                self.api_configs[api_info.func_name] = api_info
            log.info("[API初始化]完成 %s", self.api_configs.keys())
        else:
            log.error("[API初始化]失败 code=%s, msg=%s, data=%s", code, msg, data)

    def get_token(self) -> ApiResponse:
        """
        获取token
        """
        cache_key = f'jwt_token#{self.user_id}'
        # 先查询缓存
        token = self.cache.get(cache_key)
        if token is not None and len(token) > 0:
            self.session.headers['authorization'] = token
            log.info("[get_token]with-cache-%s", token)
            return ApiResponse.assemble_succ_resp(token)
        api_rsp = self.post_rsp(func_getToken, params={'user-id': self.user_id, 'app-key': self.get_key()},
                                df=False)
        if api_rsp.is_success() and api_rsp.data is not None and len(api_rsp.data) > 0:
            token = api_rsp.data
            self.cache.set(cache_key, token, 10 * 60)
            self.session.headers['authorization'] = token
            log.info("[get_token]finish-%s", token)
        else:
            log.error("[get_token]failed-%s", api_rsp)
        return api_rsp

    def post_rsp(self, func_name, params=None, query_params=None,
                 fields=None, df=False, batch=None,
                 timeout=600,
                 req_pb_class=None, rsp_pb_class=None,
                 rsp_mode=ApiRspMode.PROCESSED) -> ApiResponse:
        t_dict = {'t_req_1': time.time()}
        """
        params传入dict类型；
        传输协议：目前支持json格式HTTP接口、pb格式数据接口，对应'application/x-protobuf'和'application/json'

        :param func_name: api唯一标识，比如query_his_bar，同配置文件中对应
        :param params: 查询参数列表，具体字段由数据接口定义，格式如{'symbol':'SH600000','beginDate':'20210101'}
        :param query_params: 用于传入放置在Query Parameters（即URL）中参数，传入dict类型
        :param fields: 查询字段数组，比如['price','vol']
        :param df: 返回数据类型，是否为df，true为df，false为list/dict等基础对象
        :param batch: 批量查询请求参数，如 "batch": {"req_id": "1", "offset": "0", "limit": 1000}
        :param timeout: 超时时间，单位秒，默认30秒
        :returns:   目前采用三元组方式返回数据
            :return: data: 返回查询数据
            :return: code: 返回码
            :return: msg: 返回消息
        """
        api_info = self.api_configs.get(func_name)
        if api_info is None:
            log.error('[%s]-请求失败! 函数请求未授权，未获取到该函数名', func_name)
            return ApiResponse.assemble_err_resp(ApiRspCode.NOT_AUTH, func_name + '函数请求未授权')

        # 生成trace_id
        trace_id = get_uid()
        log.info("[%s]-start, trace_id=%s, path=%s, params=%s, query_params=%s, fields=%s, df=%s, batch=%s,"
                 " req_pb_class=%s, rsp_pb_class=%s",
                 func_name, trace_id, api_info.api_uri, params, query_params, fields, df, batch,
                 req_pb_class, rsp_pb_class)
        # 先获取token
        if func_name != func_getToken:
            token_rsp = self.get_token()
            if not token_rsp.is_success():
                # token获取失败，则函数跳出
                log.error('[%s]-请求失败! 获取Token失败, code=%s, msg=%s, token_rsp=%s',
                          token_rsp.code, token_rsp.msg, token_rsp)
                return ApiResponse.assemble_err_resp(ApiRspCode.NOT_AUTH, func_name + '函数请求未授权')
        headers = self.session.headers.copy()
        headers['trace_id'] = trace_id
        # 请求数据类型转换
        try:
            if params is None:
                params = {}
            if batch is not None and isinstance(batch, dict):
                # 处理分批请求
                if isinstance(params, dict) and 'batch' in params:
                    # 参数中已经带了batch数据，则进行更新
                    params.get('batch').update(batch)
                else:
                    # batch的规范为 {'batch':{}, 'params':{}}
                    params = {'batch': batch, 'params': params}
            if DataType.PROTO_BUF.name == api_info.req_data_type.name:
                if isinstance(params, Message):
                    # 直接传入PB对象
                    req = params
                else:
                    # 传入dict，则需显示传入PB对象，进行转换
                    if req_pb_class is None:
                        log.error('[%s]-请求失败! 传入PB定义为空', func_name)
                        return ApiResponse.assemble_err_resp(ApiRspCode.PARAM_ERROR, func_name + '传入PB定义为空')
                    req = proto_utils.convert_req2protobuf(req_pb_class,
                                                           params_dict=params)
                # 请求数据转PB二进制
                _binary_str = req.SerializeToString()
                params = _binary_str
                headers['Content-Type'] = 'application/x-protobuf'
                # 设置接受的返回数据类型
                headers['Accept'] = 'application/x-protobuf'
            else:
                headers['Content-Type'] = 'application/json'
        except Exception as param_err:
            log.error(
                "[%s]-请求失败! HTTP请求参数异常, trace_id=%s, path=%s, params=%s, fields=%s, df=%s, http_error=%s",
                func_name, trace_id, api_info.api_uri, params, fields, df, param_err)
            return ApiResponse.assemble_err_resp(ApiRspCode.PARAM_ERROR, '请求参数错误{}'.format(param_err))

        # TODO 加解密功能
        # 发起http请求
        try:
            t_dict['t_req_2'] = time.time()
            if api_info.req_method.name == ApiReqMethod.GET.name:
                response = self.session.get(self.api_host + api_info.api_uri,
                                            params=params, headers=headers, timeout=timeout,
                                            verify=self.verify_ssl)
            else:
                if isinstance(params, dict):
                    if query_params is not None:
                        response = self.session.post(self.api_host + api_info.api_uri,
                                                     params=query_params,
                                                     json=params, headers=headers, timeout=timeout,
                                                     verify=self.verify_ssl)
                    else:
                        response = self.session.post(self.api_host + api_info.api_uri,
                                                     json=params, headers=headers, timeout=timeout,
                                                     verify=self.verify_ssl)
                else:
                    response = self.session.post(self.api_host + api_info.api_uri,
                                                 data=params, headers=headers, timeout=timeout,
                                                 verify=self.verify_ssl)
        except (requests.exceptions.HTTPError,
                requests.exceptions.ConnectionError,
                requests.exceptions.RequestException) as http_error:
            log.error("[%s]-请求失败! HTTP请求异常, trace_id=%s, path=%s, params=%s, fields=%s, df=%s, http_error=%s",
                      func_name, trace_id, api_info.api_uri, params, fields, df, http_error)
            traceback.print_exc()
            return ApiResponse.assemble_err_resp(ApiRspCode.HTTP_ERROR, 'HTTP请求异常{}'.format(http_error))
        except requests.exceptions.Timeout as timeout_error:
            log.error("[%s]-请求失败! HTTP请求异常, trace_id=%s, path=%s, params=%s, fields=%s, timeout_error=%s",
                      func_name, trace_id, api_info.api_uri, params, fields, df, timeout_error)
            return ApiResponse.assemble_err_resp(ApiRspCode.HTTP_TIMEOUT, 'HTTP请求超时')
        t_dict['t_rsp_1'] = time.time()
        log.info("[%s]-httpresp, trace_id=%s, path=%s, params=%s, fields=%s, df=%s",
                 func_name, trace_id, api_info.api_uri, params, fields, df)
        # 判断返回码
        if response.status_code != 200:
            trace_http_log(response)
            log.error(
                "[%s]-请求失败! HTTP请求异常, trace_id=%s, path=%s, params=%s, fields=%s, df=%s, code_error=%s, text=%s",
                func_name, trace_id, api_info.api_uri, params, fields, df, response.status_code, response.text)
            return _parse_http_error_meta(response)
        elif _is_debug:
            # TODO 仅开发环境进行追踪
            trace_http_log(response)
        # 获取返回数据类型
        _rsp_data_type = self._get_data_type_resp(api_info, response.headers)
        try:
            # 处理对应数据类型，并根据需要的返回类型确定返回dataframe还是json
            _api_response = self._convert_resp(_rsp_data_type,
                                               api_info,
                                               response,
                                               df, fields, batch, t_dict,
                                               rsp_pb_class,
                                               rsp_mode)
        except Exception as e:
            traceback.print_exc()
            log.error(
                "[%s]-请求失败! HTTP响应解析失败, trace_id=%s, path=%s, params=%s, fields=%s, df=%s, code_error=%s, text=%s, e=%s",
                func_name, trace_id, api_info.api_uri, params, fields, df, response.status_code, response.text, e)
            return ApiResponse.assemble_err_resp(ApiRspCode.RSP_ERROR, '响应报文解析失败!{}'.format(type(e).__name__))
        if _is_debug:
            cal_timestamp(t_dict, response.headers)
        if _api_response.is_success():
            log.info("[%s]-请求完成, trace_id=%s, path=%s, params=%s, fields=%s, df=%s,",
                     func_name, trace_id, api_info.api_uri, params, fields, df)
        else:
            log.error("[%s]-请求失败! 请求报错, trace_id=%s, path=%s, params=%s, fields=%s, df=%s, _api_response=%s",
                      func_name, trace_id, api_info.api_uri, params, fields, df, _api_response)
        if _is_debug:
            _api_response.extra['t_dict'] = t_dict
        return _api_response

    def post(self, func_name, params=None, query_params=None,
             fields=None, df=False, batch=None,
             timeout=600,
             req_pb_class=None, rsp_pb_class=None,
             rsp_mode=ApiRspMode.PROCESSED):
        """
        返回三元组
        """
        _api_response = self.post_rsp(func_name=func_name, params=params, query_params=query_params,
                                      fields=fields, df=df, batch=batch, timeout=timeout,
                                      req_pb_class=req_pb_class, rsp_pb_class=rsp_pb_class,
                                      rsp_mode=rsp_mode)
        if _api_response.is_success():
            _data = _api_response.data
            return _data, _api_response.code, _api_response.msg
        else:
            return None, _api_response.code, _api_response.msg

    def post_batch(self, func_name, params=None, query_params=None,
                   fields=None, df=False, need_batch=False, limit=100000,
                   timeout=600,
                   req_pb_class=None, rsp_pb_class=None):
        """
        返回三元组
        """
        req_id = get_uid()
        if limit is None or limit <= 0:
            limit = 100000
        batch = {"req_id": req_id, "offset": "", "limit": limit}
        if not need_batch:
            return self.post(func_name=func_name, params=params, query_params=query_params,
                             fields=fields, df=df, timeout=timeout, batch=batch,
                             req_pb_class=req_pb_class, rsp_pb_class=rsp_pb_class)
        else:
            result_cache = []
            _last_batch = None
            _last_api_rsp = None
            query_limit = 10000
            while query_limit > 0:
                query_limit = query_limit - 1
                # 聚合接口默认先不转df
                _last_api_rsp = self.post_rsp(func_name=func_name, params=params, query_params=query_params,
                                              fields=fields, df=df, timeout=timeout, batch=batch,
                                              req_pb_class=req_pb_class, rsp_pb_class=rsp_pb_class)
                #_last_api_rsp.data.to_csv(f'{batch["req_id"]}_{batch["offset"]}_{batch["limit"]}.csv')
                if not _last_api_rsp.is_success():
                    break
                result_cache.append(_last_api_rsp.data)
                if 'batch' in _last_api_rsp.extra:
                    _batch_rsp = _last_api_rsp.extra['batch']
                    if 'is_end' in _batch_rsp and _batch_rsp['is_end'] == True:
                        _last_batch = _batch_rsp
                        break
                    if 'isEnd' in _batch_rsp and _batch_rsp['isEnd'] == True:
                        _last_batch = _batch_rsp
                        break
                    if 'last_offset' in _batch_rsp:
                        batch['offset'] = _batch_rsp['last_offset']
                    elif 'lastOffset' in _batch_rsp:
                        batch['offset'] = _batch_rsp['lastOffset']
                    else:
                        print(_batch_rsp)
                else:
                    break
            # 结果集集合
            if result_cache is None:
                _last_api_rsp.data = None
            elif len(result_cache) == 1:
                _last_api_rsp.data = result_cache[0]
            elif len(result_cache) > 1:
                if isinstance(result_cache[0], list):
                    aggr_result = list(chain(*result_cache))
                    _last_api_rsp.data = aggr_result
                elif isinstance(result_cache[0], pd.DataFrame):
                    aggr_df = pd.concat(result_cache)
                    _last_api_rsp.data = aggr_df
                else:
                    _last_api_rsp = ApiResponse.assemble_err_resp(ApiRspCode.SDK_ERROR,
                                                                  "数据聚合未处理:{}".format(type(result_cache[0])))
            if _last_api_rsp.is_success():
                _data = _last_api_rsp.data
                if df and not isinstance(_data, pd.DataFrame):
                    _data = GidHClient._convert_resp2df(_data, fields)
                return _data, _last_api_rsp.code, _last_api_rsp.msg
            else:
                return None, _last_api_rsp.code, _last_api_rsp.msg

    @staticmethod
    def _get_data_type_resp(apiinfo, headers):
        """
        根据配置的api信息和响应的http.headers信息，返回http返回的数据类型
        """
        # 先根据headers判断
        content_type = _get_http_content_type(headers)
        if 'application/x-protobuf' in content_type:
            return DataType.PROTO_BUF
        elif 'application/json' in content_type:
            return DataType.JSON
        else:
            return apiinfo.rsp_data_type

    @staticmethod
    def _convert_resp(data_type, api_info, response, is_df, fields, batch, t_dict, rsp_pb_class,
                      rsp_mode) -> ApiResponse:
        """
        将返回对象（JSON、PB）统一转成python基础对象（dict、list等）
        """
        if t_dict is None:
            t_dict = {}
        if DataType.JSON.name == data_type.name:
            _rsp_obj = json.loads(response.text)
            t_dict['t_rsp_parsed'] = time.time()
            if ApiRspMode.PASSED == rsp_mode:
                return ApiResponse.assemble_succ_resp(_rsp_obj)
            # 获取对应的数据节点
            _api_rsp = GidHClient._parse_data_node(_rsp_obj, api_info.ret_data_node, batch)
            if is_df and _api_rsp.data is not None:
                # 转dataframe
                _api_rsp.data = GidHClient._convert_resp2df(_api_rsp.data, fields)
                t_dict['t_rsp_framed'] = time.time()
                return _api_rsp
            else:
                # 不返回df则直接返回
                return _api_rsp
        elif DataType.PROTO_BUF.name == data_type.name:
            if rsp_pb_class is None:
                log.error('[convert_resp_content] %s 未传入响应PB数据结构', api_info.func_name)
                raise Exception('未传入响应PB数据结构')
            if ApiRspMode.PASSED == rsp_mode:
                _ps_ins = proto_utils.convert_resp_proto2ins(rsp_pb_class, response.content)
                return ApiResponse.assemble_succ_resp(_ps_ins)
            #  TODO
            if rsp_pb_class == common_pb2.CommonTableRes:
                _pb_ins = proto_utils.convert_resp_proto2ins(rsp_pb_class, response.content)
                _api_rsp = GidHClient._parse_data_node(_pb_ins, api_info.ret_data_node, batch)
                _table_values = proto_utils.convert_result_table_values(_pb_ins.data)
                print(_api_rsp)
                return _api_rsp
            else:
                _pb_dict = proto_utils.convert_resp_proto2dict(rsp_pb_class, response.content)
                _api_rsp = GidHClient._parse_data_node(_pb_dict, api_info.ret_data_node, batch)
                t_dict['t_rsp_parsed'] = time.time()
                if is_df and _api_rsp.data is not None:
                    # 转dataframe
                    _api_rsp.data = GidHClient._convert_resp2df(_api_rsp.data, fields)
                    t_dict['t_rsp_framed'] = time.time()
                return _api_rsp
        else:
            t_dict['t_rsp_parsed'] = time.time()
            return ApiResponse.assemble_succ_resp(response.text)

    @staticmethod
    def _convert_resp2df(_rsp_obj, _fields):
        _columns = None
        if _fields is not None and len(_fields) > 0:
            _columns = _fields
        if isinstance(_rsp_obj, dict):
            df = pd.DataFrame.from_dict(_rsp_obj, orient='index', columns=_columns)
            # df = df.convert_dtypes()
            return df
        else:
            df = pd.DataFrame(_rsp_obj, columns=_columns)
            # df = df.convert_dtypes()
            return df

    @staticmethod
    def _parse_data_node(_dict_obj, _data_node, batch=None, meta_node='meta') -> ApiResponse:
        if _data_node is None or len(_data_node) == 0:
            return ApiResponse.assemble_succ_resp(_dict_obj)
        if isinstance(_dict_obj, dict):
            if meta_node in _dict_obj:
                # 校验响应数据的meta元数据，判断返回码；没有meta，则不校验meta元数据
                _meta = _dict_obj.get(meta_node)
                _meta_code = _meta.get('code')
                if 'success' in _meta and _meta['success'] != True:
                    return ApiResponse.assemble_err_resp(_meta_code, _meta.get('message'))
                if _meta_code is not None and not ApiRspCode.is_succ(_meta_code) and '0' != _meta_code:
                    return ApiResponse.assemble_err_resp(_meta_code, _meta.get('message'))
            if _data_node in _dict_obj:
                if batch is not None and 'batch' in _dict_obj:
                    return ApiResponse.assemble_succ_resp(_dict_obj[_data_node], batch=_dict_obj['batch'])
                else:
                    return ApiResponse.assemble_succ_resp(_dict_obj[_data_node])
            else:
                log.error('[_get_data_node] _dict_obj= %s 无 %s 属性', _dict_obj, _data_node)
                return ApiResponse.assemble_succ_resp({})
        elif isinstance(_dict_obj, Message):
            if hasattr(_dict_obj, meta_node):
                # 校验响应数据的meta元数据，判断返回码；没有meta，则不校验meta元数据
                _meta = getattr(_dict_obj, meta_node)
                _meta_code = getattr(_meta, 'code')
                if hasattr(_meta, 'success') and getattr(_meta, 'success') != True:
                    return ApiResponse.assemble_err_resp(_meta_code, getattr(_meta, 'message'))
                if _meta_code is not None and not ApiRspCode.is_succ(_meta_code) and '0' != _meta_code:
                    return ApiResponse.assemble_err_resp(_meta_code, getattr(_meta, 'message'))
            if hasattr(_dict_obj, _data_node):
                if batch is not None and hasattr(_dict_obj, 'batch'):
                    return ApiResponse.assemble_succ_resp(getattr(_dict_obj, _data_node),
                                                          batch=getattr(_dict_obj, 'batch'))
                else:
                    return ApiResponse.assemble_succ_resp(getattr(_dict_obj, _data_node))
            else:
                log.error('[_get_data_node] _dict_obj= %s 无 %s 属性', _dict_obj, _data_node)
                return ApiResponse.assemble_succ_resp({})
        else:
            # 不是字典，则不取子节点
            return ApiResponse.assemble_succ_resp(_dict_obj)


def _get_http_content_type(_headers):
    """
    获取http headers中的Content-Type
    """
    _content_type = None
    if 'Content-Type' in _headers:
        _content_type = _headers.get('Content-Type')
    elif 'content-type' in _headers:
        _content_type = _headers.get('content_type').lower()
    else:
        for _header in _headers:
            if 'content_type' == _header.lower():
                _content_type = _headers[_header]
    if _content_type is not None:
        return _content_type.lower()
    else:
        return None


def get_uid():
    return f'{int(time.time() * 1000000)}.{random.randrange(0, 1000)}'


def _parse_http_error_meta(http_response, meta_node='meta', msg_node='message') -> ApiResponse:
    _rsp_text = http_response.text
    if isinstance(_rsp_text, str) and meta_node in _rsp_text and msg_node in _rsp_text:
        try:
            _dict_obj = json.loads(_rsp_text)
            if isinstance(_dict_obj, dict) and meta_node in _dict_obj:
                # 校验响应数据的meta元数据，判断返回码；没有meta，则不校验meta元数据
                _meta = _dict_obj.get(meta_node)
                _meta_code = _meta.get('code')
                if 'success' in _meta and _meta['success'] != True:
                    return ApiResponse.assemble_err_resp(_meta_code, _meta.get(msg_node))
                if _meta_code is not None and not ApiRspCode.is_succ(_meta_code) and '0' != _meta_code:
                    return ApiResponse.assemble_err_resp(_meta_code, _meta.get(msg_node))
        except Exception as e:
            log.error('[_parse_http_error_meta]解析http返回异常 %s', _rsp_text, e)
    # 直接返回http响应
    return ApiResponse.assemble_err_resp(
        ApiRspCode.HTTP_ERRCODE_PRE.value.format(http_response.status_code), _rsp_text)


def cal_timestamp(t_dict, headers):
    for header in headers:
        if header.startswith('X-T') or header.startswith('x-t') or header.startswith('T_') or header.startswith('t_'):
            t_dict[header] = headers.get(header)


def trace_http_log(response):
    log.info(f'****** 请求接口:\turl={response.request.url}\tmethod={response.request.method}')
    log.info(f'\trequest:\theaders={response.request.headers}')
    if response.status_code != 200 or _is_debug:
        log.info(f'\trequest:\tbody={response.request.body}')
    log.info(' ')
    log.info(f'\tresponse:\tcode={response.status_code}')
    log.info(f'\tresponse:\theaders={response.headers}')
    if response.status_code != 200 or _is_debug:
        log.info(f'\tresponse:\tcontent={response.content}')
