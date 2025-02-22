import warnings
import datetime
import pandas as pd

from deepquant import gid
from deepquant.data.gqclient.commons import ApiRspCode
from deepquant.quest.utils.datetime_func import convert_dt_to_date_str
from ..decorators import export_as_api, may_trim_bjse
from ..yhdatah_helper import yhdatah_serialize, http_conv_list_to_csv
from ..validators import (
    ensure_date_range,
    ensure_date_or_today_int,
    ensure_list_of_string,
    check_items_in_container,
    ensure_order,
    raise_for_no_panel,
    ensure_date_str,
    ensure_market_code,
    ensure_date_int,
)
from ..services.calendar import (
    get_trading_dates,
    get_previous_trading_date,
    get_trading_dates_in_type,
)
from ..utils import is_panel_removed


@export_as_api
@may_trim_bjse
@yhdatah_serialize(converter=http_conv_list_to_csv, name='market_code')
def get_margin_stocks(date=None, exchange=None, margin_type='stock', market="cn"):
    """获取融资融券信息

    :param date: 查询日期，默认返回今天上一交易日，支持 str, timestamp, datetime 类型
    :param exchange: 交易所信息，默认不填写则返回全部。
                    str类型，默认为 None，返回所有字段。可选字段包括：
                    'XSHE', 'sz' 代表深交所；'XSHG', 'sh' 代表上交所，不区分大小写
                    (Default value = None)
    :param margin_type: 'stock' 代表融券卖出，'cash'，代表融资买入，默认为'stock'

    """
    pass

@export_as_api
@may_trim_bjse
@yhdatah_serialize(converter=http_conv_list_to_csv, name='market_code')
def get_suspend_days(market_code, start_date, end_date):
    """获取证券停牌信息

    :param market_code:标的名称,格式如[‘600000.SH，600004.SH’]
    :param start_date: 查询开始时间，格式如2024-01-01，start_time='0',表示返回最新的
    :param end_date: 查询结束时间，格式如2024-01-01，end_time='0',表示返回最新的
    :return key为market_code, value为trade_date列表的dict

    """
    data, code, msg = gid.get_suspended_days(market_code, start_date, end_date)

    #print(data)

    if ApiRspCode.is_succ(code) and not data.empty :
        grouped = data.groupby('market_code')['trade_date'].apply(list)
        dict = grouped.to_dict()

        return dict
    else:
        return None

@export_as_api
@may_trim_bjse
def get_industry(industry, source=12, date=None):
    """获取行业股票列表

    :param industry: 行业名称或代码
    :param source: 分类来源。
                10:万得行业分类； 12:证监会行业分类； 13:申万行业分类； 14:中信行业分类；港股: hsi: 恒生
    :param date: 查询日期，默认为当前最新日期
    :param market:  (Default value = "cn")
    :return: 所属目标行业的market_code list or None
    """

    if date is None:
        date = datetime.date.today()
        date = convert_dt_to_date_str(date)
    if isinstance(date, datetime.datetime):
        date = convert_dt_to_date_str(date)

    data, code, msg = gid.get_industry(industry, source, date)

    if ApiRspCode.is_succ(code) and not data.empty :
        #df = data.rename(columns={"security_code": "market_code"})
        if len(data.columns)==1:
            data.columns=["market_code"]
        return data["market_code"]

    else:
        return None

@export_as_api
@may_trim_bjse
@yhdatah_serialize(converter=http_conv_list_to_csv, name='market_code')
def concept(*concepts, **kwargs):
    """获取对应某个概念的股票列表。

    可指定日期，默认按当前日期返回。目前支持的概念列表可以查询以下网址:
    https://www.ricequant.com/api/research/chn#concept-API-industry

    :param concepts: 概念字符串,如 '民营医院'
    :param date: 可指定日期，默认按当前日期返回.
    :param market: 地区代码, 如 'cn'
    :returns: 符合对应概念的股票列表

    """
    #msg = "'concept' is deprecated, please use 'get_concept' instead"
    #warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
    date = kwargs.pop("date", None)
    if date is None:
        date = datetime.date.today()
    if isinstance(date, datetime.date):
        date = convert_dt_to_date_str(date)

    data, code, msg = gid.get_concept(concepts, date)

    if ApiRspCode.is_succ(code) and not data.empty:
        if len(data.columns) == 1:
            data.columns = ["market_code"]
        return data["market_code"]

    else:
        return None


