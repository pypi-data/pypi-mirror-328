"""
@author: zhangluping_it
@time: 2024/9/2 19:09
@description: 因子计算/分析相关等算子
"""
import os
import traceback

import numpy as np
import pandas as pd

# TODO 目前采用引入swordfish的方式，后续发布采用python源码集成so库的方式
#import swordfish as sf
#import swordfish.function as sff
#from swordfish._swordfishcpp import Constant, Vector, Matrix, Table, Int
import deepquant.oplib  as sf
import deepquant.oplib.function as sff
from deepquant.oplib._swordfishcpp import Constant, Vector, Matrix, Table, Int

sf_path = os.path.dirname(sf.__file__)
sf.config.set_home(sf_path)
sf.config.set_log(os.path.join(sf_path, 'dolphindb.log'))

sf.init()
from .op_udf import *

# 是否转换计算结果到传入参数类型
conv_result_switch = True


class ConvertToNumpyError(Exception):
    pass


def sf_to_numpy(x: Constant):
    if isinstance(x, Vector):
        return x.to_numpy()
    elif isinstance(x, Matrix):
        return x.to_numpy()
    elif isinstance(x, Table):
        return x.to_pandas()
    else:
        message = "sf_to_numpy不支持传入数据类型L({})".format(type(x))
        raise ConvertToNumpyError(message)


def convert(param, result, fill_col_names = False):
    if not conv_result_switch:
        return result
    if isinstance(param, pd.DataFrame):
        if isinstance(result, Table):
            df = result.to_pandas()
            df.index = param.index
            if param.columns.name is not None:
                df.columns.name = param.columns.name
            return df
        elif isinstance(result, Matrix):
            df = pd.DataFrame(sf_to_numpy(result))
            df.index = param.index
            if fill_col_names and len(df.columns) == len(param.columns):
                df.columns = param.columns
            if param.columns.name is not None:
                df.columns.name = param.columns.name
            return df
        else:
            return pd.DataFrame(sf_to_numpy(result))
    elif isinstance(param, np.ndarray):
        return sf_to_numpy(result)
    elif isinstance(param, pd.Series):
        si = pd.Series(sf_to_numpy(result))
        si.index = param.index
        return si
    else:
        return result


def ADD_CONST(x, c):
    """
    :param x: 标量/向量/矩阵，例如 [1,2,3]
    :param c: 标量，例如 3
    :return: x + c, 上例中返回 vector[4,5,6]
    """
    return convert(x, sff.add(x, c))


def MUL_CONST(x, c):
    """
    :param x: 标量/向量/矩阵，例如 [1,2,3]
    :param c: 标量，例如 3
    :return: x * c, 上例中返回 vector[3,6,9]
    """
    return convert(x, sff.mul(x, c))


def ADD(x, y):
    """
    :param x: 标量/向量/矩阵，例如 [1,2,3]
    :param y: 标量或者和x长度相同的向量或矩阵，例如 [4,5,6]
    :return: x+y, 上例中返回 vector[5,6,7]
    """
    return convert(x, sff.add(x, y))


def SUB(x, y):
    """
    :param x: 标量/向量/矩阵，例如 [1,2,3]
    :param y: 标量或者和x长度相同的向量或矩阵，例如 [3,2,1]
    :return: x-y, 上例中返回 vector[-2,0,2]
    """
    return convert(x, sff.sub(x, y))


def MUL(x, y):
    """
    :param x: 标量/向量/矩阵，例如 [1,2,3]
    :param y: 标量或者和x长度相同的向量或矩阵，例如 [2,3,4]
    :return: x*y, 上例中返回 vector[2,6,12]
    """
    return convert(x, sff.mul(x, y))


def DIV(x, y):
    """
    :param x: 标量/向量/矩阵，例如 [9,8,7.0]
    :param y: 标量或者和x长度相同的向量或矩阵，例如 [3,2,4.0]
    :return: x/y, 上例中返回 vector[3., 4., 1.75]
    """
    # np.divide
    return convert(x, sff.div(x, y))


def LOG(x):
    return convert(x, sff.log(x))


def EXP(x):
    return convert(x, sff.exp(x))


def SQRT(x):
    return convert(x, sff.sqrt(x))


def SQUARE(x):
    return convert(x, sff.square(x))


def SIN(x):
    return convert(x, sff.sin(x))


def COS(x):
    return convert(x, sff.cos(x))


def NEG(x):
    # return np.negative(x)
    return convert(x, sff.neg(x))


