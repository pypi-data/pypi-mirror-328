# -*- coding: utf-8 -*-
"""
Description: 解析用户输入的python函数类型的因子定义
Author: wangdanfeng
Email: wangdanfeng_it@chinastock.com.cn
Date Created: 2024-07-12
Version: 1.0
"""

import re
import ast
import astor
import inspect
import importlib

import collections
import yaml

from RestrictedPython import compile_restricted
from RestrictedPython.Guards import safe_builtins
from RestrictedPython import compile_restricted
from RestrictedPython import safe_globals
from RestrictedPython import utility_builtins


class FunctionCallVisitor(ast.NodeVisitor):
    def __init__(self):
        self.function_metas = []

    def visit_FunctionDef(self, node):
        # 提取函数注释（类型提示）
        annotations = {}
        if node.returns:
            annotations["return"] = "" 

        parameters = []
        for arg in node.args.args:
            if arg.annotation:
                annotations[arg.arg] = ast.dump(arg.annotation)
            param_info = {
                "name": arg.arg,
                "default": None,
                # "annotation": ast.dump(arg.annotation) if arg.annotation else None,
                "annotation": (
                    arg.annotation.value
                    if (arg.annotation and isinstance(arg.annotation, ast.Constant))
                    else ''
                ),
                "kind": "POSITIONAL_OR_KEYWORD",
            }
            parameters.append(param_info)

        if node.args.defaults:
            num_defaults = len(node.args.defaults)
            for i, default in enumerate(node.args.defaults):
                parameters[-num_defaults + i]["default"] = ast.dump(default)

        meta = {
            "name": node.name,
            "doc": ast.get_docstring(node),
            "annotations": annotations,
            "parameters": parameters,
            "return_annotation": annotations.get("return"),
            "calls": [],
            "func_str": astor.to_source(node),
        }
        for stmt in node.body:
            meta["calls"].extend(self.visit_Statement(stmt))

        meta["calls"] = list(set(meta["calls"]))

        self.function_metas.append(meta)
        self.generic_visit(node)

    def visit_Statement(self, node):
        calls = []
        if isinstance(node, ast.Call) and not isinstance(node.func, ast.Attribute):
            calls.append(node.func.id)
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            calls.append(node.value.func.id)
        elif isinstance(node, ast.Assign):
            if 'func' in node.value.__dict__:
                if isinstance(node.value, ast.Call):
                    if 'id' in node.value.func.__dict__:
                        calls.append(node.value.func.id)
        # 递归访问所有子节点
        for field in ast.iter_fields(node):
            if isinstance(field[1], list):
                for item in field[1]:
                    if isinstance(item, ast.AST):
                        calls.extend(self.visit_Statement(item))
            elif isinstance(field[1], ast.AST):
                calls.extend(self.visit_Statement(field[1]))
        return calls


def parse_function_from_string(func_str):
    """
    解析用户输入的python函数类型的因子定义, 注意点:

    1. 只解析首个函数
    2. 函数参数均需要为可以获得的数据, 且均为数值类型
    3. 函数有返回值，且只取首个返回值作为结果
    4. 函数优先尝试采用pandas.DataFrame方式进行矩阵运算
    5. 支持的算子参考文档:
    6. 支持的数据参考文档
    7. 复杂因子请通过jupyterlab研究环境进行提交
    8. 不允许定义可变参数
    """
    try:
        tree = ast.parse(func_str)
    except Exception as e:
        raise ValueError(f"{func_str} 语法错误: {e}")
    # print(ast.dump(tree, indent=4))
    visitor = FunctionCallVisitor()
    visitor.visit(tree)
    if len(visitor.function_metas) == 0:
        raise ValueError("No function definition found in the provided string.")

    metadata = visitor.function_metas[0]
    return metadata


def extract_func(meta):
    """
    对于因子函数, 有如下限制：

    1. 限制内置函数和模块
    2. 限制全局变量
    3. 限制文件系统访问
    """
    '''#严格限制版本
    op_module = importlib.import_module("op")
    op_functions = {
        name: function
        for name, function in inspect.getmembers(op_module, inspect.isfunction)
    }
    total_code = meta["func_str"]
    compiled_code = compile_restricted(total_code, "<string>", "exec")
    restricted_globals = safe_globals.copy()
    restricted_globals.update(
        {
            "__builtins__": utility_builtins,
            "_print_": print,  # 允许使用 print 函数
        }
    )
    restricted_globals.update(op_functions)
    restricted_globals.update({"D": op_module.D})
    restricted_locals = {}
    exec(compiled_code, restricted_globals, restricted_locals)
    f_func = restricted_locals.get(meta["name"])
    '''
    import pandas as pd
    import numpy as np
    from deepquant.factor import op as sw
    import deepquant.factor.op as op
    user_space = {
        "pd": pd,
        "np": np,
        "sw": sw,
        'op': op,
    }
    try:
        import talib as ta
        user_space.update({"ta": ta})
    except ModuleNotFoundError:
        print("talib is not installed")
    user_space.update({name: func for name, func in inspect.getmembers(sw, inspect.isfunction)})
    try:
        exec(meta["func_str"], user_space)
    except Exception as e:
        raise (e)
    f_func = user_space[meta["name"]]
    return f_func


