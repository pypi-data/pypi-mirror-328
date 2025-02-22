# -*- coding: utf-8 -*-
import six
import datetime
import warnings
import bisect

import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta

def get_dominant_future(underlying_symbol, start_date=None, end_date=None, rule=0, rank=1, market="cn"):
    import warnings

    msg = "'get_dominant_future' is deprecated, please use 'futures.get_dominant' instead"
    warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
    return get_dominant(underlying_symbol, start_date, end_date, rule, rank, market)


def get_dominant(underlying_symbol, start_date=None, end_date=None, rule=0, rank=1, market="cn"):
    """获取指定期货品种当日对应的主力合约

    :param underlying_symbol: 如'IF' 'IC'
    :param start_date: 如 '2015-01-07' (Default value = None)
    :param end_date: 如 '2015-01-08' (Default value = None)
    :param market:  (Default value = "cn")
    :param rule:  主力合约规则 (Default value = 0)
        0：在rule=1的规则上，增加约束(曾做过主力合约的合约，一旦被换下来后，不会再被选上)
        1：合约首次上市时，以当日收盘同品种持仓量最大者作为从第二个交易日开始的主力合约，当同品种其他合约持仓量在收盘后
           超过当前主力合约1.1倍时，从第二个交易日开始进行主力合约的切换。日内不会进行主力合约的切换
        2: 前一交易日持仓量与成交量均为最大的合约
    :param rank:  (Default value = 1):
        1: 主力合约
        2: 次主力合约
        3：次次主力合约
    :returns: pandas.Series
        返回参数指定的具体主力合约名称

    """
    if not isinstance(underlying_symbol, six.string_types):
        raise ValueError("invalid underlying_symbol: {}".format(underlying_symbol))




def current_real_contract(ob, market):
    """获取指定期货品种当日对应的真实合约"""
    pass


_FIELDS = [
    "margin_type",
    "long_margin_ratio",
    "short_margin_ratio",
    "commission_type",
    "open_commission_ratio",
    "close_commission_ratio",
    "close_commission_today_ratio",
]


def future_commission_margin(market_code=None, fields=None, hedge_flag="speculation"):
    import warnings

    msg = "'future_commission_margin' is deprecated, please use 'futures.get_commission_margin' instead"
    warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
    return get_commission_margin(market_code, fields, hedge_flag)


def get_commission_margin(market_code=None, fields=None, hedge_flag="speculation"):
    """获取期货保证金和手续费数据

    :param market_code: 期货合约, 支持 market_code 或 market_code list,
        若不指定则默认获取所有合约 (Default value = None)
    :param fields: str 或 list, 可选字段有： 'margin_type', 'long_margin_ratio', 'short_margin_ratio',
            'commission_type', 'open_commission_ratio', 'close_commission_ratio',
            'close_commission_today_ratio', 若不指定则默认获取所有字段 (Default value = None)
    :param hedge_flag: str, 账户对冲类型, 可选字段为: 'speculation', 'hedge',
            'arbitrage', 默认为'speculation', 目前仅支持'speculation' (Default value = "speculation")
    :returns: pandas.DataFrame

    """



def get_future_member_rank(market_code, trading_date=None, info_type='volume'):
    import warnings

    msg = "'get_future_member_rank' is deprecated, please use 'futures.get_member_rank' instead"
    warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
    return get_member_rank(market_code, trading_date, info_type)



def get_member_rank(obj, trading_date=None, rank_by='volume', **kwargs):
    """获取指定日期最近的期货会员排名数据
    :param obj： 期货合约或品种代码
    :param trading_date: 日期
    :param rank_by: 排名依据字段
    :keyword start_date
    :keyword end_date
    :returns pandas.DataFrame or None
    """
    pass


def get_warehouse_stocks(underlying_symbols, start_date=None, end_date=None, market="cn"):
    """获取时间区间内期货的注册仓单

    :param underlying_symbols: 期货品种, 支持列表查询
    :param start_date: 如'2015-01-01', 如果不填写则为去年的当日日期
    :param end_date: 如'2015-01-01', 如果不填写则为当日日期
    :param market: 市场, 默认为"cn"
    :return: pd.DataFrame

    """
    pass

def get_contract_multiplier(underlying_symbols, start_date=None, end_date=None, market="cn"):
    """获取时间区间内期货的合约乘数

    :param underlying_symbols: 期货品种, 支持列表查询
    :param start_date: 开始日期, 如'2015-01-01', 如果不填写则取underlying_symbols对应实际数据最早范围
    :param end_date: 结束日期, 如'2015-01-01', 如果不填写则为当日前一天
    :param market: 市场, 默认为"cn", 当前仅支持中国市场
    :return: pd.DataFrame

    """
    pass

