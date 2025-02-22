from deepquant import gid

gid.init('gidtest','gid#2024');

data, code, msg = gid.get_kline(
    ['000001.SZ'],  # 可填写多个标的代码
    frequency='1d',
    start_time='2023-10-01',
    end_time='2024-01-01'
)

print(data.head())

from deepquant.factor.op import *

print("ATR", ATR(data.high_price, data.low_price, data.close_price, 6))
print("SMA", SMA(data.close_price))