# 基础数据字段，转换为(表接口)对应的实际字段
DATA_COLS = {
    "get_kline": {
        "open_": {"colname": "open_price"},
        "high": {"colname": "high_price"},
        "close": {"colname": "close_price"},
        "low": {"colname": "low_price"},
        "volume": {},
        "amount": {"colname": "value"},
        "vwap": {},
    },
}

def anno2dict(anno:str):
    if not anno:
        return {}
    anno_d = dict()
    for ele in anno.split(","):
        res = ele.split(":")
        if len(res) == 2:
            anno_d.update({res[0]: res[1]})
    return anno_d


def check_dt_suffix(colname):
    target = r"(_\dq)$"
    match = re.search(target, colname)
    if match:
        ori_colname = colname.replace(match.group(1), "")
        return True, ori_colname
    else:
        return False, colname


def param2api(params, data2cols=DATA_COLS):
    res = collections.defaultdict(dict)
    for param in params:
        anno_d = anno2dict(param.get('annotation'))
        if 't:param' in param.get('annotation'):
            continue
        if 'f:' in param.get('annotation'):
            res["get_factor"][param["name"]] = anno_d["f"] 
            continue
        for api, cols in data2cols.items(): 
            param_name = param["name"]
            if api in ["cashflow", "balancesheet", "income", "fina_indicator"]:
                has_suffix, real_colname = check_dt_suffix(param["name"])
                if has_suffix:
                    param_name = real_colname

            if param_name in cols:
                colinfo = cols.get(param_name) or {}
                colname = colinfo.get("colname", param['name'])
                res[api][param['name']] = colname
                break
        else:
            raise(ValueError(f"{param_name}暂不支持公式,请用脚本Script版因子"))
    return res


def test():
    # func_str = """def alpha101(close, open_, high, low, ma5):
    #     return (close - open_) / (high - low + 0.001)"""
    func_strs = ["""
def ma5_rev(close: 'author:gidtest', win:'t:param'=5):  
    return Mean(close, win)/close
    """,
    """
def volume_ratio(close, volume, ndays:'t:param'=12):
    up = close.pct_change()
    AVS = volume[up > 0.0001].sum()
    BVS = volume[up < -0.0001].sum()
    CVS = volume[abs(up) < 0.0001].sum()
    return (AVS + 1/2*CVS) / (BVS + 1/2*CVS)
    """,
    """
def psy(close, ndays:'t:param'=12):
    up_days = close - close.shift(1) > 0
    return up_days.rolling(ndays).sum()/ndays
""",
"""
def money_flow(close, high, low, volume, ndays:'t:param'=20):
    flow = (close + high + low).mean() * volume
    return Mean(flow, ndays)
""",
"""
def ARBR(BR: "f:public.意愿指标BR", AR: "f:人气指标AR"):
    return AR - BR
"""
,
"""
def free_cash_flow(free_cash_flow, free_cash_flow_1q):
    return free_cash_flow - free_cash_flow_1q
"""
    ]
    for func_str in  func_strs[-1:]:
        print(func_str)
        meta = parse_function_from_string(func_str)
        print(meta)
        import json

        print(repr(func_str))

        tree = ast.parse(func_str)
        #print(ast.dump(tree, indent=4))
        visitor = FunctionCallVisitor()
        visitor.visit(tree)
        # for func in visitor.function_metas:
        #    print(func)
        # print(json.dumps(meta, indent=4, ensure_ascii=False))
        print('111', param2api(meta["parameters"]))
        p2a = param2api(meta["parameters"])
        extract_func(visitor.function_metas[0])
        from oq_data import OqData
        od = OqData('public', '123456')
        fields = {}
        for api, Fields in p2a.items():
            for k, v in Fields.items():
                if "." not in v:
                    fields[k] = f"public.{v}"
                else:
                    fields[k] = v
            for a, b in fields.items():
                print(b, fields)
                print(dict(
                        start_time='2021-07-03 08:00:00',
                        end_time='2024-07-04 08:00:00',
                        symbol_pool=["000905.SH"],
                        freq='1d',
                        market_code=[],
                        factor_name = b
                    ))
                df = od.get_data(
                    "get_factor",
                    fields,
                    **dict(
                        start_time='2021-07-03 08:00:00', 
                        end_time='2024-07-04 08:00:00', 
                        symbol_pool=["000905.SH"], 
                        freq='1d',
                        market_code=[],
                        factor_name = b
                    )
                )
                print(df.head())


if __name__ == "__main__":
    test()
