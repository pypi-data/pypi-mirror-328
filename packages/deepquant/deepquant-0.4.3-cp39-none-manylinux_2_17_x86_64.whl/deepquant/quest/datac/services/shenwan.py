# -*- coding: utf-8 -*-
import datetime
import warnings
import pandas as pd
import numpy as np
import re
from ..decorators import export_as_api

from deepquant import gid
#from deepquant.factor import op
#from deepquant.algo.apis.api_base import history_bars
from ..validators import (
    ensure_list_of_string,
    ensure_date_int,
    ensure_date_range,
    ensure_string,
    ensure_string_in,
    check_items_in_container,
    ensure_date_or_today_int
)


@export_as_api
def get_instrument_industry(order_book_ids, source='14', level=1, date=None, market="cn"):
    """获取股票对应的行业

    :param order_book_ids: 股票列表，如['000001.XSHE', '000002.XSHE']
    :param source: 分类来源。'10':万得行业分类 '12'：证监会行业分类  '13':申万行业分类 '14':中信行业分类 默认'14'
                
    :param date: 如 '2015-01-07' (Default value = None)
    :param level:  (Default value = 1)
    :param market:  (Default value = "cn")
    :returns: code, name
        返回输入日期最近交易日的股票对应行业
    """
    order_book_ids = ensure_list_of_string(order_book_ids)
    source = ensure_string_in(source, ["10", "12", "13", "14"], 'source')
    date = ensure_date_or_today_int(date)
    if(level not in [0,1,2,3]): 
        raise ValueError("level must be in [0,1,2,3]")

    f,code,msg = gid.industry(order_book_ids)

    if not gid.is_success_code(code):
         raise ValueError("get_instrument_industry  fail.{}{}".format(code, msg))

    source=int(source)
    df,code,msg=gid.industry(['000001.SZ','000002.SZ'])
    df=df[['market_code','industries_type','in_date','ind_code_l1','ind_name_l1','ind_code_l2','ind_name_l2','ind_code_l3','ind_name_l3']]
    df['in_date']=df['in_date'].astype(int)
    df.columns=['market_code','source','in_date','first_industry_code','first_industry_name','second_industry_code','second_industry_name','third_industry_code','third_industry_name']
    df=df[df['source']==source]
    #df=df[df['in_date'] <= date] #目前好像都是一条数据，先不用日期筛选了
    if level==1:
        df = df[['market_code','in_date','first_industry_code','first_industry_name']]
    elif level==2:
        df = df[['market_code','in_date','second_industry_code','second_industry_name']]
    elif level==3:
        df = df[['market_code','in_date','third_industry_code','third_industry_name']]
   
    return df.set_index("market_code")