def get_current_basis(market_code, market='cn'):
    """获取股指期货的实时基差指标

    :param market_code: str or str list	合约代码
    :param market: str	默认是中国内地市场('cn') 。可选'cn' - 中国内地市场；
    :return: DataFrame with below fields:
        字段	类型	说明
        market_code	str	合约代码
        datetime	datetime	时间戳
        index	str	指数合约
        index_px	float	指数最新价格
        future_px	float	期货最新价格
        basis	 float	升贴水， 等于期货合约收盘价- 对应指数收盘价
        basis_rate	float	升贴水率(%)，（期货合约收盘价- 对应指数收盘价）/对应指数收盘价*100
        basis_annual_rate	float	年化升贴水率（%), basis_rate *(250/合约到期剩余交易日）
    """
    pass


VALID_FIELDS_MAP = {
    '1d': [
        "open", "high", "low", "close", "index", "close_index",
        "basis", "basis_rate", "basis_annual_rate",
        "settlement", "settle_basis", "settle_basis_rate", "settle_basis_annual_rate"
    ],
    '1m': [
        "open", "high", "low", "close", "index", "close_index",
        "basis", "basis_rate", "basis_annual_rate"
    ],
    'tick': [
        "index", "future_px", "index_px",
        "basis", "basis_rate", "basis_annual_rate",
    ]
}

FUTURE_PRICE_FIELDS_MAP = {
    '1d': ['close', 'open', 'high', 'low', 'settlement'],
    '1m': ['close', 'open', 'high', 'low'],
    'tick': ['last']
}


def get_basis(market_code, start_date=None, end_date=None, fields=None, frequency='1d', market="cn"):
    """ 获取股指期货升贴水信息.

    :param market_code: 期货合约, 支持 market_code 或 market_code list.
    :param start_date: 开始时间, 若不传, 为 end_date 前3个月.
    :param end_date: 结束时间, 若不传, 为 start_date 后3个月, 如果 start_date 也不传, 则默认为最近3个月.
    :param fields: 需要返回的字段, 若不传则返回所有字段, 支持返回的字段包括
        open, high, low, close, index, close_index, basis, basis_rate, basis_annual_rate.
    :param frequency: 数据频率, 默认 '1d', 其他可选 {'1m', 'tick'}
        frequency=tick时, fields为index, future_px, index_px, basis, basis_rate, basis_annual_rate
    :param market: 市场, 默认'cn'
    :return: MultiIndex DataFrame.
    """
    pass


VALID_ADJUST_METHODS = ['prev_close_spread', 'open_spread', 'prev_close_ratio', 'open_ratio']


def _get_future_factors_df(rule=0, market='cn'):
    """ 获取所有复权因子表 """
    pass



def get_ex_factor(underlying_symbols, start_date=None, end_date=None, adjust_method='prev_close_spread', rule=0,
                  market='cn'):
    """ 获取期货复权因子

    :param underlying_symbols: 期货合约品种，str or list
    :param start_date: 开始日期
    :param end_date: 结束日期
    :param adjust_method: 复权方法，prev_close_spread, prev_close_ratio, open_spread, open_ratio,
    默认为‘prev_close_spread'
    :param rule: 主力合约规则
    :param market: 默认是中国内地市场('cn') 。可选'cn' - 中国内地市场
    :return: DataFrame
    """
    pass


def __internal_get_ex_factor(underlying_symbols, adjust_type, adjust_method, rule=0):
    """ 内部使用，获取复权因子，提供给get_dominant_price进行复权计算用
    :return: pd.Series
    """
    df = _get_future_factors_df(rule)
    df = df.loc[underlying_symbols]

    factor = df[adjust_method]
    factor.name = 'ex_factor'
    factor = factor.reset_index()
    pre = adjust_type == 'pre'
    ratio = adjust_method.endswith('ratio')

    def _process(x):
        if ratio:
            x['ex_cum_factor'] = x['ex_factor'].cumprod()
            if pre:
                x['ex_cum_factor'] = x['ex_cum_factor'] / x['ex_cum_factor'].iloc[-1]
        else:
            x['ex_cum_factor'] = x['ex_factor'].cumsum()
            if pre:
                x['ex_cum_factor'] = x['ex_cum_factor'] - x['ex_cum_factor'].iloc[-1]

        # tds 是从小到大排列的， 因此reindex后无需再sort
        return x.set_index('ex_date')

    factor = factor.groupby('underlying_symbol', as_index=True).apply(_process)
    return factor['ex_cum_factor']


