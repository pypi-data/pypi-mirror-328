import inspect
import os
import logging

import requests
import pandas as pd
import numpy as np
import yaml
from . import analysor, perf
from .factor_parser import parse_function_from_string, param2api, extract_func




from .oq_data import OqData
from deepquant.data.interface import gid

logger = logging.getLogger("f_calc")
logger.setLevel(logging.INFO)

class DataError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def run(task_info):
    # ret = get_params_by_taskid(taskid, task_info)
    # if len(ret) == 7:
    #     username, func_str, start_date, end_date, frange, factor_id, factor_name = ret
    # else:
    #     return
    func_str=task_info['factorContent']
    if func_str.find("def factor_calc(") != -1:
        stage_cnt = 12
        logger.info(f"script schema, total stage {stage_cnt}")
        df_fval = run_factor_scipt(task_info)
    else:
        stage_cnt = 17
        logger.info(f"formula schema, total stage {stage_cnt}")
        meta = parse_function_from_string(func_str)
        data2cols = get_data2cols()
        api2fields = param2api(meta["parameters"], data2cols)
        f_func = extract_func(meta)
        dfs = get_data(api2fields, task_info)
        df = data_preprocess(dfs, task_info)
        df_fval = calc_fvalue(f_func, df, meta, api2fields)


        #获取股价
        price = get_prices_data(task_info)
       

        #print("结束")
        return df_fval,price

def get_data2cols():
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
    file_dir = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.join(file_dir, "data_desp.yaml")
    from ..data.utils import gqconfig
    host = gqconfig.configs.c_server['host']
    try:
        try:
            url = f"http://{host}/static/conf/data_desp.yaml"
            r = requests.get(url)
            if r.status_code != 200:
                raise(Exception)
            data_cols = yaml.safe_load(r.text)
            with open(fpath, 'w') as fout:
                yaml.dump(data_cols, fout, default_flow_style=False, allow_unicode=True)
        except Exception as e:
            default_f = "data_desp_default.yaml"
            print(f"{url} failed, load local {default_f}")
            fpath = os.path.join(file_dir, default_f)
            with open(fpath) as fin:
                data_cols = yaml.safe_load(fin.read())
    except Exception as e:
        return DATA_COLS
    return data_cols

def calc_fvalue(f_func, df, meta, api2fields):
    cols_map = {}
    for api, fields_map in api2fields.items():
        cols_map.update(fields_map)

    cols = [
        param["name"]
        for param in meta["parameters"]
        if param["annotation"].find("t:param") == -1
    ]
    for col in cols:
        if col not in df.columns:
            raise (DataError(f"{col}未获取到数据"))
    args = {col: df[col] for col in cols}
    f_val = f_func(**args)
    f_val = f_val.dropna(how='all')
    print(f_val)
    return f_val

def run_factor_scipt(factor_task):
    logger.info(factor_task["factorContent"].replace("\\n", "\n").replace("\\", ""))
    import src.interface.gid

    gid.init("gidtest", "gid#2024")
    user_space = {
        "DataError": DataError,
        "pd": pd,
        "np": np,
        "task_info": factor_task,
        "gid": gid,
    }
    try:
        exec(
            factor_task["factorContent"].replace("\\n", "\n").replace("\\", ""),
            user_space,
        )
    except Exception as e:
        raise (e)
    if "factor_calc" not in factor_task["factorContent"]:
        raise (DataError("入口函数factor_calc不存在"))
    try:
        f_val = user_space["factor_calc"](factor_task)
    except DataError as e:
        raise (DataError("数据获取错误"))
    except Exception as e:
        raise (f'{type(e)}')
    return f_val.dropna()


def get_data(api2fields, task_info):
    import psutil
    pid = os.getpid()
    process = psutil.Process(pid)
    mem = process.memory_info()
    logger.info(f"mem: {mem.rss/1024/1024:.2f}MB; {mem.vms/1024/1024:.2f}MB")
    # index_stk_df = od.get_index_stks(task_info["stockIndex"])
    # stk_codes = [row["con_code"] for idx, row in index_stk_df.iterrows()]
    # freq = task_info.get("freq", "1d")
    params = dict(
        market_code=task_info["market_code"],
        frequency=task_info["frequency"],
        start_time=f"{task_info['startDate']} 08:00:00",
        # start_time=f"2024-05-01 08:00:00",
        end_time=f"{task_info['endDate']} 08:00:00",
    )
    print(api2fields)
    #defaultdict(<class 'dict'>, {'QueryKline': {'volume': 'volume'}})
    dfs = []
    for api, fields in api2fields.items():
        data = od.get_data(api, fields, **params)
        dfs.append(data)
    #dfs = pd.concat(dfs)
    mem = process.memory_info()
    logger.info(f"mem: {mem.rss/1024/1024:.2f}MB; {mem.vms/1024/1024:.2f}MB")
    #print(dfs.head(10))
    return dfs


def data_preprocess(dfs,task_info):
    """
    将所有需要数据拼到一个df_panel
    """
    params = dict(
        start_time=f"{task_info['startDate']} 08:00:00",
        end_time=f"{task_info['endDate']} 08:00:00",
    )
    calendar = od.get_calendar(**params)
    df = dfs[0]
    for data in dfs[1:]:
        df = pd.merge(df, data, on=["dt", "code"], how="outer")
    logger.info(f"data: {df.shape}, calendar: {calendar.shape}")
    df = df.drop_duplicates(subset=['dt', 'code'], keep='last')
    print(df)
    df_panel = df.pivot(index="dt", columns="code")
    df_panel = df_panel.ffill()
    return df_panel

def get_prices_data(factor_task):
    #index_stk_df = od.get_index_stks(task_info["stockIndex"])
    #stk_codes = [row["con_code"] for idx, row in index_stk_df.iterrows()]
    #freq = task_info.get("freq", "1d")
    params = dict(
        market_code=factor_task['market_code'],
        frequency=factor_task['frequency'],
        start_time=f"{factor_task['startDate']} 08:00:00",
        end_time=f"{factor_task['endDate']} 08:00:00",
    )
    dfs = od.get_data(
        "get_kline",
        {
            "close": "close_price",
        },
        **params,
    )
    logger.info(
        f"get prices {factor_task['startDate']}-{factor_task['endDate']}, {dfs.code.value_counts().shape} lines({factor_task['frequency']})"
    )
    
    return dfs


def calc_factor(
        market_code,
        factor_name,
        frequency,
        start_time,
        end_time,
        username=None,
        password=None
):
    global od
    if not username:
        username = os.getenv("UP_USER_NAME", "")
        password = os.getenv("UP_USER_APPKEY", "")
    od = OqData(username=username, password=password)
    factor_task={
        'market_code':market_code,
        'factorContent': factor_name,
        'startDate':start_time,
        'endDate':end_time,
        'frequency':frequency
    }

    return run(factor_task)