def RECIPROCAL(x):
    """
    x的倒数， 1/x
    """
    return convert(x, sff.reciprocal(x))


def SIGN(x):
    """
    x的正负性
    :return: 正数返回1; 负数返回-1;
    """
    return convert(x, np.sign(x))


def ABS(x):
    """
    x的绝对值
    :return: 绝对值
    """
    return convert(x, sff.abs(x))


def SIGMOID(x):
    """
    :return: y= 1\ (1+exp(-1*x))
    """
    return convert(x, udf_SIGMOID(x))


def HARDSIGMOID(x):
    """
    :return: clip((x+3) \ 6, 0, 1)
    """
    return convert(x, udf_HARDSIGMOID(x))


def LEAKYRELU(x, a):
    """
    :return: max(x, 0) + a * min(x, 0)
    """
    return convert(x, udf_LEAKYRELU(x, a))


def GELU(x):
    """
    :return: x * cdfNormal(0, 1, x)
    """
    return convert(x, udf_GELU(x))


###################################### Panel operator #######################################

def XS_CUTQUARTILE(x, a):
    """
    采用四分位数法拉回截面上的离群值
    """
    return convert(x, udf_xs_cutquartile(x, a))


def XS_CUTZSCORE(x, a):
    """
    采用zscore法拉回截面上的离群值
    """
    return convert(x, udf_xs_cutzscore(x, a))


def RANK_PCT(x, ascending=True):
    """
    截面上分位数
    """
    if isinstance(x, pd.DataFrame):
        sf_x = sf.matrix(x.to_numpy())
        return convert(x, udf_rank_pct(sf_x, ascending), fill_col_names=True)
    else:
        return convert(x, udf_rank_pct(x, ascending))


def XS_REGRES(x, y, intercept=True):
    """
    截面上Y对X开展一元线性回归的残差
    """
    return convert(x, udf_xs_regres(x, y, intercept))


def xs_sortreverse(x, n, mode):
    """
    X截面前/后n名对应的X乘以-1
    """
    return convert(x, udf_xs_sortreverse(x, n, mode))


def xs_zscorereverse(x, n, mode):
    """
    X截面z值大于/小于阈值对应的X乘以-1
    """
    return convert(x, udf_xs_zscorereverse(x, n, mode))


def xs_grouping_sortreverse(x, y, n, mode):
    """
    Y截面前/后n名对应的X乘以-1
    """
    return convert(x, udf_xs_grouping_sortreverse(x, y, n, mode))


def xs_grouping_zscorereverse(x, y, a, mode):
    """
    Y截面z值大于/小于阈值对应的X乘以-1
    """
    return convert(x, udf_xs_grouping_zscorereverse(x, y, a, mode))


###################################### TimeSeries operator #######################################
def TS_CUTQUARTILE(x, iqr_scale):
    return convert(x, udf_ts_cutquantile(x, iqr_scale))


def TS_CUTZSCORE(x, std_scale):
    return convert(x, udf_ts_cutzscore(x, std_scale))


def TS_DELAY(x, move):
    """
    对于 X 中的每一个元素，计算 Xi-Xi-n，NULL 值不参与计算。
        若 X 是向量，返回一个包含 X 中两个元素之差的向量。
        若 X 是矩阵，在每列内进行上述计算，返回一个与 X 维度相同的矩阵。
        若 X 是表，在每列内进行上述计算，返回一个与 X 行数与列数都相同的表。

    :param x: 向量、矩阵或表。
    :param n: 可选参数，一个整数，用于减数相较于被减数的索引偏移。默认是1。
    :return: real
    """
    return convert(x, sff.move(x, move))


def TS_DELTAS(x, n):
    """
    对于 X 中的每一个元素，计算 Xi-Xi-n，NULL 值不参与计算。
        若 X 是向量，返回一个包含 X 中两个元素之差的向量。
        若 X 是矩阵，在每列内进行上述计算，返回一个与 X 维度相同的矩阵。
        若 X 是表，在每列内进行上述计算，返回一个与 X 行数与列数都相同的表。

    :param x: 向量、矩阵或表。
    :param n: n 可选参数，一个整数，用于减数相较于被减数的索引偏移。默认是1。
    :return: real
    """
    return convert(x, sff.deltas(x, Int(n)))


