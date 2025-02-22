#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: zhangluping_it
@time: 2024/7/22 8:55
@description: 
"""

import importlib

import pandas as pd
from google.protobuf import json_format, any_pb2
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.message import Message as PB_Message
from google.protobuf import descriptor

# from google.protobuf.json_format import MessageToDict
from .pb_json_format import MessageToDict, MessageToJson
from ..utils.log_writer import log

from . import sdk_message_pb2
from . import data_type_pb2
from .common_pb2 import *
from .news_pb2 import *
from .sdk_message_pb2 import *
from .market_data_pb2 import *
from .data_type_pb2 import *

_sym_db = _symbol_database.Default()


def convert_req2protobuf(pb_class, params_dict):
    if pb_class is None:
        log.error('[convert_req2protobuf] %s - pb_class_error %s', pb_class, '未传入请求数据pb类')
        raise Exception("未传入请求数据pb类")
    try:
        _req_obj = pb_class()
        json_format.ParseDict(params_dict, _req_obj, ignore_unknown_fields=True)
        return _req_obj
    except Exception as others:
        log.error('[convert_req2protobuf] %s - others %s', pb_class, others)
        raise Exception("接口请求PB类'{}'转换错误: {}".format(pb_class, others))


def convert_resp_proto2ins(pb_class, resp_context):
    """
    转换PB响应二进制为PB对象
    :param pb_class：    proto定义类，如pb_class
    :param resp_context:    http返回二进制
    :returns PB对象
    """
    try:
        _pb_ins = pb_class()
        _pb_ins.ParseFromString(resp_context)
        return _pb_ins
    except NameError as method_error:
        log.error('[convert_context2protobuf] %s - method_error %s', pb_class, method_error)
        raise Exception(f"响应数据pb类'{pb_class}'中函数ParseFromString不存在。")
    except Exception as others:
        log.error('[convert_context2protobuf] %s - others %s', pb_class, others)
        raise Exception("响应数据pb类'{}'转换错误: {}".format(pb_class, others))


def convert_resp_proto2dict(pb_class, resp_context):
    """
    转换PB响应二进制为dict
    :param pb_class：    proto定义类，如pb_class
    :param resp_context:    http返回二进制
    :returns dict
    """
    try:
        _pb_ins = pb_class()
        _pb_ins.ParseFromString(resp_context)
        # TODO 增加行情类数据，待出默认值配置
        _pb_dict = MessageToDict(_pb_ins,
                                 preserving_proto_field_name=True)
        if 'data' in _pb_dict:
            data_value = getattr(_pb_ins, 'data')
            if len(data_value) > 0:
                if not isinstance(data_value[0], any_pb2.Any):
                    log.error("解析失败，不是Any类型：%s", data_value[0])
                    return _pb_dict
                type_urls = data_value[0].type_url.split('/')
                if len(type_urls) == 1:
                    log.error("非法的type_url=%s, data=%s", data_value[0].type_url, data_value[0])
                    return _pb_dict
                message_class = _sym_db.GetPrototype(_sym_db.pool.FindMessageTypeByName(type_urls[-1]))
                if message_class and message_class.DESCRIPTOR.file.name == 'news.proto':
                    for item in _pb_dict['data']:
                        missing_fields = {field.name for field in message_class.DESCRIPTOR.fields} - set(item.keys())
                        if len(missing_fields) > 0:
                            item.update({field: None for field in missing_fields})
        return _pb_dict
    except NameError as method_error:
        log.error('[convert_context2protobuf] %s - method_error %s', pb_class, method_error)
        raise Exception(f"响应数据pb类'{pb_class}'中函数ParseFromString不存在。")
    except Exception as others:
        log.error('[convert_context2protobuf] %s - others %s', pb_class, others)
        raise Exception("响应数据pb类'{}'转换错误: {}".format(pb_class, others))


def convert_result_table_values(_pb_ins):
    if isinstance(_pb_ins, ResultTable):
        _col_types = []
        _col_names = []
        _rows = []
        for field, value in _pb_ins.ListFields():
            if field.name == 'col_types' and field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
                # Convert a repeated field.
                _col_types = [k for k in value]
            elif field.name == 'col_names' and field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
                # Convert a repeated field.
                _col_names = [k for k in value]
            elif field.name == 'rows' and field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
                for row in value:
                    if isinstance(row, ResultRow):
                        _rows.append([row_value for row_value in row.values])
                    print(row)
            print(field, value)
        dtypes = {}
        if len(_col_names) == len(_col_types):
            for _index in range(len(_col_names)):
                _col_name = _col_names[_index]
                _col_type = _col_types[_index]
                if _col_type == 'string' or _col_type == 'str':
                    _col_type = str
                elif _col_type == 'float' or _col_type == 'number':
                    _col_type = float
                elif _col_type == 'int' or _col_type == 'integer':
                    _col_type = int
                else:
                    error_msg = "ResultTable中未识别的类型{}".format(_col_type)
                    log.error("[解析ResultTable]异常 - %s, _col_types=%s", error_msg, _col_types)
                    raise Exception(error_msg)
                dtypes[_col_name] = _col_type
        else:
            error_msg = "ResultTable中列名和类型数量不一致{}!={}".format(len(_col_names), len(_col_types))
            log.error("[解析ResultTable]异常 - %s, _col_names=%s, _col_types=%s",
                      error_msg, _col_names, _col_types)
            raise Exception(error_msg)
        df = pd.DataFrame(data=_rows, columns=_col_names)
        df = df.astype(dtypes)
        MessageToDict(_pb_ins)
        pd.DataFrame(data=_rows, columns=_col_names, dtype=_col_types)
        _pb_ins.rows

    else:
        # TODO
        log.error('[convert_result_table_values] %s - others %s', type(_pb_ins), others)


def parse_any_obj(_data, preserving_proto_field_name=True):
    """
    :returns type, data, msg
    """
    if not isinstance(_data, any_pb2.Any):
        log.error("解析失败，不是Any类型：%s", _data)
        return None, None, '不是Any类型'
    type_urls = _data.type_url.split('/')
    if len(type_urls) == 1:
        log.error("非法的type_url=%s, data=%s", _data.type_url, _data)
        return None, None, '非法的type_url'
    type_descriptor = _sym_db.pool.FindMessageTypeByName(type_urls[-1])
    message_class = _sym_db.GetPrototype(type_descriptor)
    data_ins = message_class()
    data_ins.ParseFromString(_data.value)
    # 此处需要 MessageToDict，MessageToDict 中包含了价格和金额转换逻辑
    data_dict = MessageToDict(data_ins,
                              preserving_proto_field_name=preserving_proto_field_name)
    return type(data_ins), data_dict, None


def log_pb_obj(_pb_obj):
    if isinstance(_pb_obj, PB_Message):
        return MessageToJson(_pb_obj).replace('\n', '')
    else:
        return _pb_obj
