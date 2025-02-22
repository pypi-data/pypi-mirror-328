# ------------------查询相关接口-------------------------------
import re
import time

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from . import dataApi
from .dataApi import DataApi
from .enum import Exchange, get_exchange_value
from .enum import Variety, get_variety_value

self = None
user = ''
token = ''
api = None


class APIManager:
    _instance = None

    def __new__(cls, user='', token='', timeout=300):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            if user == '' and token == '':
                global api
                cls._instance.api = api
            else:
                cls._instance.api = DataApi(user, token, timeout=timeout)
        return cls._instance


def init(user='', token=''):
    DataApi.user = user;
    DataApi.token = token;
    global api
    api = DataApi(user, token, timeout=300)


def __init__(self, user, token, timeout=300):
    self.__timeout = timeout


def pro_api(user='', token='', timeout=300):
    """
    初始化pro API,第一次可以通过set_token('your token')来记录自己的token凭证，临时token可以通过本参数传入
    """
    pro = dataApi.DataApi(user='', token=token, timeout=timeout)
    return pro


def turnToStampTime(str):
    s_t = time.strptime(str, "%Y-%m-%d %H:%M:%S")
    # print(s_t)
    return int(time.mktime(s_t)) * 1000


def formatTime(str):
    return time.strptime(str, "%Y-%m-%d %H:%M:%S")


def freqline(freq):
    freqdict = {
        '1d': 1,
        '5m': 48,
        '10m': 24,
        '15m': 16,
        '30m': 8,
        '60m': 4
    }
    return freqdict.get(freq, 1)


date_patterns = {
    'YYYY-MM-DD': r'^(20[0-9][0-9]|19[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$',
    'hh:mm:ss': r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$',
    'ms': f'^[0-9][0-9][0-9]$'
}


def valid_date(date_string):
    if date_string == '0':
        return True;
    if ' ' in date_string:
        dateArray = date_string.split(' ')
        if len(dateArray[0]) != 10:
            return False;
        else:
            if re.match(date_patterns['YYYY-MM-DD'], dateArray[0]):
                if '.' in dateArray[1]:
                    timeArray = dateArray[1].split('.')
                    if len(timeArray[0]) != 8:
                        return False;
                    else:
                        if re.match(date_patterns['hh:mm:ss'], timeArray[0]):
                            if len(timeArray[1]) != 3:
                                print('毫秒错误' + timeArray[1])
                                return False
                            else:
                                return True

                        else:
                            print('时分秒错误' + timeArray[0])
                            return False
                else:
                    if len(dateArray[1]) != 8:
                        print('时分秒错误' + dateArray[1])
                        return False;
                    else:
                        if re.match(date_patterns['hh:mm:ss'], dateArray[1]):
                            return True
                        else:
                            print('时分秒错误' + dateArray[1])
                            return False

            else:
                return False
    else:
        if len(date_string) != 10:
            return False;
        else:
            if re.match(date_patterns['YYYY-MM-DD'], date_string):
                return True
            else:
                print('日期错误' + date_string)
                return False


def chunk_array(arr, size):
    return [arr[i:i + size] for i in range(0, len(arr), size)]


def check_duplicate(df, code, subset):
    if not is_success_code(code):
        return df
    if not isinstance(df, pd.DataFrame):
        return df
    if df.shape[0] == 0:
        return df
    for col in subset:
        if col not in df.columns:
            return df
    dup_row = df[df.duplicated(subset=subset, keep=False)].sort_values(by=subset)
    if dup_row.shape[0] >= 2:
        print(f"ex_row: {dup_row.iloc[0]}, {dup_row.iloc[1]}")
        row_cnt_init = df.shape[0]
        df = df.drop_duplicates(subset=subset)
        row_cnt = df.shape[0]
        print(f"row dup {row_cnt_init} to {row_cnt}")
    return df


def is_success_code(code):
    if hasattr(code, 'name'):
        if code.name != 'SUCCESS':
            return False
        else:
            return True
    else:
        if code != '00000':
            return False
        else:
            return True


PRICE_COLS = ['open_price', 'close_price', 'high_price', 'low_price']

FORMAT = lambda x: '%.2f' % x


def to_query(apiName,
             symbols,
             start_time,
             end_time,
             fields=None,
             limit=None,
             df=True
             ):
    if not valid_date(start_time) or not valid_date(end_time):
        return '', 000, '格式不正确'

    data, code, msg = APIManager().api.query(apiName,
                                             fields=fields,
                                             start_time=start_time,
                                             end_time=end_time,
                                             symbols=symbols,
                                             limit=limit,
                                             df=df)
    return data, code, msg


def to_query_by_batch(apiName,
                      symbols,
                      start_time=None,
                      end_time=None,
                      fields=None,
                      limit=None,
                      df=True
                      ):
    if (len(symbols) > 200):
        market_code_arr = chunk_array(symbols, 200)
        dataTotal = pd.DataFrame;
        dataFrames = []
        for market_code_tmp in market_code_arr:
            data, code, msg = APIManager().api.query(api_name=apiName, fields=fields, symbols=market_code_tmp,
                                                     start_time=start_time,
                                                     end_time=end_time,
                                                     limit=limit,
                                                     df=df)
            if not is_success_code(code):
                return data, code, msg;
            else:
                dataFrames.append(data);
        dataTotal = pd.concat(dataFrames, ignore_index=True)
        return dataTotal, code, msg;
    else:
        data, code, msg = APIManager().api.query(api_name=apiName, fields=fields, symbols=symbols, limit=limit,
                                                 start_time=start_time,
                                                 end_time=end_time,
                                                 df=df)
        return data, code, msg;


