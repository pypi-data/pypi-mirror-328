#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import json
from functools import partial
import requests
import deepquant.oplib as sf


# # 获取项目的根路径
# project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# # 将项目根路径添加到 sys.path
# if project_path not in sys.path:
#     sys.path.append(project_path)

from ..gqclient.commons import TTLCache
from ..gqclient.hclient import GidHClient
from ..proto.common_pb2 import BatchReq,BatchRes

# 金融函数相关
from ..gqclient.commons import ApiRspMode
from ..gqclient.commons import ApiRspCode
from ..gqclient.commons import FunctionMode
from ..proto import financial_fun_pb2

class DataApi:
    __token = ''
    __http_url = ''
    __user=''


    def __init__(self, user,token, timeout=30):
        self.__timeout = timeout
        self.__user = user
        cache = TTLCache()

        self.reqClient = GidHClient(cache)
        self.reqClient.init(user, token)

    def query(self, api_name, df=True, limit=None, fields=None, **kwargs):
        '''
        基础查询接口
        :param api_name:
        :param fields:
        :param kwargs:
        :return:
        '''

        if (limit==None) or (limit=='0') :
            limit = 100000
            need_batch = True
        else:
            need_batch = False

        kwargs['fields']=fields
        data, code, msg = self.reqClient.post_batch(func_name=api_name, params=kwargs,
                                                    fields=fields,df=df, limit=limit,
                                                    need_batch = need_batch,req_pb_class=BatchReq,rsp_pb_class=BatchRes)

        if str(code) not in ("ApiRspCode.SUCCESS", "0"): 
            print(kwargs)
            print(limit)
        return  data, code, msg;

    def queryByBatch(self, api_name, df=True, fields=None,batch=None, **kwargs):
        '''
        基础查询接口
        :param api_name:
        :param fields:
        :param kwargs:
        :return:
        '''
        batch= {
        "req_id": "1",
        "offset": "0",
        "limit": 1000
        };
        req_params = {
            'api_name': api_name,
            'params': kwargs,
            'fields': fields,
            'df': df,
            'batch':batch

        }
        data, code, msg = self.reqClient.post(func_name=api_name, params=req_params, df=True, timeout=self.__timeout)
        return data, code, msg;


    def factor_query_with_batch(self, api_name, df=True, limit=100000, **kwargs):
        data, code, msg = self.reqClient.post_batch(func_name=api_name, params=kwargs,
                                                    fields=None, df=True, limit=limit,
                                                    need_batch=True, req_pb_class=BatchReq, rsp_pb_class=BatchRes)
        return data, code, msg

    def get_factor(self,api_name, **kwargs):

        data, code, msg = self.reqClient.post(func_name=api_name, params=kwargs, df=True, timeout=self.__timeout)
        return data, code, msg;

    def Subscribe(market_code, flag):
        '''
        订阅行情数据
        :return:
        '''
        pass

    def UnSubscribe(market_code, flag):
        '''
        取消订阅行情数据
        :return:
        '''
        pass

    def __getattr__(self, name):
        return partial([self.query,self.queryByBatch], name)


    def function_compute(self, function_name, mode = FunctionMode.SIMPLE, params=None):
        '''
        金融函数计算接口
        :param function_name: 个人金融函数名称
        :param mode:
                FunctionMode.SIMPLE 简单参数模式 此模式下直接传递参数
                            比如fun(x,y)，可以直接传递params="1,2"简单量作为参数
                FunctionMode.COMPLEX 复杂参数模式
                            支持:标量、列表、DataFrame等常用数据格式
                            比如fun(x,y)，可以预定义
                            a=[1,2]
                            b=1234
                            params=[a,b]这种方式传递复杂参数
        :param params:参数说明见mode模式说明
        :return:
            code: 正常返回"00000"
            msg:  信息
            data: 返回结果，如果自定义函数返回多值，此处返回的是list
        '''
        #import swordfish as sf
        #from swordfish.data import Table, Vector, Matrix, Dictionary
        # 修改sf新版本引用方式
        # import deepquant.oplib as sf
        from deepquant.oplib._swordfishcpp import Table, Vector, Matrix, Dictionary

        if mode == FunctionMode.SIMPLE:
            req = financial_fun_pb2.ComputeRequest(userName = self.__user, mode=mode.value, funName = function_name);
            if params is not None:
                req.funStr = params
                data, code, msg = self.reqClient.post('funCompute', params=req,  req_pb_class=financial_fun_pb2.ComputeRequest, rsp_pb_class=financial_fun_pb2.ComputeResponse, df=False, rsp_mode= ApiRspMode.PASSED)
            if ApiRspCode.is_succ(code):
                if data.meta.code == "00000":
                    # sf进行结果解压
                    sf.init()
                    obj = sf.io.loads(data.result)
                    return obj, code, msg
                else:
                    print("function compute failed:" + data.meta.message)
            else:
                print("function compute api failed:" + msg)
            return data, code, msg

        # 复杂参数模式
        if mode == FunctionMode.COMPLEX:
            req = financial_fun_pb2.ComputeRequest(userName=self.__user, mode=mode.value, funName=function_name);
            #params序列化，然后传入参数
            #req.funParams;
            # import swordfish as sf
            # import deepquant.oplib as sf
            sf.init()
            for var in params:
                var_sf = self.transform_params(var)
                if var_sf is None:
                    print("params type not support")
                    return None, "00001", "params type not support"
                var_byte = sf.io.dumps(var_sf)
                req.funParams.append(var_byte)
                print("function params dumps success.")
                #print("-- ok --")
            data, code, msg = self.reqClient.post('funCompute', params=req,
                                                  req_pb_class=financial_fun_pb2.ComputeRequest,
                                                  rsp_pb_class=financial_fun_pb2.ComputeResponse, df=False,
                                                  rsp_mode=ApiRspMode.PASSED)

            if ApiRspCode.is_succ(code) :
                if data.meta.code=="00000":
                    # sf进行结果解压
                    sf.init()
                    obj = sf.io.loads(data.result)
                    # print(sf.call("typestr", obj))
                    # print(obj)
                    # print(data)
                    return obj, code, msg
                else:
                    print("function compute failed,code:" + data.meta.code)
                    print("function compute failed,msg:" + data.meta.message)
            else:
                print("function compute api failed:" + msg)
            return data, code, msg


    def transform_params(self, var):
        '''
        内部转换函数，不对外提供服务
        '''
        # print("in transform_params")
        if isinstance(var, float) or isinstance(var, int) or isinstance(var, bool) or isinstance(var, str):
            return sf.scalar(var)
        elif isinstance(var, np.ndarray) or isinstance(var, list):
            return sf.vector(var)
        elif isinstance(var, dict):
            return Dictionary.from_dict(var)
        elif isinstance(var, pd.core.frame.DataFrame):
            return Table.from_pandas(var)
        else:
            return None