def TS_PCTCHANGE(x, n):
    """
    计算两个元素之间的值变化比例。即对于 X 中的每一个元素，计算 (Xi / Xi-n) - 1。

    :param x: 向量、矩阵或表。
    :param n: 可选参数，整型，用于指定计算 X 中两个元素值变化百分比时的元素间隔数，默认值为 1。
    :return: real
    """
    return convert(x, sff.percentChange(x, Int(n)))


def TS_ROLLRANK(x, d, ascending=True):
    """
    滚动d日的分位数

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :param ascending: 布尔值，表示是否按升序排序。默认值是 true。
    :return: real
    """
    return convert(x, udf_ts_rollrank(x, Int(d), ascending))


def TS_ROLLZSCORE(x, d):
    """
    滚动d日的Z值

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, udf_ts_rollzscore(x, d))


def TS_ROLLCORR(x, y, window):
    """
    x和y 滚动 d 日的相关系数

    :param x: 向量、矩阵或表。
    :param y: 向量、矩阵或表。
    :param window: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, sff.mcorr(x, y, window))


def TS_RANKCORR(x, y, window):
    """
    x和y滚动d日的秩(Spearman)相关系数

    :param x: 向量、矩阵或表。
    :param y: 向量、矩阵或表。
    :param window: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, udf_ts_rankcorr(x, y, window))


def TS_COVARIANCE(x, y, window):
    """
    x和y滚动d日的协方差

    :param x: 向量、矩阵或表。
    :param y: 向量、矩阵或表。
    :param window: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, sff.mcovar(x, y, window))


def TS_MAX(x, d):
    """
    滚动d日最大值

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, sff.mmax(x, d))


def TS_MIN(x, d):
    """
    滚动d日最小值

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, sff.mmin(x, d))


def TS_SUM(x, d):
    """
    滚动d日之和

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, sff.msum(x, d))


def TS_MEAN(x, d):
    """
    滚动d日均值

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, sff.mavg(x, d))


def TS_MEDIAN(x, d):
    """
    滚动d日中位数

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """

    return convert(x, sff.mmed(x, d))


def TS_VAR(x, d):
    """
    滚动d日方差

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, sff.mvar(x, d))


def TS_STDDEV(x, d):
    """
    滚动d日标准差

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, sff.mstdp(x, d))


def TS_AVGDEV(x, d):
    """
    滚动d日平均偏差	

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, udf_ts_avgdev(x, d))


def TS_KURT(x, d):
    """
    滚动d日峰度		

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    udf_kurt = sff.partial(sff.mkurtosis, sff.VOID, sff.VOID, False)
    return convert(x, udf_kurt(x, d))


def TS_SKEW(x, d):
    """
    滚动d日偏度			

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    udf_mskew = sff.partial(sff.mskew, sff.VOID, sff.VOID, False)
    return convert(x, udf_mskew(x, d))


def TS_ARGMAX(x, d):
    """
    滚动d日最大值的索引除以d

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, udf_ts_argmax(x, d))


def TS_ARGMIN(x, d):
    """
    滚动d日最大值的索引除以d

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, udf_ts_argmin(x, d))


def TS_DECAY_LINEAR_MEAN(x, d):
    """
    滚动d日按时间索引作为权重求均值
    TODO udf ?

    :param x: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, udf_ts_decay_linear_mean(x, d))


def TS_ROOLWEIGHTED_MEAN(x, y, d):
    """
    滚动d日中，以归一化的y为权重，求x均值

    :param x: 向量、矩阵或表。
    :param y: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, udf_ts_rollweighted_mean(x, y, d))


def TS_REGBETA(x, y, d):
    """
    滚动d日中，y对x开展一元线性回归的斜率

    :param x: 向量、矩阵或表。
    :param y: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, udf_ts_regbeta(x, y, d))