def get_kline_by_date(market_code,
                      frequency,
                      start_time,
                      end_time,
                      fields=None,
                      skip_suspended=True,
                      fill_missing=None,
                      variety='stock',
                      adj=None,
                      limit=None,
                      batch='',
                      df=True):
    dataTotal = pd.DataFrame;
    dataFrames = []
    api = DataApi(DataApi.user, DataApi.token, timeout=300)
    # 将字符串转换为日期对象
    start_date = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_date = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    # 计算年份差
    year_diff = end_date.year - start_date.year

    # 计算是否分年
    if len(market_code) * 250 * year_diff > 30000:
        # 按年拆分时间段
        i = 0
        for i in range(year_diff + 1):
            # 计算每年的结束日期
            if i < year_diff:
                year_end_date = start_date.replace(year=start_date.year + 1, month=1, day=1) - timedelta(days=1)
            else:
                year_end_date = end_date

            data, code, msg = get_kline_batch(market_code=market_code,
                                              frequency=frequency,
                                              start_time=start_date.strftime('%Y-%m-%d %H:%M:%S'),
                                              end_time=year_end_date.strftime('%Y-%m-%d %H:%M:%S'),
                                              fields=fields,
                                              skip_suspended=skip_suspended,
                                              fill_missing=fill_missing,
                                              variety=variety,
                                              adj=adj,
                                              limit=limit,
                                              batch=100,
                                              df=df)
            if not is_success_code(code):
                return data, code, msg;
            else:
                dataFrames.append(data);
                # 更新开始日期为下一年的第一天
            start_date = start_date.replace(year=start_date.year + 1, month=1, day=1)

        dataTotal = pd.concat(dataFrames, ignore_index=True)
    else:
        dataTotal, code, msg = get_kline(market_code=market_code,
                                         frequency=frequency,
                                         start_time=start_time,
                                         end_time=end_time,
                                         fields=fields,
                                         skip_suspended=skip_suspended,
                                         fill_missing=fill_missing,
                                         variety=variety,
                                         adj=None,
                                         limit=limit,
                                         df=df)
    dataTotal = check_duplicate(dataTotal, code, ['orig_time', 'symbol'])
    return dataTotal, code, msg;


