# encoding: utf-8
from deepquant.quest.alpha.apis import *


__config__ = {
    "base": {
        "data_bundle_path": "D:/sendData/ricequant/bundle",
        "start_date": '2024-07-01 09:30:00',  # 回测起始日期
        "end_date": '2024-07-04 15:00:00',  # 回测结束日期
        'frequency': 'tick',
        "accounts": {
            "stock": 10000000
        },
    },
     "mod": {

         "sys_analyser": {
             # 策略基准，该基准将用于风险指标计算和收益曲线图绘制
             #   若基准为单指数/股票，此处直接设置 order_book_id，如："000300.XSHG"
             #   若基准为复合指数，则需传入 order_book_id 和权重构成的字符串，如："000300.XSHG:0.2,000905.XSHG:0.8"
             "benchmark": None,
             # 当不输出 csv/pickle/plot 等内容时，关闭该项可关闭策略运行过程中部分收集数据的逻辑，用以提升性能
             "record": False,
             # 策略名称，可设置 summary 报告中的 strategy_name 字段，并展示在 plot 回测结果图中
             "strategy_name": 'mack.pickle',
             # 回测结果输出的文件路径，该文件为 pickle 格式，内容为每日净值、头寸、流水及风险指标等；若不设置则不输出该文件
             "output_file": '/output',
             # 回测报告的数据目录，报告为 csv 格式；若不设置则不输出报告
             "report_save_path": './backtest',
             # 是否在回测结束后绘制收益曲线图
             'plot': False,
             # 收益曲线图路径，若设置则将收益曲线图保存为 png 文件
             'plot_save_file': None,
             # 收益曲线图设置
             'plot_config': {
                 # 是否在收益图中展示买卖点
                 'open_close_points': False,
                 # 是否在收益图中展示周度指标和收益曲线
                 'weekly_indicators': False
             },
         },
        "option" : {
            "enabled" : False
        },
        "convertible" : {
            "enabled" : False
        },
        "spot" : {
            "enabled" : False
        },
        "fund" : {
            "enabled" : False
        },
  }
}


def init(context):
    # 定义标
    # CS ETF Convertible Future option
    context.market_code = ['000002.SZ']
    subscribe(context.market_code)  # 订阅行情


# 盘前处理
def before_trading(context):
    pass

def handle_tick(context, tick):
    print("handle_tick.....", str(tick))
    # print(tick.market_code)
   #order_target_value(tick.market_code, 100)


# 盘后处理
def after_trading(context):
    pass


if __name__ == '__main__':
    from deepquant.quest.alpha import run_func
    data = run_func(init=init, before_trading=before_trading, after_trading=after_trading, handle_tick=handle_tick, config=__config__)