def TS_REGALPHA(x, y, d):
    """
    滚动d日中，y对x开展一元钱性回归的截距

    :param x: 向量、矩阵或表。
    :param y: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, udf_ts_regalpha(x, y, d))


def TS_REGRES(x, y, d):
    """
    滚动d日中，y对x开展一元线性回归的最近一期残差

    :param x: 向量、矩阵或表。
    :param y: 向量、矩阵或表。
    :param d: 表示滑动窗口的长度。大于等于 2 的正整型。
    :return: real
    """
    return convert(x, udf_ts_regres(x, y, d))


###################################### TA operator #######################################
def MA(x, timeperiod=30, matype=0):
    """
    Moving average (Overlap Studies)

    :param x: real
    :param timeperiod: 30
    :param matype: 0 (Simple Moving Average)
    :return: real
    """
    return convert(x, sff.ma(x, timeperiod, matype))


def EMA(x, timeperiod=30, warmup=False):
    """
    Exponential Moving Average (Overlap Studies)

    :param x: real
    :param timeperiod: 30
    :param matype: 0 (Simple Moving Average)
    :return: real
    """
    return convert(x, sff.ema(x, timeperiod, warmup))


def WMA(x, timeperiod=30):
    """
    Weighted Moving Average (Overlap Studies)

    :param x: real
    :param timeperiod: 30
    :return: real
    """
    return convert(x, sff.wma(x, timeperiod))


def SMA(x, timeperiod=30):
    """
    Simple Moving Average (Overlap Studies)

    :param x: real
    :param timeperiod: 30
    :return: real
    """
    return convert(x, sff.sma(x, timeperiod))


def DEMA(x, timeperiod=30):
    """
    Double Exponential Moving Average (Overlap Studies)

    :param x: real
    :param timeperiod: 30
    :return: real
    """
    return convert(x, sff.dema(x, timeperiod))


def KAMA(x, timeperiod=30):
    """
    Double Exponential Moving Average (Overlap Studies)

    :param x: x
    :param timeperiod: 30
    :return: real
    """
    return convert(x, sff.kama(x, timeperiod))


def MMAX(x, timeperiod=30):
    """
    Highest value over a specified period (Math Operators)

    :param x: 标量/向量/矩阵
    :param timeperiod: 30,
    :return: real
    """
    return convert(x, sff.mmax(x, timeperiod))


def MIDPOINT(x, timeperiod=14):
    """
    MidPoint over period (Overlap Studies)

    :param x: 标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(x, udf_MIDPOINT(x, timeperiod))


def MIDPRICE(high, low, timeperiod=14):
    """
    Midpoint Price over period

    :param high: 最高价，标量/向量/矩阵
    :param low: 最低价，标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(high, udf_MIDPRICE(high, low, timeperiod))


def AROONOSC(high, low, timeperiod=14):
    """
    Aroon Oscillator (Momentum Indicators)

    :param high: 最高价，标量/向量/矩阵
    :param low: 最低价，标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(high, udf_AROONOSC(high, low, timeperiod))


def WILLR(high, low, close, timeperiod=14):
    """
    Williams' %R (Momentum Indicators)

    :param high: 最高价，标量/向量/矩阵
    :param low: 最低价，标量/向量/矩阵
    :param close: 收盘价，标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(close, udf_WILLR(high, low, close, timeperiod))


def CCI(high, low, close, timeperiod=14):
    """
    Commodity Channel Index (Momentum Indicators)

    :param high: 最高价，标量/向量/矩阵
    :param low: 最低价，标量/向量/矩阵
    :param close: 收盘价，标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(close, udf_CCI(high, low, close, timeperiod))


def ADX(high, low, close, timeperiod=14):
    """
    Average Directional Movement Index (Momentum Indicators)

    :param high: 最高价，标量/向量/矩阵
    :param low: 最低价，标量/向量/矩阵
    :param close: 收盘价，标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(close, udf_ADX(high, low, close, timeperiod))


def MFI(high, low, close, volume, timeperiod=14):
    """
    Money Flow Index (Momentum Indicators)

    :param high: 最高价，标量/向量/矩阵
    :param low: 最低价，标量/向量/矩阵
    :param close: 收盘价，标量/向量/矩阵
    :param volume: 成交量，标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(close, udf_MFI(high, low, close, volume, timeperiod))


def NATR(high, low, close, timeperiod=14):
    """
    Normalized Average True Range (Volatility Indicators)

    :param high: 最高价，标量/向量/矩阵
    :param low: 最低价，标量/向量/矩阵
    :param close: 收盘价，标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(close, udf_NATR(high, low, close, timeperiod))


def BETA(x, y, timeperiod=5):
    """
    Beta (Statistic Functions)

    :param x: 标量/向量/矩阵
    :param y: 标量/向量/矩阵
    :param timeperiod: 5
    :return: real
    """
    return convert(x, udf_BETA(x, y, timeperiod))


def LINEARREG_ANGLE(x, timeperiod=14):
    """
    Linear Regression Angle (Statistic Functions)

    :param x: 标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(x, udf_LINEARREG_ANGLE(x, timeperiod))


