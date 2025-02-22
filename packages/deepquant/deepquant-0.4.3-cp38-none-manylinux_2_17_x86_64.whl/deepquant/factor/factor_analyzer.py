import inspect
import os
import logging
import glob
import itertools

import pandas as pd
import numpy as np

from scipy.stats import spearmanr, pearsonr
from scipy import stats
from typing import Iterable


from deepquant.factor import perf
from deepquant.factor.utils import *
from deepquant.factor.analysor import *
from deepquant.factor.summary import *
from deepquant.factor import plotting


#from .oq_data import OqData
import warnings
warnings.filterwarnings('ignore',category=FutureWarning)

logger = logging.getLogger("factor_analyzer")
logger.setLevel(logging.INFO)




class DataError(Exception):
    def __init__(self, msg):
        super().__init__(msg)



class FactorAnalyzer(object):
    """单因子分析

        参数
        ----------
        factor :
            因子值
            pd.DataFrame / pd.Series
            一个 DataFrame, index 为日期, columns 为资产,
            values 为因子的值
            或一个 Series, index 为日期和资产的 MultiIndex,
            values 为因子的值
        prices :
            用于计算因子远期收益的价格数据
            pd.DataFrame
            index 为日期, columns 为资产
            价格数据必须覆盖因子分析时间段以及额外远期收益计算中的最大预期期数.
            或 function
            输入参数为 securities, start_date, end_date, count
            返回值为价格数据的 DataFrame
        groupby :
            分组数据, 默认为 None
            pd.DataFrame
            index 为日期, columns 为资产，为每个资产每天的分组.
            或 dict
            资产-分组映射的字典. 如果传递了dict，则假定分组映射在整个时间段内保持不变.
            或 function
            输入参数为 securities, start_date, end_date
            返回值为分组数据的 DataFrame 或 dict
        weights :
            权重数据, 默认为 1
            pd.DataFrame
            index 为日期, columns 为资产，为每个资产每天的权重.
            或 dict
            资产-权重映射的字典. 如果传递了dict，则假定权重映射在整个时间段内保持不变.
            或 function
            输入参数为 securities, start_date, end_date
            返回值为权重数据的 DataFrame 或 dict
        binning_by_group :
            bool
            如果为 True, 则对每个组分别计算分位数. 默认为 False
            适用于因子值范围在各个组上变化很大的情况.
            如果要分析分组(行业)中性的组合, 您最好设置为 True
        quantiles :
            int or sequence[float]
            默认为 None
            在因子分组中按照因子值大小平均分组的组数
            或分位数序列, 允许不均匀分组.
            例如 [0, .10, .5, .90, 1.] 或 [.05, .5, .95]
            'quantiles' 和 'bins' 有且只能有一个不为 None
        bins :
            int or sequence[float]
            默认为 None
            在因子分组中使用的等宽 (按照因子值) 区间的数量
            或边界值序列, 允许不均匀的区间宽度.
            例如 [-4, -2, -0.5, 0, 10]
            'quantiles' 和 'bins' 有且只能有一个不为 None
        periods :
            int or sequence[int]
            远期收益的期数, 默认为 (1, 5, 10)
        max_loss :
            float
            默认为 0.25
            允许的丢弃因子数据的最大百分比 (0.00 到 1.00),
            计算比较输入因子索引中的项目数和输出 DataFrame 索引中的项目数.
            因子数据本身存在缺陷 (例如 NaN),
            没有提供足够的价格数据来计算所有因子值的远期收益，
            或者因为分组失败, 因此可以部分地丢弃因子数据
            设置 max_loss = 0 以停止异常捕获.
        zero_aware :
            bool
            默认为 False
            如果为True，则分别为正负因子值计算分位数。
            适用于您的信号聚集并且零是正值和负值的分界线的情况.


    所有属性列表
    ----------
        factor_data:返回因子值
            - 类型: pandas.Series
            - index: 为日期和股票代码的MultiIndex
        clean_factor_data: 去除 nan/inf, 整理后的因子值、forward_return 和分位数
            - 类型: pandas.DataFrame
            - index: 为日期和股票代码的MultiIndex
            - columns: 根据period选择后的forward_return
                    (如果调仓周期为1天, 那么 forward_return 为
                        [第二天的收盘价-今天的收盘价]/今天的收盘价),
                    因子值、行业分组、分位数数组、权重
        mean_return_by_quantile: 按分位数分组加权平均因子收益
            - 类型: pandas.DataFrame
            - index: 分位数分组
            - columns: 调仓周期
        mean_return_std_by_quantile: 按分位数分组加权因子收益标准差
            - 类型: pandas.DataFrame
            - index: 分位数分组
            - columns: 调仓周期
        mean_return_by_date: 按分位数及日期分组加权平均因子收益
            - 类型: pandas.DataFrame
            - index: 为日期和分位数的MultiIndex
            - columns: 调仓周期
        mean_return_std_by_date: 按分位数及日期分组加权因子收益标准差
            - 类型: pandas.DataFrame
            - index: 为日期和分位数的MultiIndex
            - columns: 调仓周期
        mean_return_by_group: 按分位数及行业分组加权平均因子收益
            - 类型: pandas.DataFrame
            - index: 为行业和分位数的MultiIndex
            - columns: 调仓周期
        mean_return_std_by_group: 按分位数及行业分组加权因子收益标准差
            - 类型: pandas.DataFrame
            - index: 为行业和分位数的MultiIndex
            - columns: 调仓周期
        mean_return_spread_by_quantile: 最高分位数因子收益减最低分位数因子收益每日均值
            - 类型: pandas.DataFrame
            - index: 日期
            - columns: 调仓周期
        mean_return_spread_std_by_quantile: 最高分位数因子收益减最低分位数因子收益每日标准差
            - 类型: pandas.DataFrame
            - index: 日期
            - columns: 调仓周期
        cumulative_return_by_quantile:各分位数每日累积收益
            - 类型: pandas.DataFrame
            - index: 日期
            - columns: 调仓周期和分位数
        cumulative_returns: 按因子值加权多空组合每日累积收益
            - 类型: pandas.DataFrame
            - index: 日期
            - columns: 调仓周期
        top_down_cumulative_returns: 做多最高分位做空最低分位多空组合每日累计收益
            - 类型: pandas.DataFrame
            - index: 日期
            - columns: 调仓周期
        ic: 信息比率
            - 类型: pandas.DataFrame
            - index: 日期
            - columns: 调仓周期
        ic_by_group: 分行业信息比率
            - 类型: pandas.DataFrame
            - index: 行业
            - columns: 调仓周期
        ic_monthly: 月度信息比率
            - 类型: pandas.DataFrame
            - index: 月度
            - columns: 调仓周期表
        quantile_turnover: 换手率
            - 类型: dict
            - 键: 调仓周期
                - index: 日期
                - columns: 分位数分组

    所有方法列表
    ----------
        calc_mean_return_by_quantile:
            计算按分位数分组加权因子收益和标准差
        calc_factor_returns:
            计算按因子值加权多空组合每日收益
        compute_mean_returns_spread:
            计算两个分位数相减的因子收益和标准差
        calc_factor_alpha_beta:
            计算因子的 alpha 和 beta
        calc_factor_information_coefficient:
            计算每日因子信息比率 (IC值)
        calc_mean_information_coefficient:
            计算因子信息比率均值 (IC值均值)
        calc_average_cumulative_return_by_quantile:
            按照当天的分位数算分位数未来和过去的收益均值和标准差
        calc_cumulative_return_by_quantile:
            计算各分位数每日累积收益
        calc_cumulative_returns:
            计算按因子值加权多空组合每日累积收益
        calc_top_down_cumulative_returns:
            计算做多最高分位做空最低分位多空组合每日累计收益
        calc_autocorrelation:
            根据调仓周期确定滞后期的每天计算因子自相关性
        calc_autocorrelation_n_days_lag:
            后 1 - n 天因子值自相关性
        calc_quantile_turnover_mean_n_days_lag:
            各分位数 1 - n 天平均换手率
        calc_ic_mean_n_days_lag:
            滞后 0 - n 天 forward return 信息比率

        plot_returns_table: 打印因子收益表
        plot_turnover_table: 打印换手率表
        plot_information_table: 打印信息比率(IC)相关表
        plot_quantile_statistics_table: 打印各分位数统计表
        plot_ic_ts: 画信息比率(IC)时间序列图
        plot_ic_hist: 画信息比率分布直方图
        plot_ic_qq: 画信息比率 qq 图
        plot_quantile_returns_bar: 画各分位数平均收益图
        plot_quantile_returns_violin: 画各分位数收益分布图
        plot_mean_quantile_returns_spread_time_series: 画最高分位减最低分位收益图
        plot_ic_by_group: 画按行业分组信息比率(IC)图
        plot_factor_auto_correlation: 画因子自相关图
        plot_top_bottom_quantile_turnover: 画最高最低分位换手率图
        plot_monthly_ic_heatmap: 画月度信息比率(IC)图
        plot_cumulative_returns: 画按因子值加权组合每日累积收益图
        plot_top_down_cumulative_returns: 画做多最大分位数做空最小分位数组合每日累积收益图
        plot_cumulative_returns_by_quantile: 画各分位数每日累积收益图
        plot_quantile_average_cumulative_return: 因子预测能力平均累计收益图
        plot_events_distribution: 画有效因子数量统计图

        create_summary_tear_sheet: 因子值特征分析
        create_returns_tear_sheet: 因子收益分析
        create_information_tear_sheet: 因子 IC 分析
        create_turnover_tear_sheet: 因子换手率分析
        create_event_returns_tear_sheet: 因子预测能力分析
        create_full_tear_sheet: 全部分析

        plot_disable_chinese_label: 关闭中文图例显示
        """

    def __init__(self, factor, prices, groupby=None, weights=1.0,
                 quantiles=None, bins=None, periods=(1, 5, 10),
                 binning_by_group=False, max_loss=0.25, zero_aware=False):
        
        self.factor = factor
        self.prices = prices
        self.groupby = groupby
        self.weights = weights

        self._quantiles = quantiles
        self._bins = bins
        self._periods = periods
        self._binning_by_group = binning_by_group
        self._max_loss = max_loss
        self._zero_aware = zero_aware
        self._clean_factor_data = None
        self.__gen_clean_factor_and_forward_returns()

       
        #绘图相关配置
        self.figname = "factor_analyzer"
        self.plotpath = "./factor_dashboard"

    @property
    def mean_return_by_date(self):
        return self._mean_return_by_date.apply(utils.rate_of_return, axis=0)

    @property
    def _mean_return_by_date(self):
        _mean_return_by_date, _ = self.calc_mean_return_by_quantile(
            by_date=True,
            by_group=False,
            demeaned=False,
            group_adjust=False,
        )
        return _mean_return_by_date

    @property
    def mean_return_std_by_date(self):
        _, std_quant_daily = self.calc_mean_return_by_quantile(
            by_date=True,
            demeaned=False,
            by_group=False,
            group_adjust=False,
        )
        mean_return_std_by_date = std_quant_daily.apply(std_conversion, axis=0)

        return mean_return_std_by_date

    @property
    def mean_return_by_group(self):
        """分行业的分位数收益

        返回值:
            MultiIndex 的 DataFrame
            index 分别是分位数、 行业名称,  column 是 period  (1, 5, 10)
        """
        mean_return_group, _ = self.calc_mean_return_by_quantile(
            by_date=False,
            by_group=True,
            demeaned=True,
            group_adjust=False,
        )
        mean_return_group = mean_return_group.apply(utils.rate_of_return, axis=0)
        return mean_return_group

    @property
    def mean_return_std_by_group(self):
        _, mean_return_std_group = self.calc_mean_return_by_quantile(
            by_date=False,
            by_group=True,
            demeaned=True,
            group_adjust=False,
        )
        mean_return_std_group = mean_return_std_group.apply(std_conversion, axis=0)
        return mean_return_std_group

    @property
    def mean_return_spread_by_quantile(self):
        mean_return_spread_by_quantile, _ = self.compute_mean_returns_spread()
        return mean_return_spread_by_quantile

    @property
    def mean_return_spread_std_by_quantile(self):
        _, std_spread_quant = self.compute_mean_returns_spread()
        return std_spread_quant

    @property
    def ic(self):
        """IC 分析, 日度 ic

        返回 DataFrame, index 是时间,  column 是 period 的值 (1, 5, 10)
        """
        return self.calc_factor_information_coefficient()

    @property
    def ic_by_group(self):
        """行业 ic"""
        return self.calc_mean_information_coefficient(by_group=True)

    @property
    def ic_monthly(self):
        ic_monthly = self.calc_mean_information_coefficient(group_adjust=False,
                                                            by_group=False,
                                                            by_time="M").copy()
        ic_monthly.index = ic_monthly.index.map(lambda x: x.strftime('%Y-%m'))
        return ic_monthly

    @property
    def quantile_turnover(self):
        """换手率分析

        返回值一个 dict, key 是 period, value 是一个 DataFrame(index 是日期, column 是分位数)
        """

        quantile_factor = self._clean_factor_data['factor_quantile']
        quantile_turnover_rate = {
            convert_to_forward_returns_columns(p):
            pd.concat([perf.quantile_turnover(quantile_factor, q, p)
                       for q in range(1, int(quantile_factor.max()) + 1)],
                      axis=1)
            for p in self._periods
        }

        return quantile_turnover_rate

    def compute_mean_returns_spread(self, upper_quant=None, lower_quant=None,
                                    by_date=True, by_group=False,
                                    demeaned=False, group_adjust=False):
        """计算两个分位数相减的因子收益和标准差

        参数:
        upper_quant: 用 upper_quant 选择的分位数减去 lower_quant 选择的分位数
        lower_quant: 用 upper_quant 选择的分位数减去 lower_quant 选择的分位数
        by_date:
        - True: 按天计算两个分位数相减的因子收益和标准差
        - False: 不按天计算两个分位数相减的因子收益和标准差
        by_group:
        - True: 分行业计算两个分位数相减的因子收益和标准差
        - False: 不分行业计算两个分位数相减的因子收益和标准差
        demeaned:
        - True: 使用超额收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        - True: 使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性收益
        """
        upper_quant = upper_quant if upper_quant is not None else self._factor_quantile
        lower_quant = lower_quant if lower_quant is not None else 1
        if ((not 1 <= upper_quant <= self._factor_quantile) or
            (not 1 <= lower_quant <= self._factor_quantile)):
            raise ValueError("upper_quant 和 low_quant 的取值范围为 1 - %s 的整数"
                             % self._factor_quantile)
        mean, std = self.calc_mean_return_by_quantile(by_date=by_date, by_group=by_group,
                                                      demeaned=demeaned, group_adjust=group_adjust,)
        mean = mean.apply(utils.rate_of_return, axis=0)
        std = std.apply(std_conversion, axis=0)
        return perf.compute_mean_returns_spread(mean_returns=mean,
                                               upper_quant=upper_quant,
                                               lower_quant=lower_quant,
                                               std_err=std)

    @property
    def _factor_quantile(self):
        data = self.clean_factor_data
        if not data.empty:
            return max(data.factor_quantile)
        else:
            _quantiles = self._quantiles
            _bins = self._bins
            _zero_aware = self._zero_aware
            get_len = lambda x: len(x) - 1 if isinstance(x, Iterable) else int(x)
            if _quantiles is not None and _bins is None and not _zero_aware:
                return get_len(_quantiles)
            elif _quantiles is not None and _bins is None and _zero_aware:
                return int(_quantiles) // 2 * 2
            elif _bins is not None and _quantiles is None and not _zero_aware:
                return get_len(_bins)
            elif _bins is not None and _quantiles is None and _zero_aware:
                return int(_bins) // 2 * 2


    def __gen_clean_factor_and_forward_returns(self):
        """格式化因子数据和定价数据"""
        factor = self.factor.melt(col_level=0,value_vars=self.factor.columns,var_name="asset", value_name='factor',
             ignore_index=False
            ).set_index('asset', append=True)
        factor.index.names = ['date', 'asset']
     
        self._clean_factor_data = get_clean_factor_and_forward_returns(
        factor,
        self.prices,
        self.groupby,
        None,
        self._binning_by_group,
        self._quantiles,
        self._bins,
        self._periods,
        self._max_loss,
        self._zero_aware)
        #todo weight处理有问题，先绕过去
        '''
        self._clean_factor_data = get_clean_factor_and_forward_returns(
        factor,
        self.prices,
        self.groupby,
        self.weights,
        self._binning_by_group,
        self._quantiles,
        self._bins,
        self._periods,
        self._max_loss,
        self._zero_aware)
        '''
        self._clean_factor_data['weights'] = self.weights 
        #print(self._clean_factor_data)
       
        

    
    @property
    def clean_factor_data(self):
        return self._clean_factor_data

    def calc_mean_return_by_quantile(self, by_date=False, by_group=False,
                                     demeaned=False, group_adjust=False):
        """计算按分位数分组因子收益和标准差

        因子收益为收益按照 weight 列中权重的加权平均值

        参数:
        by_date:
        - True: 按天计算收益
        - False: 不按天计算收益
        by_group:
        - True: 按行业计算收益
        - False: 不按行业计算收益
        demeaned:
        - True: 使用超额收益计算各分位数收益，超额收益=收益-基准收益
                (基准收益被认为是每日所有股票收益按照weight列中权重的加权的均值)
        - False: 不使用超额收益
        group_adjust:
        - True: 使用行业中性收益计算各分位数收益，行业中性收益=收益-行业收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
        - False: 不使用行业中性收益
        """
        if by_date:
            mean_return_by_date, mean_return_std_by_date = perf.mean_return_by_quantile(
            self._clean_factor_data,
            by_date=True,
            by_group=by_group,
            demeaned=demeaned,
            group_adjust=group_adjust,
            )
            return (mean_return_by_date, mean_return_std_by_date)
        else:
            mean_return_by_quantile, mean_return_std_by_quantile = perf.mean_return_by_quantile(
            self._clean_factor_data,
            by_group=by_group,
            demeaned=demeaned,
            group_adjust=group_adjust,
            )
            return (mean_return_by_quantile, mean_return_std_by_quantile)
    
    @property
    def mean_return_by_quantile(self):
        """收益分析

        用来画分位数收益的柱状图

        返回 pandas.DataFrame, index 是 factor_quantile, 值是(1, 2, 3, 4, 5),
        column 是 period 的值 (1, 5, 10)
        """
        mean_ret_quantile, _ = self.calc_mean_return_by_quantile(
            by_date=False,
            by_group=False,
            demeaned=False,
            group_adjust=False,
        )
        mean_compret_quantile = mean_ret_quantile.apply(utils.rate_of_return, axis=0)
        return mean_compret_quantile

    @property
    def mean_return_std_by_quantile(self):
        """收益分析

        用来画分位数收益的柱状图

        返回 pandas.DataFrame, index 是 factor_quantile, 值是(1, 2, 3, 4, 5),
        column 是 period 的值 (1, 5, 10)
        """
        _, mean_ret_std_quantile = self.calc_mean_return_by_quantile(
            by_date=False,
            by_group=False,
            demeaned=False,
            group_adjust=False,
        )
        mean_ret_std_quantile = mean_ret_std_quantile.apply(utils.std_conversion, axis=0)
        return mean_ret_std_quantile

    def calc_cumulative_return_by_quantile(self, period=None, demeaned=False, group_adjust=False):
        """计算指定调仓周期的各分位数每日累积收益

        参数:
        period: 指定调仓周期
        demeaned:
        详见 calc_mean_return_by_quantile 中 demeaned 参数
        - True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        详见 calc_mean_return_by_quantile 中 group_adjust 参数
        - True: 使用行业中性化后的收益计算累积收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        """
        if period is None:
            period = self._periods[0]
        period_col = convert_to_forward_returns_columns(period)

        factor_returns = self.calc_mean_return_by_quantile(
            by_date=True, demeaned=demeaned, group_adjust=group_adjust
        )[0][period_col].unstack('factor_quantile')

        cum_ret = factor_returns.apply(perf.cumulative_returns, period=period)

        return cum_ret

    def calc_cumulative_returns(self, period=None,
                                demeaned=False, group_adjust=False):
        """计算指定调仓周期的按因子值加权组合每日累积收益

        当 period > 1 时，组合的累积收益计算方法为：
        组合每日收益 = （从第0天开始每period天一调仓的组合每日收益 +
                        从第1天开始每period天一调仓的组合每日收益 + ... +
                        从第period-1天开始每period天一调仓的组合每日收益) / period
        组合累积收益 = 组合每日收益的累积

        参数:
        period: 指定调仓周期
        demeaned:
        详见 calc_factor_returns 中 demeaned 参数
        - True: 对权重去均值 (每日权重 = 每日权重 - 每日权重的均值), 使组合转换为 cash-neutral 多空组合
        - False: 不对权重去均值
        group_adjust:
        详见 calc_factor_returns 中 group_adjust 参数
        - True: 对权重分行业去均值 (每日权重 = 每日权重 - 每日各行业权重的均值)，
                使组合转换为 industry-neutral 多空组合
        - False: 不对权重分行业去均值
        """
        if period is None:
            period = self._periods[0]
        period_col = convert_to_forward_returns_columns(period)
        factor_returns = self.calc_factor_returns(
            demeaned=demeaned, group_adjust=group_adjust
        )[period_col]

        return perf.cumulative_returns(factor_returns, period=period)

    def create_full_tear_sheet(self, demeaned=False, group_adjust=False, by_group=False,
                               turnover_periods=None, avgretplot=(5, 15), std_bar=False, html_output=False,html_filename=None):
        """全部分析

        参数:
        demeaned:
        - True：使用超额收益计算 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False：不使用超额收益
        group_adjust:
        - True：使用行业中性化后的收益计算
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False：不使用行业中性化后的收益
        by_group:
        - True: 按行业展示
        - False: 不按行业展示
        turnover_periods: 调仓周期
        avgretplot: tuple 因子预测的天数
        -(计算过去的天数, 计算未来的天数)
        std_bar:
        - True: 显示标准差
        - False: 不显示标准差
        """
        charts = []
        self.plot_quantile_statistics_table()
        print("\n-------------------------\n")
        self.plot_returns_table(demeaned=demeaned, group_adjust=group_adjust)
        charts.extend(self.plot_quantile_returns_bar(by_group=False,
                                       demeaned=demeaned,
                                       group_adjust=group_adjust))
       
        charts.extend(self.plot_cumulative_returns(period=None, demeaned=demeaned, group_adjust=group_adjust))
       
        charts.extend(self.plot_top_down_cumulative_returns(period=None,
                                              demeaned=demeaned,
                                              group_adjust=group_adjust))
       
        charts.extend(self.plot_cumulative_returns_by_quantile(period=None,
                                                 demeaned=demeaned,
                                                 group_adjust=group_adjust))
        charts.extend(self.plot_mean_quantile_returns_spread_time_series(demeaned=demeaned,
                                                           group_adjust=group_adjust))
       
        if by_group and 'group' in self._clean_factor_data.columns:
            charts.extend(self.plot_quantile_returns_bar(by_group=True,
                                           demeaned=demeaned,
                                           group_adjust=group_adjust))
        '''   
        self.plot_quantile_returns_violin(demeaned=demeaned,
                                          group_adjust=group_adjust)
        '''
       
        print("\n-------------------------\n")
        self.plot_information_table(group_adjust=group_adjust)
        charts.extend(self.plot_ic_ts(group_adjust=group_adjust, method=None))
       
        #self.plot_ic_qq(group_adjust=group_adjust)
       
        if by_group and 'group' in self._clean_factor_data.columns:
            charts.extend(self.plot_ic_by_group(group_adjust=group_adjust, method=None))
        else:
            charts.extend(self.plot_monthly_ic_heatmap(group_adjust=group_adjust))
       
        print("\n-------------------------\n")
        self.plot_turnover_table()
        charts.extend(self.plot_top_bottom_quantile_turnover(periods=turnover_periods))
       
        charts.extend(self.plot_factor_auto_correlation(periods=turnover_periods))
       
        print("\n-------------------------\n")
        before, after = avgretplot
        charts.extend(self.plot_quantile_average_cumulative_return(
            periods_before=before, periods_after=after,
            by_quantile=False, std_bar=False,
            demeaned=demeaned, group_adjust=group_adjust
        ))
       
        if std_bar:
            charts.extend(self.plot_quantile_average_cumulative_return(
                periods_before=before, periods_after=after,
                by_quantile=True, std_bar=True,
                demeaned=demeaned, group_adjust=group_adjust
            ))
        if html_output:
            if not html_filename:
                html_filename = "full_tear_sheet.html"
            print(f"html path at: {os.path.join(self.plotpath, html_filename)}")
            plotting.show_one_page(charts, html_filename, self.plotpath)
        else:
            try:
                from IPython.display import display
                for chart in charts:
                    display(chart.render_notebook())
            except Exception as e:
                print("cat not output at jupyter env")
                print("please set param(html_output=True) to display at html file")
           

    def plot_returns_table(self, demeaned=False, group_adjust=False):
        """打印因子收益表

        参数:
        demeaned:
        - True: 使用超额收益计算 (基准收益被认为是每日所有股票收益按照weight列中权重的加权的均值)
        - False: 不使用超额收益
        group_adjust:
        - True: 使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
        - False: 不使用行业中性收益
        """
        mean_return_by_quantile = self.calc_mean_return_by_quantile(
            by_date=False, by_group=False,
            demeaned=demeaned, group_adjust=group_adjust,
        )[0].apply(utils.rate_of_return, axis=0)

        mean_returns_spread, _ = self.compute_mean_returns_spread(
            upper_quant=self._quantile,
            lower_quant=1,
            by_date=True,
            by_group=False,
            demeaned=demeaned,
            group_adjust=group_adjust,
        )

        plotting.plot_returns_table(
            self.calc_factor_alpha_beta(demeaned=demeaned),
            mean_return_by_quantile,
            mean_returns_spread
        )


       
    def plot_quantile_returns_bar(self, by_group=False,
                                  demeaned=False, group_adjust=False):
        """画各分位数平均收益图

        参数:
        by_group:
        - True: 各行业的各分位数平均收益图
        - False: 各分位数平均收益图
        demeaned:
        - True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        - True: 使用行业中性化后的收益计算累积收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        """
        self.calc_mean_return_by_quantile(
            by_date=False, by_group=by_group,
            demeaned=demeaned, group_adjust=group_adjust,
        )
        mean_ratereturn_by_quantile = self.mean_return_by_quantile.apply(
        utils.rate_of_return,
        axis=0,
        base_period=1,
        )
       
        factor_name = "plot_quantile_returns_bar"
        charts = []
        charts.extend(
            plotting.plot_quantile_returns_bars(mean_ratereturn_by_quantile, by_group=False)
        )
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
       
    def calc_factor_returns(self, demeaned=True, group_adjust=False):
        """计算按因子值加权组合每日收益

        权重 = 每日因子值 / 每日因子值的绝对值的和
        正的权重代表买入, 负的权重代表卖出

        参数:
        demeaned:
        - True: 对权重去均值 (每日权重 = 每日权重 - 每日权重的均值), 使组合转换为 cash-neutral 多空组合
        - False: 不对权重去均值
        group_adjust:
        - True: 对权重分行业去均值 (每日权重 = 每日权重 - 每日各行业权重的均值)，
                使组合转换为 industry-neutral 多空组合
        - False: 不对权重分行业去均值
        """
        return perf.factor_returns(self._clean_factor_data)
        

    def plot_cumulative_returns(self, period=None, demeaned=False,
                                group_adjust=False):
        """画按因子值加权组合每日累积收益图

        参数:
        periods: 调仓周期
        demeaned:
        详见 calc_factor_returns 中 demeaned 参数
        - True: 对因子值加权组合每日收益的权重去均值 (每日权重 = 每日权重 - 每日权重的均值),
                使组合转换为cash-neutral多空组合
        - False: 不对权重去均值
        group_adjust:
        详见 calc_factor_returns 中 group_adjust 参数
        - True: 对权重分行业去均值 (每日权重 = 每日权重 - 每日各行业权重的均值)，
                使组合转换为 industry-neutral 多空组合
        - False: 不对权重分行业去均值
        """
        if period is None:
            period = self._periods
        
        period = tuple(period)
        factor_returns = self.calc_factor_returns(demeaned=demeaned,
                                                  group_adjust=group_adjust)
       
        factor_name = "plot_cumulative_returns"
        charts = []
        charts.extend(
            [plotting.plot_cumulative_returns(factor_returns)]
        )
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
       

    def plot_cumulative_returns_by_quantile(self, period=None, demeaned=False,
                                            group_adjust=False):
        """画各分位数每日累积收益图

        参数:
        period: 调仓周期
        demeaned:
        详见 calc_mean_return_by_quantile 中 demeaned 参数
        - True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        详见 calc_mean_return_by_quantile 中 group_adjust 参数
        - True: 使用行业中性化后的收益计算累积收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        """
        if period is None:
            period = self._periods
        period = tuple(period)
        mean_return_by_date, _ = self.calc_mean_return_by_quantile(
            by_date=True, by_group=False, demeaned=demeaned, group_adjust=group_adjust,
        )
       
        factor_name = "plot_cumulative_returns_by_quantile"
        charts = []
        charts.extend(
            [plotting.plot_cumulative_returns_by_quantile(mean_return_by_date, period=5)]
        )
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
       
        
    def plot_mean_quantile_returns_spread_time_series(
        self, demeaned=False, group_adjust=False, bandwidth=1
    ):
        """画最高分位减最低分位收益图

        参数:
        demeaned:
        - True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        - True: 使用行业中性化后的收益计算累积收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        bandwidth: n, 加减 n 倍当日标准差
        """
        mean_quant_ret_bydate, std_quant_daily = perf.mean_return_by_quantile(
        self._clean_factor_data,
        by_date=True,
        by_group=False,
        demeaned=demeaned,
        group_adjust=group_adjust,
        )

        compstd_quant_daily = std_quant_daily.apply(
        utils.std_conversion, axis=0, base_period=1
        )

        mean_quant_rateret_bydate = mean_quant_ret_bydate.apply(
        utils.rate_of_return,
        axis=0,
        base_period=1,
        )
        mean_returns_spread, mean_returns_spread_std = perf.compute_mean_returns_spread(
        mean_quant_rateret_bydate,
        self._clean_factor_data["factor_quantile"].max(),
        self._clean_factor_data["factor_quantile"].min(),
        std_err=compstd_quant_daily,
        )
      
        factor_name = "plot_mean_quantile_returns_spread_time_series"
        charts = []
        charts.extend(
            [plotting.plot_mean_quantile_returns_spread_time_series(mean_returns_spread, mean_returns_spread_std, col="period_1")]
        )
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
        
    def create_summary_tear_sheet(self, demeaned=False, group_adjust=False):
        """因子值特征分析

        参数:
        demeaned:
        - True: 对每日因子收益去均值求得因子收益表
        - False: 因子收益表
        group_adjust:
        - True: 按行业对因子收益去均值后求得因子收益表
        - False: 因子收益表
        """
        self.plot_quantile_statistics_table()
        self.plot_returns_table(demeaned=demeaned, group_adjust=group_adjust)
        self.plot_quantile_returns_bar(by_group=False, demeaned=demeaned, group_adjust=group_adjust)
        self.plot_information_table(group_adjust=group_adjust)
        self.plot_turnover_table()
        #if html_output:
        #    show_one_page(charts, "summary_tear_sheet", self.plotpath)
        #else:
        #    for chart in charts:
        #        chart.render_notebook()

    def create_returns_tear_sheet(self, demeaned=False, group_adjust=False, by_group=False, html_output=False):
        """因子收益分析

        参数:
        demeaned:
        详见 calc_mean_return_by_quantile 中 demeaned 参数
        - True: 使用超额收益计算 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        详见 calc_mean_return_by_quantile 中 group_adjust 参数
        - True: 使用行业中性化后的收益计算 (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        by_group:
        - True: 画各行业的各分位数平均收益图
        - False: 不画各行业的各分位数平均收益图
        """
        
        self.plot_returns_table(demeaned=demeaned, group_adjust=group_adjust)
        
        charts = list(itertools.chain(
            self.plot_quantile_returns_bar(by_group=False,
                                       demeaned=demeaned,
                                       group_adjust=group_adjust),
            self.plot_cumulative_returns(
                period=None, demeaned=demeaned, group_adjust=group_adjust
            ),
            self.plot_cumulative_returns_by_quantile(period=None,
                                                 demeaned=demeaned,
                                                 group_adjust=group_adjust),
            self.plot_mean_quantile_returns_spread_time_series(
                demeaned=demeaned, group_adjust=group_adjust
            )
        ))
        
        if by_group and 'group' in self._clean_factor_data.columns:
            charts.extend(self.plot_quantile_returns_bar(by_group=True,
                                           demeaned=demeaned,
                                           group_adjust=group_adjust))
            
                                    
        charts.extend(self.plot_top_down_cumulative_returns(period=None,
                                              demeaned=demeaned,
                                              group_adjust=group_adjust))
        if html_output:
            plotting.show_one_page(charts, "returns_tear_sheet.html", self.plotpath)
        else:
            for chart in charts:
                print(chart)
                chart.render_notebook()

        '''  
        #不支持                                    
        self.plot_quantile_returns_violin(demeaned=demeaned,
                                          group_adjust=group_adjust)
        '''
        
    def create_information_tear_sheet(self, group_adjust=False, by_group=False):
        """因子 IC 分析

        参数:
        group_adjust:
        - True: 使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
        - False: 不使用行业中性收益
        by_group:
        - True: 画按行业分组信息比率(IC)图
        - False: 画月度信息比率(IC)图
        """
        self.plot_ic_ts(group_adjust=group_adjust, method=None)
        
        if by_group and 'group' in self._clean_factor_data.columns:
            self.plot_ic_by_group(group_adjust=group_adjust, method=None)
        else:
            self.plot_monthly_ic_heatmap(group_adjust=group_adjust)
       
        '''
        #不支持
        self.plot_ic_qq(group_adjust=group_adjust)
        '''
   
    def create_turnover_tear_sheet(self, turnover_periods=None):
        """因子换手率分析

        参数:
        turnover_periods: 调仓周期
        """
        self.plot_turnover_table()
        self.plot_top_bottom_quantile_turnover(periods=turnover_periods)
       
        self.plot_factor_auto_correlation(periods=turnover_periods)
    

    def calc_factor_alpha_beta(self, demeaned=True, group_adjust=False):
        """计算因子的 alpha 和 beta

        因子值加权组合每日收益 = beta * 市场组合每日收益 + alpha

        因子值加权组合每日收益计算方法见 calc_factor_returns 函数
        市场组合每日收益是每日所有股票收益按照weight列中权重加权的均值
        结果中的 alpha 是年化 alpha

        参数:
        demeaned:
        详见 calc_factor_returns 中 demeaned 参数
        - True: 对因子值加权组合每日收益的权重去均值 (每日权重 = 每日权重 - 每日权重的均值),
                使组合转换为cash-neutral多空组合
        - False: 不对权重去均值
        group_adjust:
        详见 calc_factor_returns 中 group_adjust 参数
        - True: 对权重分行业去均值 (每日权重 = 每日权重 - 每日各行业权重的均值)，
                使组合转换为 industry-neutral 多空组合
        - False: 不对权重分行业去均值
        """
        factor_returns = perf.factor_returns(
        self._clean_factor_data
        )
        return perf.factor_alpha_beta(
        self._clean_factor_data, factor_returns, demeaned, group_adjust)



    def calc_factor_information_coefficient(self, group_adjust=False, by_group=False, method=None):
        """计算每日因子信息比率 (IC值)

        参数:
        group_adjust:
        - True: 使用行业中性收益计算 IC (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性收益
        by_group:
        - True: 分行业计算 IC
        - False: 不分行业计算 IC
        method:
        - 'rank': 用秩相关系数计算IC值
        - 'normal': 用普通相关系数计算IC值
        """
        if method is None:
            method = 'rank'
        if method not in ('rank', 'normal'):
            raise (DataError("`method` should be chosen from ('rank' | 'normal')"))

        if method == 'rank':
            method = spearmanr 
        elif method == 'normal':
            method = pearsonr
        return perf.factor_information_coefficient(self._clean_factor_data,group_adjust, by_group, method)



    def calc_mean_information_coefficient(self, group_adjust=False, by_group=False,
                                          by_time=None, method=None):
        """计算因子信息比率均值 (IC值均值)

        参数:
        group_adjust:
        - True: 使用行业中性收益计算 IC (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性收益
        by_group:
        - True: 分行业计算 IC
        - False: 不分行业计算 IC
        by_time:
        - 'Y': 按年求均值
        - 'M': 按月求均值
        - None: 对所有日期求均值
        method:
        - 'rank': 用秩相关系数计算IC值
        - 'normal': 用普通相关系数计算IC值
        """
        if method is None:
            method = 'rank'
        if method not in ('rank', 'normal'):
            raise (DataError("`method` should be chosen from ('rank' | 'normal')"))

        if method == 'rank':
            method = spearmanr
        elif method == 'normal':
            method = pearsonr
        return perf.mean_information_coefficient(self._clean_factor_data,group_adjust,by_group,by_time, method)

    def calc_average_cumulative_return_by_quantile(self, periods_before, periods_after,
                                                   demeaned=False, group_adjust=False):
        """按照当天的分位数算分位数未来和过去的收益均值和标准差

        参数:
        periods_before: 计算过去的天数
        periods_after: 计算未来的天数
        demeaned:
        - True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        - True: 使用行业中性化后的收益计算累积收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        """
        return  perf.average_cumulative_return_by_quantile(
            self._clean_factor_data,
            returns=self.prices,
            periods_before=periods_before,
            periods_after=periods_after,
            demeaned=demeaned,
            group_adjust=group_adjust
        )

    def calc_autocorrelation_n_days_lag(self, n=10, rank=False):
        """滞后1-n天因子值自相关性

        参数:
        n: 滞后1天到n天的因子值自相关性
        rank:
        - True: 秩相关系数
        - False: 普通相关系数
        """
        return pd.Series(
            [
                perf.factor_autocorrelation(self._clean_factor_data, p, rank=rank).mean()
                for p in range(1, n + 1)
            ],
            index='lag_' + pd.Index(range(1, n + 1)).astype(str)
        )

    def calc_quantile_turnover_mean_n_days_lag(self, n=10):
        """各分位数滞后1天到n天的换手率均值

        参数:
        n: 滞后 1 天到 n 天的换手率
        """
        quantile_factor = self._clean_factor_data['factor_quantile']

        quantile_turnover_rate = pd.concat(
            [pd.Series([perf.quantile_turnover(quantile_factor, q, p).mean()
                        for q in range(1, int(quantile_factor.max()) + 1)],
                       index=range(1, int(quantile_factor.max()) + 1),
                       name=p)
             for p in range(1, n + 1)],
            axis=1, keys='lag_' + pd.Index(range(1, n + 1)).astype(str)
        ).T
        quantile_turnover_rate.columns.name = 'factor_quantile'

        return quantile_turnover_rate

    def calc_ic_mean_n_days_lag(self, n=10, group_adjust=False, by_group=False, method=None):
        """滞后 0 - n 天因子收益信息比率(IC)的均值

        滞后 n 天 IC 表示使用当日因子值和滞后 n 天的因子收益计算 IC

        参数:
        n: 滞后0-n天因子收益的信息比率(IC)的均值
        group_adjust:
        - True: 使用行业中性收益计算 IC (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性收益
        by_group:
        - True: 分行业计算 IC
        - False: 不分行业计算 IC
        method:
        - 'rank': 用秩相关系数计算IC值
        - 'normal': 用普通相关系数计算IC值
        """
        ic = self.calc_factor_information_coefficient(group_adjust=group_adjust, by_group=by_group, method=method)
        ic_mean = []
        if by_group and 'group' in ic.columns:
            ic_mean.append([ic.groupby('group').mean()])
        else:
            ic_mean.append([ic.mean()])

        
        for lag in range(1, n + 1):
            ic_mean.append(self._calc_ic_mean_n_day_lag(
                n=lag,
                group_adjust=group_adjust,
                by_group=by_group,
                method=method
            ))
        ic_mean = [pd.DataFrame(lst) for lst in ic_mean]
        if not by_group:
            ic_mean = pd.concat(ic_mean, keys='lag_' + pd.Index(range(n + 1)).astype(str), axis=1)
            ic_mean = ic_mean.T
        else:
            ic_mean = pd.concat(ic_mean, keys='lag_' + pd.Index(range(n + 1)).astype(str), axis=0)
        
        return ic_mean

    def _calc_ic_mean_n_day_lag(self, n, group_adjust=False, by_group=False, method=None):
        if method is None:
            method = 'rank'
        if method not in ('rank', 'normal'):
            raise ValueError("`method` should be chosen from ('rank' | 'normal')")

        if method == 'rank':
            method = spearmanr
        elif method == 'normal':
            method = pearsonr

        factor_data = self._clean_factor_data.copy()
        factor_value = factor_data['factor'].unstack('asset')

        factor_data['factor'] = factor_value.shift(n).stack(dropna=True)
        if factor_data.dropna().empty:
            return pd.Series(np.nan, index=perf.get_forward_returns_columns(factor_data.columns))
        ac = perf.factor_information_coefficient(
            factor_data.dropna(),
            group_adjust=group_adjust, by_group=by_group,
            method=method
        )
        ac_mean = []
        if by_group and 'group' in ac.columns:
            ac_mean = [ac.groupby('group').mean()]
        else:
            ac_mean = [ac.mean()]
        return ac_mean

    def plot_ic_hist(self, group_adjust=False, method=None):
        """画信息比率分布直方图

        参数:
        group_adjust:
        - True: 使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
        - False: 不使用行业中性收益
        method:
        - 'rank': 用秩相关系数计算IC值
        - 'normal': 用相关系数计算IC值
        """
        ic_data = perf.factor_information_coefficient(self._clean_factor_data,group_adjust = group_adjust)
       
        factor_name = "plot_ic_hist"
        charts = []
        charts.extend([
            plotting.plot_ic_hist(ic_data)
        ])
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
    
    def plot_ic_ts(self, group_adjust=False, method=None):
        """画信息比率(IC)时间序列图

        参数:
        group_adjust:
        - True: 使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
        - False: 不使用行业中性收益
        method:
        - 'rank': 用秩相关系数计算IC值
        - 'normal':用相关系数计算IC值
        """
        ic = self.calc_factor_information_coefficient(
            group_adjust=group_adjust, by_group=False, method=method
        )
        factor_name = "plot_ic_ts"
        charts = []
        charts.extend([
            plotting.plot_ic_ts(ic)
        ])
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
    
    '''
    def plot_ic_qq(self, group_adjust=False, method=None, theoretical_dist=None):
        """画信息比率 qq 图

        参数:
        group_adjust:
        - True: 使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
        - False: 不使用行业中性收益
        method:
        - 'rank': 用秩相关系数计算IC值
        - 'normal': 用相关系数计算IC值
        theoretical_dist:
        - 'norm': 正态分布
        - 't': t 分布
        """
        theoretical_dist = 'norm' if theoretical_dist is None else theoretical_dist
        theoretical_dist = getattr(stats, theoretical_dist)
        ic = self.calc_factor_information_coefficient(
            group_adjust=group_adjust,
            by_group=False,
            method=method,
        )
        factor_name = "plot_ic_qq"
        charts = []
        charts.extend([
            plotting.plot_ic_qq(ic)
        ])
        plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
    '''

    def plot_quantile_returns_bar(self, by_group=False,
                                  demeaned=False, group_adjust=False):
        """画各分位数平均收益图

        参数:
        by_group:
        - True: 各行业的各分位数平均收益图
        - False: 各分位数平均收益图
        demeaned:
        - True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        - True: 使用行业中性化后的收益计算累积收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        """
        mean_quant_ret, std_quantile = self.calc_mean_return_by_quantile(
            by_date=False, by_group=by_group,
            demeaned=demeaned, group_adjust=group_adjust,
        )

        mean_quant_rateret = mean_quant_ret.apply(
        utils.rate_of_return, axis=0, base_period=1)
        factor_name = "plot_quantile_returns_bar"
        charts = []
        charts.extend(
            plotting.plot_quantile_returns_bars(mean_quant_rateret, by_group=by_group)
        )
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
       
    def plot_factor_auto_correlation(self, periods=None, rank=True):
        """画因子自相关图

        参数:
        periods: 滞后周期
        rank:
        - True: 用秩相关系数
        - False: 用相关系数
        """
        if periods is None:
            periods = self._periods
        
        factor_name = "plot_factor_auto_correlation"
        charts = []

        for p in periods:
            factor_autocorrelation = perf.factor_rank_autocorrelation(self._clean_factor_data, p)
            charts.extend([
            plotting.plot_factor_rank_auto_correlation(factor_autocorrelation, p)
            ])
        
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
       


    def calc_top_down_cumulative_returns(self, period=None,
                                         demeaned=False, group_adjust=False):
        """计算做多最大分位，做空最小分位组合每日累积收益

        参数:
        period: 指定调仓周期
        demeaned:
        详见 calc_mean_return_by_quantile 中 demeaned 参数
        - True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        详见 calc_mean_return_by_quantile 中 group_adjust 参数
        - True: 使用行业中性化后的收益计算累积收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        """
        if period is None:
            period = self._periods[0]
        period_col = convert_to_forward_returns_columns(period)
        mean_returns, _ = self.calc_mean_return_by_quantile(
            by_date=True, by_group=False,
            demeaned=demeaned, group_adjust=group_adjust,
        )

        upper_quant = mean_returns[period_col].xs(self._quantiles,
                                                  level='factor_quantile')
        lower_quant = mean_returns[period_col].xs(1,
                                                  level='factor_quantile')
        ret = perf.cumulative_returns(upper_quant - lower_quant, period=period)
        return ret 

    def calc_autocorrelation(self, rank=True):
        """根据调仓周期确定滞后期的每天计算因子自相关性

        当日因子值和滞后period天的因子值的自相关性

        参数:
        rank:
        - True: 秩相关系数
        - False: 普通相关系数
        """
        ret = pd.concat(
            [
                perf.factor_autocorrelation(self._clean_factor_data,
                                           period, rank=rank)
                for period in self._periods
            ],
            axis=1,
            keys=list(map(convert_to_forward_returns_columns, self._periods))
        )
        return ret

    def plot_top_bottom_quantile_turnover(self, periods=None):
        """画最高最低分位换手率图

        参数:
        periods: 调仓周期
        """
        quantile_turnover = self.quantile_turnover

        if periods is None:
            periods = self._periods

        factor_name = "plot_top_bottom_quantile_turnover"
        charts = []

        for p in periods:
            charts.extend([
            plotting.plot_top_bottom_quantile_turnover(self._clean_factor_data["factor_quantile"], p)
            ])
        
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
       
    
    def plot_quantile_average_cumulative_return(self, periods_before=5, periods_after=10,
                                                by_quantile=False, std_bar=False,
                                                demeaned=False, group_adjust=False):
        """因子预测能力平均累计收益图

        参数:
        periods_before: 计算过去的天数
        periods_after: 计算未来的天数
        by_quantile: 是否各分位数分别显示因子预测能力平均累计收益图
        std_bar:
        - True: 显示标准差
        - False: 不显示标准差
        demeaned:
        详见 calc_mean_return_by_quantile 中 demeaned 参数
        - True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        详见 calc_mean_return_by_quantile 中 group_adjust 参数
        - True: 使用行业中性化后的收益计算累积收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        """
        average_cumulative_return_by_q = self.calc_average_cumulative_return_by_quantile(
            periods_before=periods_before, periods_after=periods_after,
            demeaned=demeaned, group_adjust=group_adjust
        )
        
        factor_name = "plot_quantile_average_cumulative_return"
        charts = []
        
        charts.extend([
        plotting.plot_quantile_average_cumulative_return(average_cumulative_return_by_q,
                                                   by_quantile=by_quantile,
                                                   std_bar=std_bar,
                                                   periods_before=periods_before,
                                                   periods_after=periods_after)
        ])
        
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
    
          
    
    def create_event_returns_tear_sheet(self, avgretplot=(5, 15),
                                        demeaned=False, group_adjust=False,
                                        std_bar=False):
        """因子预测能力分析

        参数:
        avgretplot: tuple 因子预测的天数
        -(计算过去的天数, 计算未来的天数)
        demeaned:
        详见 calc_mean_return_by_quantile 中 demeaned 参数
        - True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        详见 calc_mean_return_by_quantile 中 group_adjust 参数
        - True: 使用行业中性化后的收益计算累积收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        std_bar:
        - True: 显示标准差
        - False: 不显示标准差
        """
        before, after = avgretplot
        if std_bar:
            self.plot_quantile_average_cumulative_return(
                periods_before=before, periods_after=after,
                by_quantile=True, std_bar=True,
                demeaned=demeaned, group_adjust=group_adjust
            )
        else:
            self.plot_quantile_average_cumulative_return(
            periods_before=before, periods_after=after,
            by_quantile=False, std_bar=False,
            demeaned=demeaned, group_adjust=group_adjust
        )

    def plot_returns_table(self, demeaned=False, group_adjust=False):
        """打印因子收益表

        参数:
        demeaned:
        - True: 使用超额收益计算 (基准收益被认为是每日所有股票收益按照weight列中权重的加权的均值)
        - False: 不使用超额收益
        group_adjust:
        - True: 使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
        - False: 不使用行业中性收益
        """
        mean_return_by_quantile = self.calc_mean_return_by_quantile(
            by_date=False, by_group=False,
            demeaned=demeaned, group_adjust=group_adjust,
        )[0].apply(utils.rate_of_return, axis=0, base_period=1)
        
        mean_returns_spread, _ = self.compute_mean_returns_spread(
            upper_quant=self._quantiles,
            lower_quant=1,
            by_date=True,
            by_group=False,
            demeaned=demeaned,
            group_adjust=group_adjust,
        )

        plotting.plot_returns_table(
            self.calc_factor_alpha_beta(demeaned=demeaned),
            mean_return_by_quantile,
            mean_returns_spread
        )

    def plot_turnover_table(self):
        """打印换手率表"""
        charts = [plotting.plot_turnover_table(
            self.calc_autocorrelation(),
            self.quantile_turnover
        )]
        return charts
    
    def plot_information_table(self, group_adjust=False, method=None):
        """打印信息比率 (IC)相关表

        参数:
        group_adjust:
        - True：使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
        - False：不使用行业中性收益
        method：
        - 'rank'：用秩相关系数计算IC值
        - 'normal':用相关系数计算IC值
        """
        ic = self.calc_factor_information_coefficient(
            group_adjust=group_adjust,
            by_group=False,
            method=method
        )
        charts = [plotting.plot_information_table(ic)]
        return charts
    
    def plot_quantile_statistics_table(self):
        """打印各分位数统计表"""
        df = self._clean_factor_data
        if 'group' in df.columns:
            df = df.drop('group',axis=1)

        charts = [plotting.plot_quantile_statistics_table(df)]
        return charts
    
    def plot_ic_by_group(self, group_adjust=False, method=None):
        """画按行业分组信息比率(IC)图

        参数:
        group_adjust:
        - True: 使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
        - False: 不使用行业中性收益
        method:
        - 'rank': 用秩相关系数计算IC值
        - 'normal': 用相关系数计算IC值
        """
        if  not 'group' in self._clean_factor_data.columns:
            print("no group info. set group info by groupby")
            return
        ic_by_group = self.calc_mean_information_coefficient(
            group_adjust=group_adjust,
            by_group=True,
            method=method
        )
        charts = [plotting.plot_ic_by_group(ic_by_group)]
        return charts
    
    
    def plot_events_distribution(self, num_days=5):
        """画有效因子数量统计图

        参数:
        num_days: 统计间隔天数
        """
        factor_name = "plot_events_distribution"
        charts = []
        
        charts.extend([
        plotting.plot_events_distribution(
            events=self._clean_factor_data['factor'],
            num_days=num_days,
            full_dates=pd.to_datetime(self._clean_factor_data.index.get_level_values('date').unique()))
        ])
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts

    def plot_monthly_ic_heatmap(self, group_adjust=False):
        """画月度信息比率(IC)图

        参数:
        group_adjust:
        - True: 使用行业中性收益 (行业收益被认为是每日各个行业股票收益按照weight列中权重的加权的均值)
        - False: 不使用行业中性收益
        """
        ic_monthly = self.calc_mean_information_coefficient(
            group_adjust=group_adjust, by_group=False, by_time="M"
        )

        factor_name = "plot_monthly_ic_heatmap"
        charts = []

        new_index_year = []
        new_index_month = []
        for date in ic_monthly.index:
            new_index_year.append(date.year)
            new_index_month.append(date.month)

        ic_monthly.index = pd.MultiIndex.from_arrays(
            [new_index_year, new_index_month], names=["year", "month"]
        )

        for (period, ic) in ic_monthly.items():
            periods_num = period.replace('period_', '')
            charts.extend([
            plotting.plot_monthly_ic_heatmap(ic.unstack(), periods_num)
            ])
            
        
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
    
    def plot_top_down_cumulative_returns(self, period=None, demeaned=False, group_adjust=False):
        """画做多最大分位数做空最小分位数组合每日累积收益图

        period: 指定调仓周期
        demeaned:
        详见 calc_mean_return_by_quantile 中 demeaned 参数
        - True: 使用超额收益计算累积收益 (基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)
        - False: 不使用超额收益
        group_adjust:
        详见 calc_mean_return_by_quantile 中 group_adjust 参数
        - True: 使用行业中性化后的收益计算累积收益
                (行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)
        - False: 不使用行业中性化后的收益
        """
        if period is None:
            period = self._periods
        if not isinstance(period, Iterable):
            period = (period, )
        period = tuple(period)
        
        factor_name = "plot_top_down_cumulative_returns"
        charts = []
        for p in period:
            if p in self._periods:
                factor_return = self.calc_top_down_cumulative_returns(
                    period=p, demeaned=demeaned, group_adjust=group_adjust,
                )
                
                charts.extend([
                plotting.plot_top_down_cumulative_returns(
                    factor_return, period=p
                )
                ])
        
        #plotting.show_one_page(charts, f'{self.figname}.{factor_name}.{plotting.conf["theme"]}.html', self.plotpath)
        return charts
    
    
        
    def set_plot_path(self, path):
        """设置绘图输出路径，默认是./factor_dashboard

        参数:
        path: 路径
        """   
        self.plotpath = path 

    
    
'''

def alpha101(close, open_, high, low):
    return (close - open_) / (high - low + 0.001)


if __name__ == "__main__":
    

    fs = glob.glob("/home/wangdanfeng/calculator_jobs/f_calc/kline_day/*.parquet")
    dfs = pd.concat([pd.read_parquet(f) for f in fs])

    df_panel = dfs.pivot(index='dt', columns='code')

    factor_data = alpha101(df_panel["close"],df_panel["open"], df_panel["high"], df_panel["low"])
    
    groupby = factor_data.applymap(lambda x:str(np.random.randint(10)))
    

    prices = dfs.pivot(index='dt', columns='code', values='close').bfill()
    prices.index.name='Date'
    far = FactorAnalyzer(factor_data, prices, groupby=groupby, weights=1.0,
                    quantiles=5, bins=None, periods=(1, 5, 10),
                    binning_by_group=False, max_loss=0.25, zero_aware=False)
    far.set_plot_path("/home/wangdanfeng/deepquantsdk/deepquant/factor/factor_dashboard")
    #far.plot_quantile_statistics_table()
    far.create_full_tear_sheet(demeaned=False, group_adjust=False, by_group=True, turnover_periods=None, avgretplot=(5, 15), std_bar=True)
'''