MARGIN_FIELDS = (
    "borrow_money_balance",
    "purch_with_borrow_money",
    "repayment_of_borrow_money",
    "sec_lending_balance",
    "sales_of_borrowed_sec",
    "repayment_of_borrow_sec",
    "sec_lending_balance_vol",
    "margin_trade_balance",
)

MARGIN_SUMMARY_MAP = {"SH": "XSHG", "XSHG": "XSHG", "SZ": "XSHE", "XSHE": "XSHE"}


@export_as_api
@may_trim_bjse
@yhdatah_serialize(converter=http_conv_list_to_csv, name='market_code')
def get_securities_margin(
        market_code, start_date=None, end_date=None, fields=None, expect_df=True, market="cn"
):
    """获取股票融资融券数据

    :param market_codes: 股票代码或代码列表
    :param start_date: 开始时间，支持 str, date, datetime, pandasTimestamp
        默认为 end_date 之前一个月 (Default value = None)
    :param end_date: 结束时间 默认为当前日期前一天 (Default value = None)
    :param fields: str 或 list 类型. 默认为 None, 返回所有字段。可选字段包括：
                   margin_balance, buy_on_margin_value, margin_repayment, short_balance, short_balance_quantity,
                   short_sell_quantity, short_repayment_quantity, total_balance
                   (Default value = None)
    :param expect_df: 返回 MultiIndex DataFrame (Default value = True)
    :param market: 地区代码, 如: 'cn' (Default value = "cn")
    :returns: 如果传入多个股票代码，且 fields 为多个或者 None，返回 pandas.Panel
        如果传入一只股票或者 fields 为单个字段，则返回 pandas.DataFrame
        如果传入的股票代码和字段数都是1，则返回 pandas.Series

    """

    if isinstance(market_code, (tuple, list)):
        market_codes = market_code
    else:
        market_codes = [market_code]

    # TODO 支持全市场数据
    # all_list = []
    # for order_book_id in order_book_ids:
    #     if order_book_id.upper() in MARGIN_SUMMARY_MAP:
    #         all_list.append(MARGIN_SUMMARY_MAP[order_book_id.upper()])
    #     else:
    #         inst = instruments(order_book_id, market)
    #
    #         if inst is not None and inst.type in ["CS", "ETF", "LOF"]:
    #             all_list.append(inst.order_book_id)
    #         else:
    #             warnings.warn("{} is not stock, ETF, or LOF.".format(order_book_id))
    # order_book_ids = all_list
    # if not order_book_ids:
    #     raise ValueError("no valid securities in {}".format(order_book_ids))
    if fields is None:
        fields = list(MARGIN_FIELDS)
    else:
        fields = ensure_list_of_string(fields, "fields")
        check_items_in_container(fields, MARGIN_FIELDS, "fields")
        fields = ensure_order(fields, MARGIN_FIELDS)
    start_date, end_date = ensure_date_range(start_date, end_date)
    if end_date > ensure_date_or_today_int(None):
        end_date = ensure_date_or_today_int(get_previous_trading_date(datetime.date.today()))
    trading_dates = pd.to_datetime(get_trading_dates(start_date, end_date, market=market))

    s, e = ensure_date_str(start_date), ensure_date_str(end_date)
    df, _, _ = gid.margin_detail(market_code=market_codes, start_time=s, end_time=e)
    #df, _, _ = gid.margin_detail(market_code=['000001.SZ', '000002.SZ'], start_time='2002-07-23',
                                   # end_time='2024-08-02', limit=10)
    if df.empty or df is None:
        return

    if not expect_df and not is_panel_removed:

        pl = pd.Panel(items=fields, major_axis=trading_dates, minor_axis=market_codes)
        for r in df:
            for field in fields:
                value = r.get(field)
                pl.at[field, r["trade_date"], r["market_code"]] = value

        if len(market_codes) == 1:
            pl = pl.minor_xs(market_codes[0])
        if len(fields) == 1:
            pl = pl[fields[0]]
        if len(market_codes) != 1 and len(fields) != 1:
            warnings.warn("Panel is removed after pandas version 0.25.0."
                          " the default value of 'expect_df' will change to True in the future.")
        return pl
    else:
        df.sort_values(["market_code", "trade_date"], inplace=True)
        df.set_index(["market_code", "trade_date"], inplace=True)
        df = df.reindex(columns=fields)
        if expect_df:
            print(df)
            return df

        if len(market_codes) != 1 and len(fields) != 1:
            raise_for_no_panel()

        if len(market_codes) == 1:
            df.reset_index(level=0, drop=True, inplace=True)
            if len(fields) == 1:
                df = df[fields[0]]
            return df
        else:
            df = df.unstack(0)[fields[0]]
            df.index.name = None
            df.columns.name = None
            return df


