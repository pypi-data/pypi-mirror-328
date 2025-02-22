import os
os.environ["deepquantsdk_env"] = "inner"
from deepquant import gid
from deepquant.factor import oq_data

username = "<用户名>" 
app_key = "<SDK的APPKEY>"

od = oq_data.OqData(username, app_key)

# 获取银河投资决策平台提供的公共因子值
# 获取列表可以通过平台公共因子库(deepquant.chinastock.com.cn/factorHouse)查询
data = od.get_factor_rows(
    factor_name='public.MACD',
    start_time='2024-10-01 00:00:00',
    end_time='2024-11-01 00:00:00',
    freq='1d',
    symbol_pool=['000300.SH']
)