def get_kline_batch(market_code,
                    frequency,
                    start_time,
                    end_time,
                    fields=None,
                    skip_suspended=True,
                    fill_missing=None,
                    variety='stock',
                    adj=None,
                    limit=None,
                    batch='',
                    df=True):
    '''
    分批获取kline数据

    :param market_code: 标的名称,格式如[‘600000.SH，600004.SH’]
    :param frequency: k线周期，格式如1D表示日线，5m表示5分钟线
    :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
    :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
    :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
    :param skip_suspended: 是否跳过停牌, 默认True,跳过停牌
    :param fill_missing: 填充方式, None - 不填充, 'NaN' - 用空值填充，默认 None
    :param limit: 查询条数，默认None, 返回全部查询内容，例如limit=100,表示返回100条数据
    :param batch: 分批条数，表示每批次查询的标的数
    :param df: 返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    if not valid_date(start_time) or not valid_date(end_time):
        return '', 000, '格式不正确'

    limit_ceil = 90000
    if not limit or limit > limit_ceil:
        limit = limit_ceil
    if batch == "":
        start_date = datetime.strptime(start_time[:10], "%Y-%m-%d")
        end_date = datetime.strptime(end_time[:10], "%Y-%m-%d")
        gap_days = (end_date - start_date).days
        if gap_days < 0:
            return None, -1, '时间参数错误'
        batch = limit // int((gap_days * freqline(frequency) / 360 * 250))
    if (batch != "" and len(market_code) > batch):
        market_code_arr = chunk_array(market_code, batch)
        dataTotal = pd.DataFrame;
        dataFrames = []
        for market_code_tmp in market_code_arr:
            data, code, msg = APIManager().api.query('queryKLines',
                                                     fields=fields,
                                                     start_time=start_time,
                                                     end_time=end_time,
                                                     symbols=market_code_tmp,
                                                     frequency=frequency,
                                                     variety=get_variety_value(variety),
                                                     adj=adj,
                                                     limit=limit,
                                                     df=df)
            if not is_success_code(code):
                return data, code, msg;
            else:
                dataFrames.append(data);
        dataTotal = pd.concat(dataFrames, ignore_index=True)
        dataTotal = check_duplicate(dataTotal, code, ['orig_time', 'symbol'])
        return dataTotal, code, msg;
    else:
        data, code, msg = APIManager().api.query('queryKLines',
                                                 fields=fields,
                                                 start_time=start_time,
                                                 end_time=end_time,
                                                 symbols=market_code,
                                                 frequency=frequency,
                                                 variety=get_variety_value(variety),
                                                 adj=adj,
                                                 limit=limit,
                                                 df=df)
        data = check_duplicate(data, code, ['orig_time', 'symbol'])
        return data, code, msg;


def get_kline(market_code,
              frequency,
              start_time,
              end_time,
              fields=None,
              skip_suspended=True,
              fill_missing=None,
              variety='stock',
              adj=None,
              limit=None,
              df=True):
    '''
    获取Kline
    :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
    :param frequency: k线周期，格式如1D表示日线，5m表示5分钟线
    :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
    :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
    :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
    :param skip_suspended: 是否跳过停牌, 默认True,表示跳过停牌
    :param fill_missing: 填充方式, None - 不填充, 'NaN' - 用空值填充，默认 None
    :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
    :param adj: 复权类型,None不复权,pre:前复权,post:后复权
    :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    if not valid_date(start_time) or not valid_date(end_time):
        return '', 000, '格式不正确'
    if fields != None:
        fields = fields + ['symbol', 'orig_time']

    data, code, msg = get_kline_batch(
        market_code=market_code,
        frequency=frequency,
        start_time=start_time,
        end_time=end_time,
        fields=fields,
        skip_suspended=skip_suspended,
        fill_missing=fill_missing,
        variety=variety,
        adj=adj,
        limit=limit,
        batch="",
        df=df
    )
    '''
    data, code, msg = APIManager().api.query('queryKLines',
                                fields=fields,
                                start_time=start_time,
                                end_time=end_time,
                                symbols=market_code,
                                frequency=frequency,
                                limit=limit,
                                variety=get_variety_value(variety),
                                df=df)
    '''
    if adj is not None:
        # 批量查询复权因子
        fcts, code_fcts, msg_fcts = exfactor(market_code=market_code, start_time=start_time, end_time=end_time)
        # 查询有误返回原Kline
        if not is_success_code(code_fcts):
            return data, code, msg;
        if fcts.shape[0] == 0:
            return data, code, msg;
        data["orig_time_key"] = pd.to_datetime(
            data["orig_time"]
        ).dt.strftime('%Y-%m-%d')
        data["new_key"] = data["symbol"] + data["orig_time_key"]
        fcts["ex_date"] = pd.to_datetime(fcts['ex_date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
        fcts["new_key"] = fcts["market_code"] + fcts["ex_date"]
        # 填充复权因子
        data = data.set_index(['new_key'], drop=False).merge(fcts.set_index(['new_key']), left_index=True,
                                                             right_index=True, how='left')
        data.sort_values(['symbol', 'orig_time_key'], ascending=False)
        data['cum_factor'] = data['cum_factor'].fillna(method='ffill')
        # 没有复权因子回填1
        data['cum_factor'] = data['cum_factor'].fillna(value=1)

        if adj == 'post':
            data["cum_factor"] = data["cum_factor"].astype(float)

        # 针对前复权，需要查询出最新的复权因子
        if adj == 'pre':
            new_fcts, new_fcts_code, new_fcts_msg = exfactor(market_code=market_code, start_time='0', end_time='0')
            if not is_success_code(new_fcts_code):
                return data, code, msg;
            new_fcts = new_fcts.sort_values('ex_date', ascending=False)
            new_factor = new_fcts.groupby('market_code')['cum_factor'].first()
            data = data.set_index(['symbol'], drop=False).merge(new_factor, left_index=True,
                                                                right_index=True, how='left')
            data['cum_factor_x'] = data['cum_factor_x'].fillna(method='ffill')
            data['cum_factor_y'] = data['cum_factor_y'].fillna(value=1)
            data["cum_factor_x"] = data["cum_factor_x"].astype(float)
            data["cum_factor_y"] = data["cum_factor_y"].astype(float)
        if fields != None:
            need_adj_cols = set(fields) & set(PRICE_COLS)
        else:
            need_adj_cols = set(PRICE_COLS)
        for col in need_adj_cols:
            data[col] = data[col].astype(float)
            if adj == 'post':
                data[col] = data[col] * data["cum_factor"]
            if adj == 'pre':
                data[col] = data[col] * data['cum_factor_x'] / data['cum_factor_y']
            data[col] = data[col].map(FORMAT)
            data[col] = data[col].astype(float)
        if fields != None:
            data = data[fields]
        data.reset_index(drop=True)
        data = check_duplicate(data, code, ['orig_time', 'symbol'])
        return data, code, msg;

    else:
        data = check_duplicate(data, code, ['orig_time', 'symbol'])
        return data, code, msg;


def get_kline_combine(klines,
                      exfactors,
                      adj=None):
    if adj == None:
        return klines;
    else:
        if exfactors.shape[0] == 0:
            return klines;
        klines["orig_time_key"] = pd.to_datetime(
            klines["orig_time"]
        ).dt.strftime('%Y-%m-%d')
        klines["new_key"] = klines["symbol"] + klines["orig_time_key"]
        try:
            exfactors["ex_date"] = pd.to_datetime(exfactors['ex_date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
        except ValueError:
            pass
        # exfactors["ex_date"] = pd.to_datetime(exfactors['ex_date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
        exfactors["new_key"] = exfactors["market_code"] + exfactors["ex_date"]
        # 填充复权因子
        klines = klines.set_index(['new_key'], drop=False).merge(exfactors.set_index(['new_key']), left_index=True,
                                                                 right_index=True, how='left')
        klines.sort_values(['symbol', 'orig_time_key'], ascending=False)
        klines['cum_factor'] = klines['cum_factor'].fillna(method='ffill')
        # 没有复权因子回填1
        klines['cum_factor'] = klines['cum_factor'].fillna(value=1)

        if adj == 'post':
            klines["cum_factor"] = klines["cum_factor"].astype(float)

        # 针对前复权，需要查询出最新的复权因子
        if adj == 'pre':
            exfactors = exfactors.sort_values('ex_date', ascending=False)
            exfactors = exfactors.groupby('market_code')['cum_factor'].first()
            klines = klines.set_index(['symbol'], drop=False).merge(exfactors, left_index=True,
                                                                    right_index=True, how='left')
            klines['cum_factor_x'] = klines['cum_factor_x'].fillna(method='ffill')
            klines['cum_factor_y'] = klines['cum_factor_y'].fillna(value=1)
            klines["cum_factor_x"] = klines["cum_factor_x"].astype(float)
            klines["cum_factor_y"] = klines["cum_factor_y"].astype(float)

        need_adj_cols = set(PRICE_COLS)
        for col in need_adj_cols:
            klines[col] = klines[col].astype(float)
            if adj == 'post':
                klines[col] = klines[col] * klines["cum_factor"]
            if adj == 'pre':
                klines[col] = klines[col] * klines['cum_factor_x'] / klines['cum_factor_y']
            klines[col] = klines[col].map(FORMAT)
            klines[col] = klines[col].astype(float)
        if adj == 'pre':
            klines.drop(['cum_factor_x', 'cum_factor_y'], axis=1, inplace=True)
        if adj == 'post':
            klines.drop('cum_factor', axis=1, inplace=True)
        klines.drop(['ex_date', 'ex_factor', 'orig_time_key', 'new_key', 'market_code', 'security_code_y'], axis=1,
                    inplace=True)

        klines.reset_index(drop=True)
        return klines;


def get_snapshot(market_code,
                 start_time,
                 end_time,
                 fields=None,
                 skip_suspended=True,
                 fill_missing=None,
                 adjust=0,
                 limit=None,
                 variety='stock',
                 df=True):
    '''
    获取快照行情
    :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
    :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
    :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
    :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
    :param skip_suspended: 是否跳过停牌, 默认True,表示跳过停牌
    :param fill_missing: 填充方式, None - 不填充, 'NaN' - 用空值填充，默认 None
    :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
    :param variety: 证券类型，默认None, 表示全部，variety='stock',表示返回股票类型
    :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    if fields != None:
        fields = fields + ['symbol', 'orig_time']
    data, code, msg = APIManager().api.query('querySnapshot',
                                             fields=fields,
                                             start_time=start_time,
                                             end_time=end_time,
                                             symbols=market_code,
                                             limit=limit,
                                             variety=get_variety_value(variety),
                                             df=df)
    if adjust == 0:
        return data, code, msg;
    else:
        ex_data, ex_code, ex_msg = to_query('exfactor', fields=fields, symbols=market_code, start_time=start_time,
                                            end_time=end_time, limit=limit, df=df)


def get_tick_execution(market_code,
                       start_time,
                       end_time,
                       fields=None,
                       limit=None,
                       variety='stock',
                       df=True
                       ):
    '''
     获取逐笔成交
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    '''
    if fields != None:
        fields = fields + ['symbol', 'exec_time']
    data, code, msg = APIManager().api.query('queryExecution',
                                             fields=fields,
                                             start_time=start_time,
                                             end_time=end_time,
                                             symbols=market_code,
                                             limit=limit,
                                             variety=get_variety_value(variety),
                                             df=df)
    return data, code, msg;


def get_tick_order(market_code,
                   start_time,
                   end_time,
                   limit=None,
                   fields=None,
                   variety='stock',
                   df=True):
    '''
     获取逐笔委托数据
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
     :return:
    '''
    if fields != None:
        fields = fields + ['symbol', 'order_time']

    data, code, msg = APIManager().api.query('queryTickOrder',
                                             fields=fields,
                                             start_time=start_time,
                                             end_time=end_time,
                                             symbols=market_code,
                                             limit=limit,
                                             variety=get_variety_value(variety),
                                             df=df)
    return data, code, msg;


def get_index_price(index_code,
                    start_time,
                    end_time,
                    fields=None,
                    limit=None,
                    df=True):
    '''
    获取指数数据
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
     :return:
    '''
    # return to_query('querySnapshot', df=df, fields=fields, symbols=index_code, start_time=start_time,
    #                 end_time=end_time, limit=limit)

    data, code, msg = APIManager().api.query('queryKLines',
                                             fields=fields,
                                             start_time=start_time,
                                             end_time=end_time,
                                             symbols=index_code,
                                             limit=limit,
                                             variety=get_variety_value('index'),
                                             df=df)
    return data, code, msg;


def get_orderqueue(market_code,
                   start_time,
                   end_time,
                   fields=None,
                   limit=None,
                   df=True):
    '''
    获取委托队列
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
     :return:
    '''
    return to_query_by_batch('queryOrderQueue', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, df=df, limit=limit)


def get_price(market_code,
              frequency,
              start_time,
              end_time,
              fields=None,
              skip_suspended=True,
              fill_missing=None,
              variety='stock',
              adj=None,
              limit=None,
              offset=0,
              df=True):
    '''
    获取Kline
    :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
    :param frequency: k线周期，格式如1D表示日线，5m表示5分钟线
    :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
    :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
    :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
    :param skip_suspended: 是否跳过停牌, 默认True,表示跳过停牌
    :param fill_missing: 填充方式, None - 不填充, 'NaN' - 用空值填充，默认 None
    :param variety: 证券类型，默认None, 表示全部，variety='stock',表示返回股票类型
    :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
    :param offset: 查询开始条数，默认0, 从第一条开始返回，offset=100,表示从101条开始返回
    :param adj: 复权类型,none不复权,pre:前复权,post:后复权
    :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    if not valid_date(start_time) or not valid_date(end_time):
        return '', 000, '格式不正确'
    # if fields!=None:
    #     fields = fields+['market_code','orig_time']

    data, code, msg = APIManager().api.query('get_price',
                                             fields=fields,
                                             start_time=start_time,
                                             end_time=end_time,
                                             symbols=market_code,
                                             frequency=frequency,
                                             skip_suspended=skip_suspended,
                                             fill_missing=fill_missing,
                                             limit=limit,
                                             offeset=offset,
                                             variety=get_variety_value(variety),
                                             df=df)

    if not (variety == 'stock' or variety == 'all' or variety == 'none'):
        return data, code, msg

    if adj is not None:
        # 批量查询复权因子
        fcts, code_fcts, msg_fcts = exfactor(market_code=market_code, start_time=start_time, end_time=end_time)
        # 查询有误返回原Kline
        if not is_success_code(code_fcts):
            return data, code, msg;
        if fcts.shape[0] == 0:
            return data, code, msg;
        fcts = fcts.rename(columns={"market_code": "symbol"})
        data["new_key"] = data["market_code"] + data["orig_time"].astype(str)
        # fcts["ex_date"]=pd.to_datetime(fcts['ex_date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
        fcts["ex_date"] = fcts['ex_date'] + "000000"
        fcts["new_key"] = fcts["symbol"] + fcts["ex_date"]
        # 填充复权因子
        data = data.set_index(['new_key'], drop=False).merge(fcts.set_index(['new_key']), left_index=True,
                                                             right_index=True, how='left')
        data.sort_values(['market_code', 'orig_time'], ascending=False)
        data['cum_factor'] = data['cum_factor'].fillna(method='ffill')
        # 没有复权因子回填1
        data['cum_factor'] = data['cum_factor'].fillna(value=1)

        if adj == 'post':
            data["cum_factor"] = data["cum_factor"].astype(float)

        # 针对前复权，需要查询出最新的复权因子
        if adj == 'pre':
            new_fcts, new_fcts_code, new_fcts_msg = exfactor(market_code=market_code, start_time='0', end_time='0')
            if not is_success_code(new_fcts_code):
                return data, code, msg;
            new_fcts = new_fcts.sort_values('ex_date', ascending=False)
            new_factor = new_fcts.groupby('market_code')['cum_factor'].first()
            data = data.set_index(['market_code'], drop=False).merge(new_factor, left_index=True,
                                                                     right_index=True, how='left')
            data['cum_factor_x'] = data['cum_factor_x'].fillna(method='ffill')
            data['cum_factor_y'] = data['cum_factor_y'].fillna(value=1)
            data["cum_factor_x"] = data["cum_factor_x"].astype(float)
            data["cum_factor_y"] = data["cum_factor_y"].astype(float)
        if fields != None:
            need_adj_cols = set(fields) & set(PRICE_COLS)
        else:
            need_adj_cols = set(PRICE_COLS)
        for col in need_adj_cols:
            data[col] = data[col].astype(float)
            if adj == 'post':
                data[col] = data[col] * data["cum_factor"]
            if adj == 'pre':
                data[col] = data[col] * data['cum_factor_x'] / data['cum_factor_y']
            data[col] = data[col].map(FORMAT)
            data[col] = data[col].astype(float)
        if fields != None:
            data = data[fields]
        data.reset_index(drop=True)
        if adj == 'pre':
            data.drop(['ex_date', 'ex_factor', 'cum_factor_x', 'new_key', 'symbol', 'cum_factor_y', 'security_code'],
                      axis=1,
                      inplace=True)
        elif adj == 'post':
            data.drop(['ex_date', 'ex_factor', 'cum_factor', 'new_key', 'symbol', 'security_code'],
                      axis=1, inplace=True)
        return data, code, msg;

    else:
        return data, code, msg;


# ------------------查询资讯相关接口-------------------------------
def stock_basic(
        market_code,
        fields=None,
        limit=None,
        df=True
):
    '''
    股票基础信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
     :return:
    '''
    return to_query_by_batch('stock_basic', fields=fields, symbols=market_code, limit=limit, df=df)


def index_basic(
        market_code,
        fields=None,
        limit=None,
        df=True
):
    '''
    股票基础信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
     :return:
    '''
    return to_query_by_batch('index_basic', fields=fields, symbols=market_code, limit=limit, df=df)


def industry(
        market_code,
        fields=None,
        limit=None,
        df=True
):
    '''
    行业分类信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
     :return:
    '''

    # data, code, msg = api.query('industry', fields=fields, symbols=market_code,limit=limit, df=df)
    # return data, code, msg;
    return to_query_by_batch('industry', fields=fields, symbols=market_code, limit=limit, df=df)


def company(
        market_code,
        fields=None,
        limit=None,
        df=True
):
    '''
    公司简介信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('company', fields=fields, symbols=market_code, limit=limit, df=df)


def sharehold(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
     股本信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
   :return:
   '''
    return to_query_by_batch('sharehold', symbols=market_code, start_time=start_time, end_time=end_time, fields=fields,
                             limit=limit, df=df)


def segment(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    公司主营业务信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('segment', symbols=market_code, start_time=start_time, end_time=end_time, fields=fields,
                             limit=limit, df=df)


def historysymbollist(
        start_time='',
        end_time='',
        variety='',
        limit=None,
        df=True
):
    '''
    历史股票列表信息
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param variety: 证券类型，默认None, 表示全部，variety='stock',表示返回股票类型
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    if not valid_date(start_time) or not valid_date(end_time):
        return '', 000, '格式不正确'
    data, code, msg = APIManager().api.query('historysymbollist',
                                             variety=get_variety_value(variety),
                                             start_time=start_time,
                                             end_time=end_time,
                                             limit=limit,
                                             fields=None,
                                             df=df)
    return data, code, msg;


def stock_ipo(
        market_code,
        fields=None,
        limit=None,
        df=True
):
    '''
    首次公开发行信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    # data, code, msg = APIManager().api.query('stock-ipo', fields=fields, symbols=market_code, limit=limit, df=df)
    # return data, code, msg;
    return to_query_by_batch('stock-ipo', fields=fields, symbols=market_code, limit=limit, df=df)


def listmore(
        market_code,
        fields=None,
        limit=None,
        df=True
):
    '''
    增发数据信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    # data, code, msg = APIManager().api.query('listmore', fields=fields, symbols=market_code, limit=limit, df=df)
    # return data, code, msg;
    return to_query_by_batch('listmore', fields=fields, symbols=market_code, limit=limit, df=df)


def divident(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    股票分红信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('divident', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def allotment(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    股票配股信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('allotment', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def exdiv(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    股票除权除息信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('exdiv', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def exfactor(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    复权因子表信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('exfactor', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def forward_backward_factor(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    复权因子表信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    fcts, fcts_code, fcts_msg = exfactor(market_code=market_code, start_time=start_time, end_time=end_time)
    if not is_success_code(fcts_code):
        return fcts, fcts_code, fcts_msg;
    new_fcts, new_fcts_code, new_fcts_msg = exfactor(market_code=market_code, start_time='0', end_time='0')

    if not is_success_code(new_fcts_code):
        return fcts, fcts_code, fcts_msg;
    new_fcts = new_fcts.sort_values(['ex_date', 'market_code'], ascending=False)
    new_factor = new_fcts.groupby('market_code')['cum_factor'].first()
    fcts = fcts.set_index(['market_code'], drop=False).merge(new_factor, left_index=True,
                                                             right_index=True, how='left')
    fcts['cum_factor_x'] = fcts['cum_factor_x'].fillna(method='ffill')
    fcts['cum_factor_y'] = fcts['cum_factor_y'].fillna(value=1)
    fcts["cum_factor_x"] = fcts["cum_factor_x"].astype(float)
    fcts["cum_factor_y"] = fcts["cum_factor_y"].astype(float)
    fcts = fcts.rename(columns={'cum_factor_x': 'barkward'})
    fcts['forward'] = fcts['barkward'] / fcts['cum_factor_y']
    return fcts, fcts_code, fcts_msg;


def top10holders(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    A股十大股东名单
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('top10holders', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def restricted_free(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    限售股解禁明细
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('restricted_free', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def freefloat(
        market_code,
        limit=None,
        fields=None,
        df=True
):
    '''
    解禁数据
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('freefloat', fields=fields, symbols=market_code, limit=limit, df=df)


def pledge(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    股权持股冻结/质押情况信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('pledge', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def balancesheet(
        market_code,
        start_time,
        end_time,
        limit=None,
        fields=None,
        df=True
):
    '''
    A股一般企业资产负债表
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('balancesheet', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def income(market_code,
           start_time,
           end_time,
           limit=None,
           fields=None,
           df=True
           ):
    '''
    A股一般企业利润表
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('income', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def cashflow(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    A股一般企业现金流表
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('cashflow', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def fina_forecast(
        market_code,
        start_time='0',
        end_time='0',
        fields=None,
        limit=None,
        df=True
):
    '''
    A股财务指标
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('fina_forecast', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def current_performance(
        market_code,
        start_time='0',
        end_time='0',
        fields=None,
        limit=None,
        df=True
):
    '''
    A股财务指标
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('current_performance', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def fina_indicator(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    A股财务指标
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('fina_indicator', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def fina_indicator_derive(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    A股财务衍生指标
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('fina_indicator_derive', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def trade_calendar(
        market,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    交易日历
     :param market:交易市场名称，交易所 SH上交所 SZ深交所 BJ 北交所
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    if not valid_date(start_time) or not valid_date(end_time):
        return '', 000, '格式不正确'

    data, code, msg = APIManager().api.query('trade_calendar', fields=fields, market_type=get_exchange_value(market),
                                             # start_time=turnToStampTime(start_time),
                                             # end_time=turnToStampTime(end_time),
                                             start_time=start_time,
                                             end_time=end_time,
                                             df=df)
    return data, code, msg;


def block_trade(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    大宗交易数据
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('block_trade', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def split(
        market_code,
        start_time='0',
        end_time='0',
        fields=None,
        limit=None,
        df=True
):
    '''
    A股拆分股信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('split', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def st_days(
        market_code,
        start_time='0',
        end_time='0',
        fields=None,
        limit=None,
        df=True
):
    '''
    A股ST日期
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('st_days', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def get_suspended_days(
        market_code,
        start_time='0',
        end_time='0',
        fields=None,
        limit=None,
        df=True
):
    '''
    A股ST日期
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('suspended_days', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def get_industry(
        industry,
        datasource,
        date,
        fields=None,
        limit=None,
        df=True
):
    '''
    查询行业成分股
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    data, code, msg = APIManager().api.query('get_industry',
                                             fields=fields,
                                             industry=industry,
                                             industryType=datasource,
                                             date=date,
                                             limit=limit,
                                             df=df)
    return data, code, msg


def get_concept(
        concept,
        date,
        fields=None,
        limit=None,
        df=True
):
    '''
    查询行业成分股
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    data, code, msg = APIManager().api.query('get_concept',
                                             fields=fields,
                                             concept=concept,
                                             date=date,
                                             limit=limit,
                                             df=df)
    return data, code, msg


def top_inst(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    机构龙虎榜
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('top_inst', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def margin_detail(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    融资融券交易明细信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('margin_detail', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df);


def margin(
        market,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    融资融券成交汇总信息
     :param market:交易市场名称，交易所 SH上交所 SZ深交所 BJ 北交所
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    if not valid_date(start_time) or not valid_date(end_time):
        return '', 000, '格式不正确'

    data, code, msg = APIManager().api.query('margin', fields=fields, market_type=get_exchange_value(market),
                                             # start_time=turnToStampTime(start_time),
                                             # end_time=turnToStampTime(end_time),
                                             start_time=start_time,
                                             end_time=end_time,
                                             limit=limit, df=df)
    return data, code, msg;


def fund_indicator(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    基金最新指标信息
     :param market_code:标的名称,格式如[‘510300.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('fund_indicator', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def index_con(
        index_code,
        fields=None,
        df=True,
        limit=None
):
    '''
    A股指数成分股
    :param index_code:指数名称,格式如[‘399001.SZ’]
    :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
    :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
    :param fields:查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
    :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    data, code, msg = APIManager().api.query('index_con', fields=fields, symbols=index_code, limit=limit, df=df)
    return data, code, msg;


def index_con_his(
        index_code,
        start_time,
        end_time,
        fields=None,
        df=True,
        limit=None
):
    '''
    A股指数成分股
    :param index_code:指数名称,格式如[‘399001.SZ’]
    :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
    :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
    :param fields:查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
    :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    data, code, msg = APIManager().api.query('index_con_his', fields=fields, symbols=index_code, start_time=start_time,
                                             end_time=end_time, limit=limit, df=df)
    return data, code, msg;


def fut_basic(
        contract_flag,
        contract_variety,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    期货合约信息
    :param contract_flag:期货合约
    :param contract_variety:期货品种类型
    :param start_time:查询开始日期,格式如‘2024-01-01’
    :param end_time:查询结束日期,格式如‘2024-01-01’
    :param fields:查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
    :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    if not valid_date(start_time) or not valid_date(end_time):
        return '', 000, '格式不正确'

    data, code, msg = APIManager().api.query('fut_basic', fields=fields, contract_flag=contract_flag,
                                             contract_variety=contract_variety,
                                             # start_time=turnToStampTime(start_time),
                                             # end_time=turnToStampTime(end_time),
                                             start_time=start_time,
                                             end_time=end_time,
                                             limit=limit, df=df)
    return data, code, msg;


def fut_daily(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    期货交易日行情
    :param market_code:标的名称,格式如‘’
    :param start_time:查询开始日期,格式如‘2024-01-01’
    :param end_time:查询结束日期,格式如‘2024-01-01’
    :param fields:查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
    :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('fut_daily', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def get_factor_by_date(
        factor_name,
        start_time,
        end_time,
        freq,
        symbol_pool,
        market_code=[],
        df=True
):
    '''
    获取因子
    :param factor_name:因子名称,格式如‘MA5’
    :param start_time:查询开始日期,格式如‘2024-01-01’
    :param end_time:查询结束日期,格式如‘2024-01-01’
    :param freq: 数据周期，格式如1D表示日线
    :param symbol_pool:股票池，格式如‘000300.SH’
    :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
    :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    '''
    dataTotal = pd.DataFrame;
    dataFrames = []
    api = DataApi(DataApi.user, DataApi.token, timeout=300)
    # 将字符串转换为日期对象
    start_date = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_date = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    # 计算年份差
    year_diff = end_date.year - start_date.year

    # 按年拆分时间段
    i = 0
    for i in range(year_diff + 1):
        # 计算每年的结束日期
        if i < year_diff:
            year_end_date = start_date.replace(year=start_date.year + 1, month=1, day=1) - timedelta(days=1)
        else:
            year_end_date = end_date
        # 打印每年的时间段
        # print(f"From: {start_date.strftime('%Y-%m-%d')} To: {year_end_date.strftime('%Y-%m-%d')}")
        data, code, msg = get_factor(
            factor_name=factor_name,
            start_time=start_date.strftime('%Y-%m-%d %H:%M:%S'),
            end_time=year_end_date.strftime('%Y-%m-%d %H:%M:%S'),
            freq=freq,
            symbol_pool=symbol_pool,
            market_code=market_code,
            df=df,
            code_per_req=None,
            limit=100000
        )
        if code == "-1":
            return data, code, msg;
        else:
            dataFrames.append(data);
            # 更新开始日期为下一年的第一天
        start_date = start_date.replace(year=start_date.year + 1, month=1, day=1)

    dataTotal = pd.concat(dataFrames, ignore_index=True)
    dataTotal = check_duplicate(dataTotal, code, ['data_time', 'security_code'])
    return dataTotal, code, msg


def get_factor_by_security(
        factor_name,
        start_time,
        end_time,
        freq,
        symbol_pool,
        market_code=[],
        df=True,
        code_per_req=None,
        limit=100000
):
    '''
    获取因子
    :param factor_name:因子名称,格式如‘MA5’
    :param start_time:查询开始日期,格式如‘2024-01-01’
    :param end_time:查询结束日期,格式如‘2024-01-01’
    :param freq: 数据周期，格式如1D表示日线
    :param symbol_pool:股票池，格式如‘000300.SH’
    :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
    :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    '''
    if not valid_date(start_time) or not valid_date(end_time):
        return '', 000, '格式不正确'

    limit_ceil = 120000
    if not limit or limit > limit_ceil:
        limit = limit_ceil
    start_date = datetime.strptime(start_time[:10], "%Y-%m-%d")
    end_date = datetime.strptime(end_time[:10], "%Y-%m-%d")
    gap_days = (end_date - start_date).days
    if gap_days < 0:
        return None, -1, '时间参数错误'
    if not code_per_req:
        code_per_req = limit // int((gap_days * freqline(freq) / 360 * 250))

    if code_per_req and len(market_code) > code_per_req:
        market_code_arr = chunk_array(market_code, code_per_req)
        dataFrames = []
        for market_code_tmp in market_code_arr:
            data, code, msg = APIManager().api.factor_query_with_batch('queryFactorById',
                                                                       security_code=market_code_tmp,
                                                                       start_date=start_time,
                                                                       end_date=end_time,
                                                                       symbol_pool=symbol_pool,
                                                                       freq=freq,
                                                                       name=factor_name,
                                                                       user_name=DataApi.user,
                                                                       df=df,
                                                                       # batch is required, indeed use limit
                                                                       batch={}, limit=limit)
            if not is_success_code(code):
                return data, code, msg;
            else:
                dataFrames.append(data);
        dataTotal = pd.concat(dataFrames, ignore_index=True)
        dataTotal = check_duplicate(dataTotal, code, ['data_time', 'security_code'])
        return dataTotal, code, msg;
    else:
        data, code, msg = APIManager().api.factor_query_with_batch('queryFactorById',
                                                                   security_code=market_code,
                                                                   start_date=start_time,
                                                                   end_date=end_time,
                                                                   symbol_pool=symbol_pool,
                                                                   freq=freq,
                                                                   name=factor_name,
                                                                   user_name=DataApi.user,
                                                                   df=df,
                                                                   batch={}, limit=limit)
        data = check_duplicate(data, code, ['data_time', 'security_code'])
        return data, code, msg


class DataError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def save_factor(
        factor_name,
        fval_df,
        symbol_pool,
        freq="1d",
        batch_size=1000,
):
    '''
    保存因子值到服务端
    :param fval_df:因子值矩阵，列为标的名称，行为时间格式(类型datetimes.DatetimeIndex)
    :param factor_name:因子名称,格式如‘MA5’
    :param start_time:查询开始日期,格式如‘2024-01-01’
    :param end_time:查询结束日期,格式如‘2024-01-01’
    :param freq: 数据周期，格式如1D表示日线
    :param symbol_pool:股票池，格式如‘000300.SH’
    '''
    factor = (
        fval_df.melt(
            col_level=0,
            value_vars=fval_df.columns,
            var_name="asset",
            value_name="factor",
            ignore_index=False,
        )
        .reset_index()
        .rename(
            columns={"dt": "data_time", "asset": "security_code", "factor": "value"}
        )
    )
    factor["symbol_pool"] = symbol_pool
    factor["name"] = f"{DataApi.user}.{factor_name}"
    factor = factor.replace(
        {np.nan: None, float("inf"): None, np.inf: None, -np.inf: None}
    )
    res = save_df(factor, DataApi.user, freq, batch_size)
    return res, 0, ''


def save_df(df, username, freq, batch_size=1000):
    df["data_time"] = df["data_time"].dt.strftime("%Y-%m-%d %H:%M:%S.%f").str[:-3]
    json_data = {"user_name": username, "freq": freq, "data": []}
    affected_rows = 0
    for i in range(0, df.shape[0], batch_size):
        json_data["data"] = df.iloc[i: i + batch_size].to_dict(orient="records")
        res, code, msg = APIManager().api.reqClient.post('save_factor', params=json_data)
        if not is_success_code(code):
            raise (DataError(f"code: {code}, msg: {msg}"))
        if "affected_rows" not in res:
            raise (DataError(f"no affected_rows, {res['data']}"))
        affected_rows += res["affected_rows"]
    return affected_rows


def get_factor(
        factor_name,
        start_time,
        end_time,
        freq,
        symbol_pool,
        market_code=[],
        df=True,
        code_per_req=None,
        limit=100000
):
    '''
    获取因子
    :param factor_name:因子名称,格式如‘MA5’
    :param start_time:查询开始日期,格式如‘2024-01-01’
    :param end_time:查询结束日期,格式如‘2024-01-01’
    :param freq: 数据周期，格式如1D表示日线
    :param symbol_pool:股票池，格式如‘000300.SH’
    :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
    :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    '''
    if not valid_date(start_time) or not valid_date(end_time):
        return '', 000, '格式不正确'

    limit_ceil = 120000
    if not limit or limit > limit_ceil:
        limit = limit_ceil
    dataTotal = pd.DataFrame;
    dataFrames = []
    api = DataApi(DataApi.user, DataApi.token, timeout=300)
    # 将字符串转换为日期对象
    start_date = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_date = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    # 计算年份差
    year_diff = end_date.year - start_date.year

    # 按年拆分时间段
    i = 0
    for i in range(year_diff + 1):
        # 计算每年的结束日期
        if i < year_diff:

            year_end_date = start_date.replace(year=start_date.year + 1, month=1, day=1) - timedelta(days=1)
        else:
            year_end_date = end_date
        data, code, msg = APIManager().api.factor_query_with_batch('queryFactorById',
                                                                   security_code=market_code,
                                                                   start_date=start_date.strftime('%Y-%m-%d'),
                                                                   end_date=year_end_date.strftime('%Y-%m-%d'),
                                                                   symbol_pool=symbol_pool,
                                                                   freq=freq,
                                                                   name=factor_name,
                                                                   user_name=DataApi.user,
                                                                   df=df,
                                                                   # batch is required, indeed use limit
                                                                   batch={}, limit=limit)
        if not is_success_code(code):
            return data, code, msg;
        else:
            dataFrames.append(data);
        # 更新开始日期为下一年的第一天
        start_date = start_date.replace(year=start_date.year + 1, month=1, day=1)
    dataTotal = pd.concat(dataFrames, ignore_index=True)
    dataTotal = check_duplicate(dataTotal, code, ['data_time', 'security_code'])
    return dataTotal, code, msg;


def ttm_mrq_factor(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
     获取ttm因子数据
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''
    return to_query_by_batch('ttm_mrq_factor', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def yield_factor(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    查询A股日收益率
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('yield_factor', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def derivind_factor(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
    查询A股日行情估值指标
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01，start_time='0',表示返回最新的
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01，end_time='0',表示返回最新的
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    return to_query_by_batch('derivind_factor', fields=fields, symbols=market_code, start_time=start_time,
                             end_time=end_time, limit=limit, df=df)


def dayprices(
        market_code,
        start_time='0',
        end_time='0',
        variety='stock',
        fields=None,
        limit=None,
        df=True
):
    data, code, msg = APIManager().api.query('dayprices',
                             fields=fields,
                             symbols=market_code,
                             variety=get_variety_value(variety),
                             start_time=start_time,
                             end_time=end_time,
                             limit=limit,
                             df=df)

    return data, code, msg
def allFactors(
        factorType='PRIVATE',
        fields=None,
        limit=None,
        df=True
):
    data, code, msg = APIManager().api.get_factor(api_name='queryListByType', fields=fields, factorType=factorType,

                                                  limit=limit,
                                                  df=df)
    return data, code, msg


def allFactorsList(
        factorType='PRIVATE',
        userName='gidtest',
        fields=None,
        limit=None,
        df=True
):
    data, code, msg = APIManager().api.get_factor(api_name='queryList', fields=fields, factorType=factorType,
                                                  userName=userName,
                                                  limit=limit,
                                                  df=df)
    return data, code, msg


def get_turnover_rate(market_code, start_time=None, end_time=None, fields=None, df=True):
    return to_query_by_batch('get_turnover_rate', fields=fields, symbols=market_code,
                             start_time=start_time, end_time=end_time, df=df)


def get_share_daily(
        market_code,
        start_time,
        end_time,
        fields=None,
        limit=None,
        df=True
):
    '''
     股本信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param start_time: 查询开始时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01 09:30:00，或者2024-01-01
     :param fields: 查询字段，输入查询字段列表，格式如['openPrice','closePrice']，默认是None，返回全部字段
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
   :return:
   '''
    return to_query_by_batch('queryShareDaily', symbols=market_code, start_time=start_time, end_time=end_time,
                             fields=fields,
                             limit=limit, df=df)


def get_code_change():
    '''
    股票代码变更信息
    :return: dataframe
    '''
    return to_query_by_batch('get_code_change', symbols=[])


def get_reserve_ratio(
        reserve_type='all',
        start_time='0',
        end_time='0',
        fields=None,
        limit=None,
        df=True
):
    if reserve_type == 'all':
        reserve = ['2', '3']
    if reserve_type == 'major':
        reserve = ['3']
    if reserve_type == 'other':
        reserve = ['2']

    data, code, msg = APIManager().api.query(api_name='reserveRatio', fields=fields, reserveType=reserve,
                                             start_time=start_time, end_time=end_time,
                                             limit=limit, df=df)
    return data, code, msg


def get_margin_stocks(
        exchange=['SH'],
        margin_type=None,
        date='0',
        fields=None,
        limit=None,
        df=True
):
    '''
     两融标的列表
     :param exchange: 交易所，格式如2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01
     :param fields: 查询字段，本接口暂不支持单独field查询，返回全部字段
     :param limit: 查询条数，本接口暂不支持分页查询, 返回全部查询内容
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
   :return:
   '''
    data, code, msg = APIManager().api.query(api_name='marginStocks', fields=fields, exchange=exchange,
                                             marginType=margin_type, date=date,
                                             limit=limit, df=df)
    return data, code, msg


def get_yield_curve(
        start_time='0',
        end_time='0',
        fields=None,
        limit=None,
        df=True
):
    '''
     国债收益率曲线
     :param start_time: 查询开始时间，格式如2024-01-01
     :param end_time: 查询结束时间，格式如2024-01-01
     :param fields: 查询字段，本接口暂不支持单独field查询，返回全部字段
     :param limit: 查询条数，本接口暂不支持分页查询, 返回全部查询内容
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
   :return:
   '''
    data, code, msg = APIManager().api.query(api_name='yieldCurve', fields=fields, start_time=start_time,
                                             end_time=end_time,
                                             limit=limit, df=df)
    return data, code, msg


def get_instruments(
        market_code=[],
        variety='stock',
        date='0',
        limit=None,
        # offset=0,
        df=True
):
    '''
    合约详细信息
     :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
     :param variety: 证券类型，默认None, 表示全部，variety='stock',表示返回股票类型
     :param date: 查询时间点，格式如2024-01-01, 默认0, 不限制查询时间点
     :param limit: 查询条数，默认None, 返回全部查询内容，limit=100,表示返回100条数据
     :param offset: 查询开始条数，默认0, 从第一条开始返回，offset=100,表示从101条开始返回
     :param df:返回结果方式 df=True,表示返回dataframe,df=False,表示返回是json字符串，默认True
    :return:
    '''

    data, code, msg = APIManager().api.query('get_instruments',
                                             symbols=market_code,
                                             variety=get_variety_value(variety),
                                             limit=limit,
                                             end_time=date,
                                             # offset=offset,
                                             fields=None,
                                             df=df)
    return data, code, msg;