from deepquant import gid
from ..decorators import export_as_api, compatible_with_parm, retry
import warnings
import datetime
import pandas as pd
import numpy as np
from ..utils import (
    to_date_int,
    to_datetime,
    to_date,
    to_time,
    int8_to_datetime,
    int17_to_datetime_v,
    int17_to_datetime,
    date_to_int8,
    string_types
)
from ..errors import GatewayError

@export_as_api
@compatible_with_parm(name="country", value="cn", replace="market")
def get_price(
        market_code,
        start_date=None,
        end_date=None,
        frequency="1d",
        fields=None,
        adjust_type="pre",
        skip_suspended=False,
        expect_df=True,
        time_slice=None,
        market="cn",
        **kwargs
):
    """获取证券的历史数据

    :param market_code: 股票列表
    :param market: 地区代码, 如 'cn' (Default value = "cn")
    :param start_date: 开始日期, 如 '2013-01-04' (Default value = None)
    :param end_date: 结束日期, 如 '2014-01-04' (Default value = None)
    :param frequency: 可选参数, 默认为日线。日线使用 '1d', 分钟线 '1m' (Default value = "1d")
    :param fields: 可选参数。默认为所有字段。 (Default value = None)
    :param adjust_type: 可选参数,默认为‘pre', 返回开盘价，收盘价，最高价，最低价依据get_ex_factor 复权因子（包含分红，拆分），volume依据get_split 复权因子（仅涵盖拆分）计算的前复权数据
            'none'将返回原始数据
            'post'返回开盘价，收盘价，最高价，最低价依据get_ex_factor 复权因子（包含分红，拆分），volume依据get_split 复权因子（仅涵盖拆分）计算的后复权数据
            'pre_volume'返回开盘价，收盘价，最高价，最低价,成交量依据get_ex_factor 复权因子（包含分红，拆分）计算的前复权数据
            'post_volume'返回开盘价，收盘价，最高价，最低价,成交量依据get_ex_factor 复权因子（包含分红，拆分）计算的后复权数据
            'internal'返回只包含拆分的前复权数据。 (Default value = "pre")
    :param skip_suspended: 可选参数，默认为False；当设置为True时，返回的数据会过滤掉停牌期间，
                    此时market_code只能设置为一只股票 (Default value = False)
    :param expect_df: 返回 MultiIndex DataFrame (Default value = True)
    :param time_slice: 可选参数。获取分钟线或tick数据时，仅返回指定时间段的数据。
        类型为(str, str) 或 (datetime.time, datetime.time) 或 (int, int)
        如：("09:50", "10:11") 或 (datetime.time(9, 50), datetime.time(10, 11)) 或 (930, 1011)
    :returns: 如果仅传入一只股票, 返回一个 pandas.DataFrame
        如果传入多只股票, 则返回一个 pandas.Panel

    """
    sliceable = frequency.endswith(("m", "tick"))
    # check time_slice
    if time_slice:
        if not sliceable:
            warnings.warn("param [time_slice] only take effect when getting minbar or tick.")
        if not isinstance(time_slice, (tuple, list)) or len(time_slice) != 2:
            raise ValueError("time_slice: invalid, expect tuple or list value like ('09:55', '10:11'), got {}".format(time_slice))
        start, end = to_time(time_slice[0]), to_time(time_slice[1])

    df = _get_price(
        market_code, str(start_date), str(end_date), frequency,
        fields, adjust_type, skip_suspended, expect_df, market, **kwargs
    )

    if df is None or not sliceable or not time_slice:
        # 非tick、minbar或者不指定切片时间，直接返回
        return df

    # parse slice time_slice
    index = df.index.get_level_values('datetime')
    if start > end:
        # 期货夜盘，可以指定end<start,表示从夜盘到第二天日盘
        mask = (start <= index.time) | (index.time <= end)
    else:
        mask = (start <= index.time) & (index.time <= end)

    return df[mask]


@retry(3, suppress_exceptions=(GatewayError, ), delay=3.0)
def _get_price(
        market_code,
        start_date=None,
        end_date=None,
        frequency="1d",
        fields=None,
        adjust_type="pre",
        skip_suspended=False,
        expect_df=True,
        market="cn",
        **kwargs
):
    bak_frequency = frequency
    # tick数据
    if frequency == "tick":
        return get_tick_price(market_code, start_date, end_date, fields, expect_df, market)
    elif frequency.endswith(("d", "m", "w")):
        duration = int(frequency[:-1])
        frequency = frequency[-1]
        assert 1 <= duration <= 240, "frequency should in range [1, 240]"
        if market == "hk" and frequency == "m" and duration not in (1, 5, 15, 30, 60):
            raise ValueError("frequency should be str like 1m, 5m, 15m 30m,or 60m")
        elif frequency == 'w' and duration not in (1,):
            raise ValueError("Weekly frequency should be str '1w'")
    else:
        raise ValueError("frequency should be str like 1d, 1m, 5m or tick")
    # 验证adjust_type
    if "adjusted" in kwargs:
        adjusted = kwargs.pop("adjusted")
        adjust_type = "pre" if adjusted else "none"

    if kwargs:
        raise ValueError('unknown kwargs: {}'.format(kwargs))

    return get_kline_price(market_code, bak_frequency, start_date, end_date, fields, expect_df, market);