share_fields = {
    "tot_share": "tot_share",
    "float_a_share": "a_cir_shares",
    "non_circulation_a": "a_non_cir_shares",
    "tot_a_share": "tot_a_share",
    'preferred_shares': 'preferred_shares',
    "free_circulation": "free_circulation"
}

reversed_fields = {v: k for k, v in share_fields.items()}

SHARE_FIELDS = (
    "tot_share",
    "float_a_share",
    "non_tradable_share",
    "tot_a_share"
)


@export_as_api
def get_shares(market_code, start_date=None, end_date=None, fields=None, expect_df=True, market="cn"):
    """获取流通股本信息

    :param market_code: 股票名称
    :param start_date: 开始日期, 如'2013-01-04' (Default value = None)
    :param end_date: 结束日期，如'2014-01-04' (Default value = None)
    :param fields: 如'total', 'circulation_a' (Default value = None)
    :param expect_df: 返回 MultiIndex DataFrame (Default value = True)
    :param market: 地区代码，如'cn' (Default value = "cn")
    :returns: 返回一个DataFrame

    """
    #market_code = ensure_market_code(market_code, market=market)
    if isinstance(market_code, (tuple, list)):
        market_codes = market_code
    else:
        market_codes = [market_code]
    start_date, end_date = ensure_date_range(start_date, end_date)
    if fields:
        fields = ensure_list_of_string(fields, "fields")
        check_items_in_container(fields, SHARE_FIELDS, "fields")
        fields = ensure_order(fields, SHARE_FIELDS)
    else:
        fields = list(SHARE_FIELDS)

    df, _, _ = gid.get_share_daily(market_code=market_codes, start_time=convert_int_to_date_str(start_date),end_time=convert_int_to_date_str(end_date))
    if df.empty or df is None:
        return

    dates = get_trading_dates_in_type(start_date, end_date, expect_type="datetime", market=market)
    unique = set(df.market_code)
    missing = [obid for obid in market_codes if obid not in unique]
    if missing:
        missing_df = pd.DataFrame({"market_code": missing, "trade_date": df.trade_date.iloc[-1]})
        df = pd.concat([df, missing_df])

    df.set_index(["trade_date", "market_code"], inplace=True)
    df.sort_index(inplace=True)
    df = df.unstack(level=1)
    # 交易时间数据补齐，数据接口返回的全部自然日，暂时不需要做日期补齐的操作
    # index = df.index.union(dates)
    # df = df.reindex(index)
    # df = df.fillna(method="ffill")
    df = df.loc[list(dates)]
    df = df.dropna(how="all")
    df = df[fields]
    if not is_panel_removed and not expect_df:
        pl = df.stack(1).to_panel()
        if len(market_codes) == 1:
            pl = pl.minor_xs(market_codes[0])
        if len(fields) == 1:
            pl = pl[fields[0]]
        if len(market_codes) != 1 and len(fields) != 1:
            warnings.warn("Panel is removed after pandas version 0.25.0."
                          " the default value of 'expect_df' will change to True in the future.")
        return pl
    else:
        df = df.stack(1)
        df.index.set_names(["trade_date", "market_code"], inplace=True)
        # TODO 根据全市场数据获取de_listed_date（上市或者退市日期）进行时间判断
        # de_listed_map = {i: instruments(i).de_listed_date for i in market_codes}
        # max_end_date = df.index.levels[0].max() + pd.Timedelta(days=1)
        # de_listed_map = {k: (pd.to_datetime(v) if v != '0000-00-00' else max_end_date) for k, v in
        #                  de_listed_map.items()}
        # i0 = df.index.get_level_values(0)
        # i1 = df.index.get_level_values(1).map(de_listed_map)
        # mask = i1 > i0
        # df = df[mask]
        # if df.empty:
        #     return None
        df = df.reorder_levels(["market_code", "trade_date"]).sort_index()
        if expect_df:
            return df

        if len(market_codes) != 1 and len(fields) != 1:
            raise_for_no_panel()

        if len(market_codes) == 1:
            df.reset_index(level=0, drop=True, inplace=True)
            if len(fields) == 1:
                df = df[fields[0]]
            return df
        else:
            df = df.unstack(0)[fields[0]]
            df.index.name = None
            df.columns.name = None
            return df