def LINEARREG_INTERCEPT(x, timeperiod=14):
    """
    Linear Regression Intercept (Statistic Functions)

    :param x: 标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(x, udf_LINEARREG_INTERCEPT(x, timeperiod))


def LINEARREG_SLOPE(x, timeperiod=14):
    """
    Linear Regression Slope (Statistic Functions)

    :param x: 标量/向量/矩阵
    :param timeperiod: 14
    :return: real
    """
    return convert(x, udf_LINEARREG_SLOPE(x, timeperiod))


###################################### time cut operator #######################################
def TS_ASCSORTCUT(seqa, window, n, mode):
    """
    滚动window日中，将seqa最小的n天切割出来

    :param seqa: 向量/矩阵/表
    :param window:  表示滑动窗口的长度。10，15...,60。
    :param n: 1,2,...,10
    :param mode: 1-切割部分求seqa之和，2-全序列seqa之和减去切割部分的seqa之和，3-切割部分seqa乘以-1后再求全序列seqa之和
    :return:
    """
    return convert(seqa, udf_ts_ascsortcut(seqa, window, n, mode))


def TS_DECSORTCUT(seqa, window, n, mode):
    """
    滚动window日中，将seqa最大的n天切割出来

    :param seqa: 向量/矩阵/表
    :param window: 表示滑动窗口的长度。10，15...,60。
    :param n: 1,2,...,10
    :param mode: 1-切割部分求seqa之和，2-全序列seqa之和减去切割部分的seqa之和，3-切割部分seqa乘以-1后再求全序列seqa之和
    :return:
    """
    return convert(seqa, udf_ts_decsortcut(seqa, window, n, mode))


def TS_ASCZSORTCUT(seqa, window, a, mode):
    """
    滚动window日中，将seqa的z值小于-a的时间切割出来；若不存在，则切出seqa最小的1天

    :param seqa: 向量/矩阵/表
    :param window: 表示滑动窗口的长度。10，15...,60。
    :param a: 1.5,2.0,2.5,3.0
    :param mode: 1-切割部分求seqa之和，2-全序列seqa之和减去切割部分的seqa之和，3-切割部分seqa乘以-1后再求全序列seqa之和
    :return:
    """
    return convert(seqa, udf_ts_asczscorecut(seqa, window, a, mode))


def TS_DECZSORTCUT(seqa, window, a, mode):
    """
    滚动window日中，将seqa的z值大于a的时间切割出来；若不存在，则切出seqa最大的1天

    :param seqa: 向量/矩阵/表
    :param window: 表示滑动窗口的长度。10，15...,60。
    :param a: 1.5,2.0,2.5,3.0
    :param mode: 1-切割部分求seqa之和，2-全序列seqa之和减去切割部分的seqa之和，3-切割部分seqa乘以-1后再求全序列seqa之和
    :return:
    """
    return convert(seqa, udf_ts_deczscorecut(seqa, window, a, mode))


def TS_GROUPING_ASCSORTCUT(seqa, seqb, window, n, mode):
    """
    滚动window日中，将seqb最小的n天切割出来

    :param seqa: 向量/矩阵/表
    :param seqb: 向量/矩阵/表
    :param window: 表示滑动窗口的长度。10，15...,60。
    :param n: 1,2,...,10
    :param mode: 1-切割部分求seqa之和，2-全序列seqa之和减去切割部分的seqa之和，3-切割部分seqa乘以-1后再求全序列seqa之和
    :return:
    """
    return convert(seqa, udf_ts_grouping_ascsortcut(seqa, seqb, window, n, mode))


def TS_GROUPING_DECSORTCUT(seqa, seqb, window, n, mode):
    """
    滚动window日中，将seqb最大的n天切割出来

    :param seqa: 向量/矩阵/表
    :param seqb: 向量/矩阵/表
    :param window: 表示滑动窗口的长度。10，15...,60。
    :param n: 1,2,...,10
    :param mode: 1-切割部分求seqa之和，2-全序列seqa之和减去切割部分的seqa之和，3-切割部分seqa乘以-1后再求全序列seqa之和
    :return:
    """
    return convert(seqa, udf_ts_grouping_decsortcut(seqa, seqb, window, n, mode))


def TS_GROUPING_ASCZSORTCUT(seqa, seqb, window, a, mode):
    """
    滚动window日中，将seqb的z值小于-a的时间切割出来；若不存在，则切割出seqb最小的1天

    :param seqa: 向量/矩阵/表
    :param seqb: 向量/矩阵/表
    :param window: 表示滑动窗口的长度。10，15...,60。
    :param a: 1.5,2.0,2.5,3.0
    :param mode: 1-切割部分求seqa之和，2-全序列seqa之和减去切割部分的seqa之和，3-切割部分seqa乘以-1后再求全序列seqa之和
    :return:
    """
    return convert(seqa, udf_ts_grouping_asczscorecut(seqa, seqb, window, a, mode))


def TS_GROUPING_DECZSORTCUT(seqa, seqb, window, a, mode):
    """
    滚动window日中，将seqb的z值大于a的时间切割出来；若不存在，则切割出seqb最大的1天

    :param seqa: 向量/矩阵/表
    :param seqb: 向量/矩阵/表
    :param window: 表示滑动窗口的长度。10，15...,60。
    :param a: 1.5,2.0,2.5,3.0
    :param mode: 1-切割部分求seqa之和，2-全序列seqa之和减去切割部分的seqa之和，3-切割部分seqa乘以-1后再求全序列seqa之和
    :return:
    """
    return convert(seqa, udf_ts_grouping_deczscorecut(seqa, seqb, window, a, mode))


###################################### package operator #######################################

def EWMA(x,
         com=None, span=None, half_life=None, alpha=None,
         min_periods=0, adjust=True, ignore_na=False):
    """
    返回 x 的指数加权移动平均值。该函数必须指定 com, span, halfLife, alpha 四个参数中的一个。
    """
    _sff_result = None
    if com is not None:
        _sff_result = sff.ewmMean(X=x,
                                  com=com,
                                  minPeriods=min_periods, adjust=adjust, ignoreNA=ignore_na)
    elif span is not None:
        _sff_result = sff.ewmMean(X=x,
                                  span=span,
                                  minPeriods=min_periods, adjust=adjust, ignoreNA=ignore_na)
    elif half_life is not None:
        _sff_result = sff.ewmMean(X=x,
                                  halfLife=half_life,
                                  minPeriods=min_periods, adjust=adjust, ignoreNA=ignore_na)
    elif alpha is not None:
        _sff_result = sff.ewmMean(X=x,
                                  alpha=alpha,
                                  minPeriods=min_periods, adjust=adjust, ignoreNA=ignore_na)
    else:
        _sff_result = sff.ewmMean(X=x,
                                  minPeriods=min_periods, adjust=adjust, ignoreNA=ignore_na)
    return convert(x, _sff_result)


def ATR(high, low, close, d):
    return convert(close, udf_ATR(high, low, close, d))


def MACD(x, fastperiod=12, slowperiod=26, signalperiod=9):
    """
    Moving Average Convergence/Divergence (Momentum Indicators)
    
    :param x:
    :type x: np.ndarray
    :param fastperiod: 12
    :param slowperiod: 26
    :param signalperiod: 9
    :return:
            macd:  \n
            macdsignal:  \n
            macdhist:
    :rtype: tuple
    """

    macd, macdsignal, macdhist = udf_MACD(x, fastperiod, slowperiod, signalperiod)
    return convert(x, macd), convert(x, macdsignal), convert(x, macdhist)


if __name__ == '__main__':
    try:
        print('ADD_CONST', ADD_CONST([1, 2, 3], 3))
        print('MUL_CONST', MUL_CONST([1, 2, 3], 3))
        print('ADD', ADD([1, 2, 3], [4, 5, 6]))
        print('SUB', SUB([1, 2, 3], [3, 2, 1]))
        print('MUL', MUL([1, 2, 3], [2, 3, 4]))
        print('DIV', DIV([9, 5, 7.0], [3, 2, 4.0]))
        print('LOG', LOG([3.0]))
        print('EXP', EXP([3.0]))
        print('SQRT', SQRT([3.0]))
        print('SQUARE', SQUARE([3.0]))
        print('SIN', SIN([3.0]))
        print('COS', COS([3.0]))
        print('NEG', NEG([3.0]))
        print('RECIPROCAL', RECIPROCAL([3.0]))
        print('SIGN', SIGN([3.0, -2]))
        print('ABS', ABS([3.0, -2]))
        print('SIGMOID', SIGMOID([3.0, -2]))
        print('HARDSIGMOID', HARDSIGMOID([3.0, -2]))
        print('LEAKYRELU', LEAKYRELU([3.0, -2], 3))
        print('GELU', GELU([3.0, -2]))
    except Exception as e:
        traceback.print_exc()
    print('FINISH')
