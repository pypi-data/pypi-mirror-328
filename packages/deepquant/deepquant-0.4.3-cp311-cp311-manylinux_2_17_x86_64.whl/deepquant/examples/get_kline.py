from deepquant import gid

username = "<用户名>"
app_key = "<SDK的APPKEY>"

gid.init(username, app_key)

#获取行情数据/get_kline-单只标的日K线行情
data, code, msg = gid.get_kline(
    ['000001.SZ'],  # 可填写多个标的代码
    frequency='1d',
    start_time='2023-01-01',
    end_time='2024-01-01'
)
