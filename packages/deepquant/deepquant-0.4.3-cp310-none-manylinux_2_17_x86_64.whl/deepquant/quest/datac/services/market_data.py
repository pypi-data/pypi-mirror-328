import six
import warnings
import numpy as np
import pandas as pd
from datetime  import datetime

from deepquant import gid
from ..utils import int8_to_date
from ..decorators import export_as_api, compatible_with_parm
#from collections import OrderedDict
#import math

from ..validators import (
    ensure_date_or_today_int,
    check_quarter,
    quarter_string_to_date,
    ensure_list_of_string,
    ensure_order,
    check_items_in_container,
    ensure_date_range,
    ensure_date_int,
    ensure_date_str,
    ensure_market_code,
    raise_for_no_panel,
)
from ...apis import assure_market_code


# @export_as_api
# @compatible_with_parm(name="country", value="cn", replace="market")
# def get_split(market_code, start_date=None, end_date=None, market="cn"):
#     """获取拆分信息
#
#     :param market_code: 股票 market_code or market_code list
#     :param start_date: 开始日期；默认为上市首日
#     :param end_date: 结束日期；默认为今天
#     :param market:  (Default value = "cn")
#
#     """
#     market_code = ensure_market_codes(market_code, market=market)
#     if start_date is not None:
#         start_date = ensure_date_int(start_date)
#     if end_date is not None:
#         end_date = ensure_date_int(end_date)
#     data = get_client().execute("get_split", market_code, start_date, end_date, market=market)
#     if not data:
#         return
#     df = pd.DataFrame(data)
#     df.sort_values("ex_dividend_date", inplace=True)
#     # cumprod [1, 2, 4] -> [1, 1*2, 1*2*4]
#     df["cum_factor"] = df["split_coefficient_to"] / df["split_coefficient_from"]
#     df["cum_factor"] = df.groupby("market_code")["cum_factor"].cumprod()
#     if len(market_code) == 1:
#         df.set_index("ex_dividend_date", inplace=True)
#     else:
#         df.set_index(["market_code", "ex_dividend_date"], inplace=True)
#     df.sort_index(inplace=True)
#     return df


@export_as_api
@compatible_with_parm(name="country", value="cn", replace="market")
def get_ex_factor(order_book_ids, start_date=None, end_date=None, market="cn"):
    """获取复权因子

    :param order_book_ids: 如'000001.XSHE'
    :param market: 国家代码, 如 'cn' (Default value = "cn")
    :param start_date: 开始日期，默认为股票上市日期
    :param end_date: 结束日期，默认为今天
    :returns: 如果有数据，返回一个DataFrame, 否则返回None

    """
    order_book_ids = ensure_list_of_string(order_book_ids)
    if start_date is not None:
        start_date = ensure_date_int(start_date)
    else:
        start_date = 19900101
    if end_date is not None:
        end_date = ensure_date_int(end_date)
    else:
        nowtime = datetime.now()
        end_date = int(nowtime.strftime('%Y%m%d'))
    
    f,code,msg = gid.exfactor(order_book_ids, datetime.strptime(str(start_date), '%Y%m%d').strftime('%Y-%m-%d'),
                              datetime.strptime(str(end_date), '%Y%m%d').strftime('%Y-%m-%d'))

    if not gid.is_success_code(code):
         raise ValueError("get_ex_factor  fail.{}{}".format(code, msg))
    
    df = f.drop_duplicates(subset=['cum_factor'], keep='first')
    df=df[['ex_date','market_code','ex_factor','cum_factor']]
    df['cum_factor'] = df['cum_factor'].astype(float)
    df.sort_values(["market_code", "ex_date"], inplace=True)
    df.set_index("ex_date", inplace=True)
    df.columns = ["market_code", "ex_factor", "ex_cum_factor"]
    df=df.drop(df.index[0])
    df.index=pd.to_datetime(df.index)
    return df