EQUITIES_TICK_FIELDS = [
    "trading_date", "open", "last", "high", "low",
    "prev_close", "volume", "total_turnover", "high_limited", "low_limited",
    "a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "a1_v", "a2_v", "a3_v",
    "a4_v", "a5_v", "b1_v", "b2_v", "b3_v", "b4_v", "b5_v", "change_rate",
    "num_trades",
]
FUND_TICK_FIELDS = EQUITIES_TICK_FIELDS + ["iopv", "prev_iopv"]
FUTURE_TICK_FIELDS = EQUITIES_TICK_FIELDS + ["open_interest", "prev_settlement"]
EQUITIES_TICK_COLUMNS = EQUITIES_TICK_FIELDS
FUTURE_TICK_COLUMNS = [
    "trading_date", "open", "last", "high", "low", "prev_settlement",
    "prev_close", "volume", "open_interest", "total_turnover", "high_limited", "low_limited",
    "a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "a1_v", "a2_v", "a3_v",
    "a4_v", "a5_v", "b1_v", "b2_v", "b3_v", "b4_v", "b5_v", "change_rate",
]
FUND_TICK_COLUMNS = FUND_TICK_FIELDS
RELATED_DABAR_FIELDS = {"open", "prev_settlement", "prev_close", "high_limited", "low_limited", "change_rate"}


def get_tick_price(market_code, start_date, end_date, fields, expect_df, market):
    df = get_tick_price_multi_df(market_code, start_date, end_date, fields, market)
    if df is not None and not expect_df and isinstance(market_code, string_types):
        df.reset_index(level=0, drop=True, inplace=True)
    return df

def get_kline_price(market_code, frequency, start_date, end_date, fields, expect_df, market):
    symbols = []
    if isinstance(market_code, (tuple, list)):
        symbols = market_code
    else:
        symbols = [market_code]

    dft, _, _ = gid.get_kline(symbols, frequency, start_date, end_date, fields)

    df = dft.rename(columns={"security_code": "market_code"})
    df.reset_index(level=0, drop=True, inplace=True)
    if df is not None and not expect_df and isinstance(market_code, string_types):
        if fields is not None and len(fields)==1:
            return df[fields[0]]
    elif df is not None and isinstance(market_code, list):
        if fields is None or len(fields)>1:
            df.set_index(['market_code',"orig_time"], inplace=True)


    return df



def get_tick_price_multi_df(market_code, start_date, end_date, fields, market):
    '''
    start_date, end_date = ensure_date_range(start_date, end_date, datetime.timedelta(days=3))

    live_date = current_trading_date()
    if start_date > live_date:
        return

    ins_list = ensure_instruments(market_code)
    market_code = [ins.market_code for ins in ins_list]
    #types = {ins.type for ins in ins_list}
    '''
    market_code = []
    if isinstance(market_code, (tuple, list)):
        market_code = market_code
    else:
        market_code = [market_code]

    data, _, _ = gid.get_snapshot(market_code, start_date, end_date, fields)

    df = data.rename(columns={"security_code": "market_code"})

    if df is not None  and isinstance(market_code, string_types):
        if fields is not None and len(fields) == 1:
            return df[fields[0]]
    elif df is not None and isinstance(market_code, list):
        if fields is None or len(fields) > 1:
            df.set_index(['market_code', "orig_time"], inplace=True)

def _convert_int_to_datetime(date_int, time_int):
    return date_int * 1000000000 + time_int





@export_as_api()
def get_stock_connect_holding_details(market_code, start_date=None, end_date=None):
    """
    获取北向资金席位持股明细数据
    :param market_code: 标的合约
    :param start_date: 起始日期
    :param end_date: 结束日期
    :return: pd.DataFrame
    """
    pass


@export_as_api
def get_vwap(market_code, start_date=None, end_date=None, frequency="1d"):
    """ 获取vwap(成交量加权平均价格)数据

    :param market_code: 标的合约, 支持股票、期货、期权、ETF、可转债
    :param market: 地区代码, 如 'cn' (Default value = "cn")
    :param start_date: 开始日期, 如 '2013-01-04' (Default value = None)
    :param end_date: 结束日期, 如 '2014-01-04' (Default value = None)
    :param frequency: 可选参数, 默认为日线。日线使用 '1d', 分钟线 '1m' (Default value = "1d")
    :returns: multi-index series, 其中index为 market_code, date 组成的数据, 值为 vwap
    """
    pass