DOMINANT_PRICE_ADJUST_FIELDS = [
    'open', 'high', 'low', 'close', 'last', 'high_limited', 'low_limited', 'settlement', 'prev_settlement', 'prev_close',
    'a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5'
]

DOMINANT_PRICE_FIELDS = {
    'tick': [
        "trading_date", "open", "last", "high", "low",
        "prev_close", "volume", "total_turnover", "high_limited", "low_limited",
        "a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "a1_v", "a2_v", "a3_v",
        "a4_v", "a5_v", "b1_v", "b2_v", "b3_v", "b4_v", "b5_v", "change_rate",
        "open_interest", "prev_settlement",
    ],
    'd': [
        "open", "close", "high", "low", "total_turnover", "volume", "prev_close",
        "settlement", "prev_settlement", "open_interest", "high_limited", "low_limited",
        "day_session_open",
    ],
    'm': [
        "trading_date", "open", "close", "high", "low", "total_turnover", "volume", "open_interest"
    ],
}


def _slice_dominant_data(data):
    s = None
    uids = set()
    for i, (obid, _) in enumerate(data):
        if obid in uids:
            uids.clear()
            yield slice(s, i)
            s = i
        uids.add(obid)
    yield slice(s, None)


def get_dominant_price(
        underlying_symbols, start_date=None, end_date=None,
        frequency='1d', fields=None, adjust_type='pre', adjust_method='prev_close_spread',
        rule=0,
):
    """ 获取主力合约行情数据

    :param underlying_symbols: 期货合约品种，可传入 underlying_symbol, underlying_symbol list
    :param start_date: 开始日期, 最小日期为 20210104
    :param end_date: 结束日期
    :param frequency: 历史数据的频率。 支持/日/分钟/tick 级别的历史数据，默认为'1d'。
        1m- 分钟线，1d-日线，分钟可选取不同频率，例如'5m'代表 5 分钟线
    :param fields: 字段名称列表
    :param adjust_type: 复权方式，不复权 - none，前复权 - pre，后复权 - post
    :param adjust_method: 复权方法 ，prev_close_spread/open_spread:基于价差复权因子进行复权，
        prev_close_ratio/open_ratio:基于比例复权因子进行复权，
        默认为‘prev_close_spread',adjust_type为None 时，adjust_method 复权方法设置无效
    :param rule: 主力合约规则，参考get_dominant
    :return: MultiIndex DataFrame
    """
    pass


def get_ob_datetime_multi_index(
        market_code,
        start_date,
        end_date,
        names=['market_code', 'trading_date']
):
    pass


TRADING_PARAMETERS_FIELDS = [
    'long_margin_ratio',
    'short_margin_ratio',
    'commission_type',
    'open_commission',
    'close_commission',
    'discount_rate',
    'close_commission_today',
    'non_member_limit_rate',
    'client_limit_rate',
    'non_member_limit',
    'client_limit',
    'min_order_quantity',
    'max_order_quantity',
    'min_margin_ratio',
]


def get_trading_parameters(market_code, start_date=None, end_date=None, fields=None, market='cn'):
    """ 获取期货交易参数信息

    :param market_code: 期货合约代码或代码列表
    :param start_date: 开始日期，如 '2019-01-01'，若不指定，默认为当前交易日
                       未指定时，若查询时间在 T 日 8.40pm 前，返回 T 日数据，否则返回 T+1 日数据
    :param end_date: 结束日期，如 '2023-01-01'，若不指定，默认为当前交易日
                     开始日期和结束日期需同时传入或同时不传入
    :param fields: 所需字段或字段列表，不指定则返回全部字段，可选:
        [ 'long_margin_ratio', 'short_margin_ratio', 'commission_type', 'open_commission',
          'close_commission', 'discount_rate, 'close_commission_today',
          'non_member_limit_rate', 'client_limit_rate', 'non_member_limit', 'client_limit',
          'min_order_quantity', 'max_order_quantity', 'min_margin_ratio',
        ]
        min_margin_ratio: 最低保证金
    :param market: 目前只支持中国市场，默认为 'cn'

    :return: DataFrame(MultiIndex(market_code, trading_date)) or None

    """
    pass



def get_exchange_daily(market_code, start_date=None, end_date=None, fields=None, market='cn'):
    """获取交易所日线数据

    :param market_code: 期货合约代码或代码列表
    :param start_date: 开始日期
    :param end_date: 结束日期
    :param fields: 所需字段或字段列表，不指定则返回全部字段，可选:
        [
            "open", "close", "high", "low", "total_turnover",
            "volume", "settlement", "prev_settlement", "open_interest"
        ]
    :param market: 目前只支持中国市场，默认为 'cn'
    :return: DataFrame(MultiIndex(market_code, trading_date)) or None
    """
    pass
