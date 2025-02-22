# -*- coding: utf-8 -*-

from datetime import datetime,timedelta
import warnings
import pandas as pd
import numpy as np
import re


from deepquant import gid
from deepquant.factor import op
from deepquant.factor import factor_cal  
from deepquant.quest.apis.api_base import history_bars
from ..decorators import export_as_api

from ..validators import (
    ensure_list_of_string,
    ensure_date_int,
    ensure_date_range,
    ensure_string,
    ensure_string_in,
    check_items_in_container,
    #ensure_order_book_ids,
    #ensure_order_book_id,
)

local_calc_factor = ["MA", "SMA"]

@export_as_api
def calc_factor(
        order_book_ids,  # type: Union[str, List[str]]
        source_code,  ## type:string  inspect.getsource(xxx)
        factor_name,
        start_date, 
        end_date,
        frequency ='1d',  ## type: str 1d, 5m, 10m, 15m, 30m, 60m
):  # type: (...) -> pd.DataFrame
    """   
    :param order_book_ids:  合约代码，可传入order_book_id, order_book_id list
    :param factors: 因子计算函数代码，只能传一个函数代码
    :param start_date: 
    :param end_date: 
    :frequency:  (Default value = '1d')  '1d', '5m', '10m', '15m', '30m', '60m'
    :return: pd.DataFrame
    """
    order_book_ids = ensure_list_of_string(order_book_ids)

    if start_date and end_date:
        start_date, end_date = ensure_date_range(start_date, end_date, timedelta(days=15))
    elif start_date:
        raise ValueError("Expect end_date")
    elif end_date:
        raise ValueError("Expect start_date")

    factor_value, price = factor_cal.calc_factor(market_code=order_book_ids,
                                      factor_name=source_code,
                                      start_time=datetime.strptime(str(start_date), '%Y%m%d').strftime('%Y-%m-%d'),
                                      end_time=datetime.strptime(str(end_date), '%Y%m%d').strftime('%Y-%m-%d'),
                                      frequency=frequency)
    
    factor_value = factor_value.melt(col_level=0,value_vars=factor_value.columns,var_name="security_code", value_name='value',
             ignore_index=False
            )
    factor_value=factor_value.reset_index()
    factor_value.rename(columns={'dt':'data_time'},inplace=True)
    factor_value['name']=factor_name 
    factor_value=factor_value[['security_code','data_time','name','value']]

   
    #factor_value.index.names = ['security_code', 'data_time']
    
    return factor_value

def resolve_factor(factor):
    match = re.match(r"([a-zA-Z]+)([0-9]+)", factor)
    if match:
        return match.groups()
    return factor, None

@export_as_api
def get_factor(
        order_book_ids,  # type: Union[str, List[str]]
        factors,  # type: Union[str, List[str]]
        start_date=None, 
        end_date=None,
        universe=None,  # type: Optional[Union[str, List[Union]]]
        expect_df=True  # type: Optional[bool]
):  # type: (...) -> pd.DataFrame
    """
    获取股票截止T-1日的因子数据
    简单量价因子可以本地计算，复杂因子从服务端读取

    :param order_book_ids:  合约代码，可传入order_book_id, order_book_id list
    :param factors: 因子名称 以MA5为例， 本地计算: "MA5"或"local.MA5"  远程获取: "public.MA5"  "xxxx(userid).MA5"  
    :param start_date: 
    :param end_date: 
    :param universe: 当获取横截面因子时，universe指定了因子计算时的股票池
    :param expect_df: 默认为False。当设置为True时，总是返回  DataFrame。pandas 0.25.0 以上该参数应设为 True，以避免因试图构建 Panel 产生异常
    """

    order_book_ids = ensure_list_of_string(order_book_ids)
    factor_list = ensure_list_of_string(factors)
    if start_date and end_date:
        start_date, end_date = ensure_date_range(start_date, end_date, timedelta(days=15))
    elif start_date:
        raise ValueError("Expect end_date")
    elif end_date:
        raise ValueError("Expect start_date")

    dataTotal = pd.DataFrame()
    dataFrames = []
    for i, factor in enumerate(factor_list):
        if "local." in factor  or "." not in factor:#本地计算
            factor_name = factor
            if '.' in factor_name:
                factor_name = factor_name.split('.')[-1]
            string_part, number_part = resolve_factor(factor_name)
            if string_part.upper()  in local_calc_factor and number_part :
                window = int(number_part)
                df = pd.DataFrame()
                for j, market_code in enumerate(order_book_ids):
                    #history_bars对日线处理时，会包含当日数据，需要剔除当天的数据
                    date = history_bars(market_code, (end_date - start_date + 1) + window, '1d', 'orig_time')

                    strdate = datetime.strptime(str(int(date[-2]/1000000)), '%Y%m%d').strftime('%Y-%m-%d')
                    prices = history_bars(market_code, (end_date - start_date + 1) + window, '1d', 'close_price')
                    func = getattr(op, string_part.upper())
                    if(func):  
                        value = func(prices[:-1], window)[-1]
                        new_row = pd.DataFrame({'security_code': [market_code],'data_time':[strdate], 'name': [factor], 'value': [str(value)]})
                        
                        if df.empty:
                            df = new_row
                        else:
                            df = pd.concat([df, new_row], ignore_index=True)
                    
                    else:
                        raise ValueError("Factor function not found.{}".format(factor))
                    
                dataFrames.append(df)
                    
            else:
                raise ValueError("local factor name not found.{}".format(factor))
            
        else:
            data, code, msg = gid.get_factor(factor, 
            datetime.strptime(str(start_date), '%Y%m%d').strftime('%Y-%m-%d 09:30:00'),
            datetime.strptime(str(end_date), '%Y%m%d').strftime('%Y-%m-%d 09:30:00'),
            '1d', universe, order_book_ids, expect_df)

            if not gid.is_success_code(code):
                raise ValueError('gid.get_factor failed: {}:{}'.format(code, msg))

            data=data[['security_code','data_time','name','value']]
            data['data_time']=pd.to_datetime(data['data_time'])
            data['data_time']= data['data_time'].dt.date
            dataFrames.append(data)

    dataTotal = pd.concat(dataFrames,ignore_index=True)   
    #dataTotal=dataTotal.sort_values('security_code')
    #dataTotal.set_index(["security_code", "data_time"], inplace=True)                         
    return dataTotal     

    



