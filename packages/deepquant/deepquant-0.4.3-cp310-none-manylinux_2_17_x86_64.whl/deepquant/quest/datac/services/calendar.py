from deepquant import gid
import bisect
import datetime
from ..utils import int8_to_date, int_to_datetime
from ..validators import ensure_date_int, ensure_date_str
from ..decorators import export_as_api, ttl_cache, compatible_with_parm
from ..yhdatah_helper import yhdatah_serialize, http_conv_list_to_csv


def _map_expect_type(ty, fmt, dates):
    if ty == "int":
        return dates
    if ty == "datetime":
        return [int_to_datetime(dt) for dt in dates]
    if ty == "date":
        return [int8_to_date(dt) for dt in dates]
    if ty == "str":
        return [int_to_datetime(dt).strftime(fmt) for dt in dates]
    raise TypeError(ty)


def get_trading_dates_in_type(start_date, end_date, expect_type="datetime", fmt=None, market="cn"):
    """获取两个日期之间的交易日列表

    :param start_date: 开始日期
    :param end_date: 结束日期
    :param expect_type:  (Default value = "datetime")
    :param fmt:  (Default value = None)
    :param market:  (Default value = "cn")

    """
    # 处理起始时间
    start_time = ensure_date_str(start_date)
    end_time = ensure_date_str(end_date)
    # 获取交易日历数据
    data, code, msg = gid.trade_calendar(market=['SZ'], start_time=start_time, end_time=end_time)
    if data is not None:
        dates = data['trade_days'].tolist()
        return _map_expect_type(expect_type, fmt, [int(i) for i in dates])
    else:
        print("trade_calendar无数据")
        return None


@export_as_api
@compatible_with_parm(name="country", value="cn", replace="market")
@yhdatah_serialize(converter=http_conv_list_to_csv, name='trading_date')
def get_trading_dates(start_date, end_date, market="cn"):
    """获取交易日历数据

    :param start_date: 如 '2013-01-04'
    :param end_date: 如 '2013-01-04'
    :param market: 地区代码, 如 'cn' (Default value = "cn")
    :returns: 日期列表

    """
    # 处理起始时间
    # date_str = str(start_date).zfill(8)  # 确保字符串长度为8位，不足的前面补0
    # start_time = f"{date_str[0:4]}-{date_str[4:6]}-{date_str[6:8]}"
    start_time = ensure_date_str(start_date)
    date_format = '%Y-%m-%d'
    current_date = datetime.date.today()
    end_time = datetime.date(current_date.year, 12, 31).strftime(date_format)
    # 获取交易日历数据
    data, code, msg = gid.trade_calendar(market=['SZ'], start_time=start_time, end_time=end_time)
    if data is not None:
        dates = data['trade_days'].tolist()
        return [int8_to_date(int(i)) for i in dates]
    else:
        print("trade_calendar无数据")

@export_as_api
@compatible_with_parm(name="country", value="cn", replace="market")
@yhdatah_serialize(converter=http_conv_list_to_csv, name='trading_date')
def get_previous_trading_date(date, n=1, market="cn"):
    """获取前一交易日

    :param date: 日期
    :parm n: 日期间隔
    :param market:  (Default value = "cn")

    """
    if n < 1:
        raise ValueError("n: except a positive value, got {}".format(n))
    date = ensure_date_str(date)
    # 获取交易日历数据
    data, _, _ = gid.trade_calendar(market=['SZ'], start_time=date, end_time=date)
    if data is not None:
        dates = data['last_trade_days'].tolist()
        return int8_to_date(int(dates[0]))
    return None
