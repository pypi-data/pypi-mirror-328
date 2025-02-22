# -*- coding: utf-8 -*-
import datetime
import warnings
import pandas as pd
import numpy as np
import re

from deepquant import gid
#from deepquant.factor import op
from ..decorators import export_as_api
from deepquant.quest.apis.api_base import history_bars
from ..validators import (
    ensure_list_of_string,
    ensure_date_int,
    ensure_date_range,
    ensure_string,
    ensure_string_in,
    check_items_in_container,
    ensure_market_code,
)

#from datac.decorators import export_as_api

from ..yhclient import YhClient
#from datac.decorators import export_as_api

#client = YhClient("http://yhds.inner.prodxc.chinastock.com.cn")

@export_as_api
def all_instruments(type_='stock', date=None, market="cn", **kwargs):
    """
    获取合约信息
    >>> all_instruments('stock', cache=True)
    market_code security_name exchange board_type  ... industry_code industry_name   type            trading_hours
    0   000001.SZ          平安银行       SZ         主板  ...          b10l            银行  stock  09:31-11:30,13:01-15:00
    1   000002.SZ           万科A       SZ         主板  ...          b10n           房地产  stock  09:31-11:30,13:01-15:00
    """
    '''
    ins_list = client.get("instruments", **{
        "instrument_type": type_,
        "cache": kwargs.get("cache", True)
    })
    df = pd.DataFrame(ins_list)
    '''
    df,code,msg = gid.get_instruments(variety=type_)

    return df

@export_as_api
def get_share_transformation(predecessor=None, market="cn"):
    """
    获取转股信息
    :param predecessor: 标的名称,格式如[‘600000.SH，600004.SH’],变更前或变更后的标的名称都可以
    :param market:  (Default value = "cn")
    :return pd.DataFrame
    """
    if predecessor:
        predecessor = ensure_list_of_string(predecessor)

    #df,code,msg = gid.get_code_change(predecessor)
    df,code,msg = gid.get_code_change()
    
    if not gid.is_success_code(code):
        raise ValueError("get_code_change  fail.{}{}".format(code, msg))

    df.columns=["predecessor","effective_date","current_code","successor"]
    df["share_conversion_ratio"]=0
    df["predecessor_delisted"]=True
    df["discretionary_execution"]=False
    df["predecessor_delisted_date"]=df["effective_date"]
    df["event"]="code_change"
    df=df[[
        "predecessor", "successor", "effective_date","current_code", "share_conversion_ratio", "predecessor_delisted",
        "discretionary_execution", "predecessor_delisted_date", "event"
    ]]
    if predecessor:
        df = df[df['predecessor'].isin(predecessor)]
    df = df.sort_values('predecessor').reset_index(drop=True)
    
    return df

@export_as_api(namespace="econ")
def get_reserve_ratio(reserve_type="all", start_date=None, end_date=None, market="cn"):
    """获取存款准备金率

    :param reserve_type: 存款准备金详细类别，默认为'all'，目前仅支持'all'、'major'、'other'类别的查询
    :param start_date: 开始查找时间，如'20180501'，默认为上一年的当天
    :param end_date: 截止查找时间，如'20180501'，默认为当天
    :param market:  (Default value = "cn")
    :return: pd.DataFrame

    """
    check_items_in_container(reserve_type, ["all", "major", "other"], "reserve_type")

    start_date, end_date = ensure_date_range(start_date, end_date, delta=relativedelta(years=1))

    # ret = get_client().execute(
    #     "econ.get_reserve_ratio", reserve_type, start_date, end_date, market
    # )
    start_time=str(start_date)
    end_time = str(end_date)
    ret, code, msg = gid.get_reserve_ratio(reserve_type, start_time, end_time)
    # if not ret:
    #     return
    # columns = ["info_date", "effective_date", "reserve_type", "ratio_floor", "ratio_ceiling"]
    # df = ret.set_index("info_date").sort_index(ascending=True)
    return ret