def convert_date_to_quarter(date_str):
    year=date_str[:4]
    month=int(date_str[4:6])
    q='q1'
    if 1<= month <=3:
        q='q1'
    elif 4<= month <=6:
        q='q2'
    elif 7<= month <=9:
        q='q3'
    elif 9<= month <=12:
        q='q4'

    return f"{year}{q}"

@export_as_api
@compatible_with_parm(name="country", value="cn", replace="market")
def get_dividend(order_book_ids, start_date=None, end_date=None, adjusted=False, expect_df=False, market="cn"):
    """获取分红信息

    :param order_book_ids: 股票 order_book_id or order_book_id list
    :param start_date: 开始日期，默认为股票上市日期
    :param end_date: 结束日期，默认为今天
    :param adjusted: deprecated
    :param market:  (Default value = "cn")

    """
    if adjusted:
        warnings.warn(
            "get_dividend adjusted = `True` is not supported yet. "
            "The default value is `False` now."
        )
    order_book_ids = ensure_list_of_string(order_book_ids)
    if start_date is not None:
        start_date = ensure_date_int(start_date)
    else:
        start_date = 19900101
    if end_date is not None:
        end_date = ensure_date_int(end_date)
    else:
        nowtime = datetime.now()
        end_date = int(nowtime.strftime('%Y%m%d'))
    
    df,code,msg = gid.divident(order_book_ids, datetime.strptime(str(start_date), '%Y%m%d').strftime('%Y-%m-%d'),
                              datetime.strptime(str(end_date), '%Y%m%d').strftime('%Y-%m-%d'))

    if not gid.is_success_code(code):
         raise ValueError("get_dividend  fail.{}{}".format(code, msg))
    
    df=df[['date_dvd_ann','dvd_per_share_pre_tax_cash','market_code','date_eqy_record','date_ex','date_dvd_payout','div_prelandate','report_period']]
    df.rename(columns={'date_dvd_ann':'declaration_announcement_date'},inplace=True)
    df.dropna(subset=['declaration_announcement_date','market_code'],inplace=True)
    df.columns=['declaration_announcement_date','dividend_cash_before_tax','market_code','book_closure_date','ex_dividend_date','payable_date','advance_date','quarter']
    df['round_lot']=1.0
    df['declaration_announcement_date']=pd.to_datetime(df['declaration_announcement_date'])
    df['book_closure_date']=pd.to_datetime(df['book_closure_date'])
    df['ex_dividend_date']=pd.to_datetime(df['ex_dividend_date'])
    df['payable_date']=pd.to_datetime(df['payable_date'])
    df['advance_date']=pd.to_datetime(df['advance_date'])
    df['quarter']=df['quarter'].apply(convert_date_to_quarter)
    
    if len(order_book_ids) == 1 and not expect_df:
        df.set_index("declaration_announcement_date", inplace=True)
    else:
        df.set_index(["market_code", "declaration_announcement_date"], inplace=True)
    return df.sort_index()

@export_as_api
@compatible_with_parm(name="country", value="cn", replace="market")
def get_split(order_book_ids, start_date='0', end_date='0', market="cn"):
    """获取拆分信息

    :param order_book_ids: 股票 order_book_id or order_book_id list
    :param start_date: 开始日期；默认为上市首日
    :param end_date: 结束日期；默认为今天
    :param market:  (Default value = "cn")

    """
    data,_,_=gid.split(order_book_ids,start_date,end_date)
    return data

@export_as_api
def get_st_days(market_code, start_date='0', end_date='2999-12-31', market="cn"):
    """获取拆分信息

    :param order_book_ids: 股票 order_book_id or order_book_id list
    :param start_date: 开始日期；默认为上市首日
    :param end_date: 结束日期；默认为今天
    :param market:  (Default value = "cn")

    """
    # if isinstance(market_code, six.string_types):
    #     market_code = [market_code]
    # market_code = [assure_market_code(i) for i in market_code]
    data,_,_=gid.st_days(market_code,start_date,end_date)
    return data