@export_as_api
def get_stock_connect(order_book_ids, start_date=None, end_date=None, fields=None, expect_df=True):
    """获取"陆股通"的持股、持股比例

    :param order_book_ids: 股票列表
    :param start_date: 开始日期: 如'2017-03-17' (Default value = None)
    :param end_date: 结束日期: 如'2018-03-16' (Default value = None)
    :param fields: 默认为所有字段，可输入shares_holding, holding_ratio, adjusted_holding_ratio (Default value = None)
    :param expect_df: 是否返回 MultiIndex DataFrame (Default value = True)
    :returns: 返回pandas.DataFrame or pandas.Panel

    """
    if order_book_ids not in ("shanghai_connect", "shenzhen_connect", "all_connect"):
        order_book_ids = ensure_market_code(order_book_ids, type="CS")
    start_date, end_date = ensure_date_range(start_date, end_date)
    if fields is not None:
        fields = ensure_list_of_string(fields)
        for f in fields:
            if f not in ("shares_holding", "holding_ratio", "adjusted_holding_ratio"):
                raise ValueError("invalid field: {}".format(f))
    else:
        fields = ["shares_holding", "holding_ratio", "adjusted_holding_ratio"]
    # data = get_client().execute("get_stock_connect", order_book_ids, start_date, end_date, fields)
    if not data:
        return None
    df = pd.DataFrame(data, columns=["trading_date", "order_book_id"] + fields)

    if not expect_df and not is_panel_removed:
        df = df.set_index(["trading_date", "order_book_id"])
        df = df.to_panel()
        df.major_axis.name = None
        df.minor_axis.name = None
        if len(order_book_ids) == 1:
            df = df.minor_xs(order_book_ids[0])
        if len(fields) == 1:
            df = df[fields[0]]
        if len(order_book_ids) != 1 and len(fields) != 1:
            warnings.warn("Panel is removed after pandas version 0.25.0."
                          " the default value of 'expect_df' will change to True in the future.")
        return df
    else:
        df.sort_values(["order_book_id", "trading_date"], inplace=True)
        df.set_index(["order_book_id", "trading_date"], inplace=True)
        if expect_df:
            return df

        if len(order_book_ids) != 1 and len(fields) != 1:
            raise_for_no_panel()

        if len(order_book_ids) == 1:
            df.reset_index(level=0, drop=True, inplace=True)
            if len(fields) == 1:
                df = df[fields[0]]
            return df
        else:
            df = df.unstack(0)[fields[0]]
            df.index.name = None
            df.columns.name = None
            return df