yield_curve_fields = {
    "end_date": "date",
    "yield_0s": "0S",
    "yield_1m": "1M",
    "yield_2m": "2M",
    "yield_3m": "3M",
    "yield_6m": "6M",
    "yield_9m": "9M",
    "yield_1y": "1Y",
    "yield_2y": "2Y",
    "yield_3y": "3Y",
    "yield_4y": "4Y",
    "yield_5y": "5Y",
    "yield_6y": "6Y",
    "yield_7y": "7Y",
    "yield_8y": "8Y",
    "yield_9y": "9Y",
    "yield_10y": "10Y",
    "yield_15y": "15Y",
    "yield_20y": "20Y",
    "yield_30y": "30Y",
    "yield_40y": "40Y",
    "yield_50y": "50Y",
}


@export_as_api
@compatible_with_parm(name="country", value="cn", replace="market")
def get_yield_curve(start_date=None, end_date=None, tenor=None, market="cn"):
    """获取国债收益率曲线

    :param market: 地区代码, 如'cn', 'us' (Default value = "cn")
    :param start_date: 开始日期 (Default value = "2013-01-04")
    :param end_date: 结束日期 (Default value = "2014-01-04")
    :param tenor: 类别, 如 OS, 1M, 3M, 1Y (Default value = None)

    """
    start_date, end_date = ensure_date_range(start_date, end_date)
    s, e = ensure_date_str(start_date), ensure_date_str(end_date)
    all_tenor = list(yield_curve_fields.values())
    del all_tenor[0] # 删除trade_date
    if tenor:
        tenor = ensure_list_of_string(tenor, "tenor")
        check_items_in_container(tenor, all_tenor, "tenor")
        tenor = ensure_order(tenor, all_tenor)
    else:
        tenor = all_tenor
    df, _, _ = gid.get_yield_curve(s, e)
    if df.empty or df is None:
        return
    df.rename(columns=yield_curve_fields, inplace=True)
    df.set_index("date", inplace=True)
    df.index = [int8_to_date(int(d)) for d in df.index]
    df = df.replace({None: np.nan})
    return df[tenor]


@export_as_api
def get_turnover_rate(order_book_ids, start_date=None, end_date=None, fields=None, expect_df=True, market="cn"):
    """获取股票换手率数据

    :param order_book_ids: 股票代码或股票代码列表
    :param start_date: 开始时间
    :param end_date: 结束时间；在 start_date 和 end_date 都不指定的情况下，默认为最近3个月
    :param fields: str或list类型. 默认为None, 返回所有fields.
                   field 包括： 'today', 'week', 'month', 'year', 'current_year'
                   (Default value = None)
    :param expect_df: 返回 MultiIndex DataFrame (Default value = True)
    :param market: 地区代码, 如: 'cn' (Default value = "cn")
    :returns: 如果order_book_ids或fields为单个值 返回pandas.DataFrame, 否则返回pandas.Panel

    """
    order_book_ids = ensure_list_of_string(order_book_ids)
    start_date, end_date = ensure_date_range(start_date, end_date)

    if fields is None:
        fields = ['market_code','trade_date','today','week','month','three_month','six_month','year','current_year']
    
    df, code, msg = gid.get_turnover_rate(order_book_ids, 
            datetime.strptime(str(start_date), '%Y%m%d').strftime('%Y-%m-%d'),
            datetime.strptime(str(end_date), '%Y%m%d').strftime('%Y-%m-%d'), 
            fields, True)
            
    if not gid.is_success_code(code):
        raise ValueError('gid.get_turnover_rate failed: {}:{}'.format(code, msg))


   
    df.sort_values(["market_code", "trade_date"], inplace=True)
    df.set_index(["market_code", "trade_date"], inplace=True)
    return df
