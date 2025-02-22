"""
实现因子分析相关计算功能
"""

import numpy as np
import pandas as pd
from statsmodels.api import OLS, add_constant
from scipy import stats

import empyrical as ep

from .analysor import demean_forward_returns
from .utils import get_forward_returns_columns, rolling_apply


def factor_information_coefficient(
    factor_data, group_adjust=False, by_group=False, method=stats.spearmanr
):
    """
    计算因子值与N期未来收益之间的Spearman等级相关系数（IC）

    :param factor_data: 多重索引的 DataFrame，索引为日期（level 0）和资产（level 1），包含单一alpha因子值、未来收益、因子分位数/箱子信息（可选地包含资产所属的组）。
    :type factor_data: pd.DataFrame
    :param group_adjust: 是否在计算IC之前按组对未来收益进行去均值处理。
    :type group_adjust: bool
    :param by_group: 如果为True，则对每个组单独计算每个时期的IC。
    :type by_group: bool
    :return: 因子值与提供的未来收益之间的Spearman等级相关系数（IC）。
    :rtype: pd.DataFrame
    """

    def src_ic(group):
        f = group["factor"]
        _ic = group[get_forward_returns_columns(factor_data.columns)].apply(
            lambda x: method(x, f)[0]
        )
        return _ic

    factor_data = factor_data.copy()

    grouper = [factor_data.index.get_level_values("date")]

    if group_adjust:
        factor_data = demean_forward_returns(factor_data, grouper + ["group"])
    if by_group and "group" in factor_data.columns:
        grouper.append("group")

    with np.errstate(divide="ignore", invalid="ignore"):
        ic = factor_data.groupby(grouper).apply(src_ic)

    return ic


def mean_information_coefficient(
    factor_data,
    group_adjust=False,
    by_group=False,
    by_time=None,
    method=stats.spearmanr,
):
    """
    获取指定组的平均信息系数。
    解答以下问题：
    每个月的平均IC是多少？
    整个时间范围内每个组的平均IC是多少？
    每周每个组的平均IC是多少？

    :param factor_data: 多重索引的 DataFrame，索引为日期（level 0）和资产（level 1），包含单一alpha因子值、未来收益、因子分位数/箱子信息（可选地包含资产所属的组）。
    :type factor_data: pd.DataFrame
    :param group_adjust: 是否在计算IC之前按组对未来收益进行去均值处理。
    :type group_adjust: bool
    :param by_group: 如果为True，则对每个组计算平均IC。
    :type by_group: bool
    :param by_time: 计算平均IC时使用的时间窗口。
        参见 http://pandas.pydata.org/pandas-docs/stable/timeseries.html 以获取可用的选项。
    :type by_time: str, 可选
    :return: 因子值与提供的未来价格变化窗口之间的平均Spearman等级相关系数（IC）。
    :rtype: pd.DataFrame
    """
    ic = factor_information_coefficient(
        factor_data, group_adjust, by_group, method=method
    )

    grouper = []
    if by_time is not None:
        grouper.append(pd.Grouper(freq=by_time))
    if by_group  and "group" in factor_data.columns:
        grouper.append("group")

    if len(grouper) == 0:
        ic = ic.mean()

    else:
        ic = ic.reset_index().set_index("date").groupby(grouper).mean()

    return ic


def factor_weights(factor_data, demeaned=True, group_adjust=False, equal_weight=False):
    """
    计算基于因子值的资产权重，并将其除以绝对值之和（实现总杠杆为1）。正因子值会得到正权重，负因子值会得到负权重。

    :param factor_data: 多重索引的 DataFrame，索引为日期（level 0）和资产（level 1），包含单一alpha因子值、未来收益、因子分位数/箱子信息（可选地包含资产所属的组）。
    :type factor_data: pd.DataFrame
    :param demeaned: 是否对因子值进行去均值处理以构建一个多空组合。如果为True，则通过去均值因子值并除以其绝对值之和来计算权重（实现总杠杆为1）。正权重的总和将等于负权重的绝对值，适用于美元中性多空组合。
    :type demeaned: bool
    :param group_adjust: 是否在计算权重时进行按组中性调整。如果为True，则计算按组中性的权重：每个组的权重相同，并且如果启用了`demeaned`，则在组层面进行因子值的去均值处理。
    :type group_adjust: bool
    :param equal_weight: 是否使用等权重而不是因子权重。如果为True，则资产将被等权重分配，而不是根据因子值进行权重分配。如果`demeaned`为True，则因子领域将被分成两个等大小的组，顶部资产得到正权重，底部资产得到负权重。
    :type equal_weight: bool, 可选
    :return: 基于因子值的资产权重。
    :rtype: pd.Series
    """
    pass


def factor_returns(
    factor_data, demeaned=True, group_adjust=False, equal_weight=False, by_asset=False
):
    """
    计算基于因子值的多头组合在每个时期的收益。

    :param factor_data: 多重索引的 DataFrame，索引为日期（level 0）和资产（level 1），包含单一alpha因子值、未来收益、因子分位数/箱子信息（可选地包含资产所属的组）。
    :type factor_data: pd.DataFrame
    :param demeaned: 控制如何构建因子权重
        -- 详见 `performance.factor_weights` 函数的说明
    :type demeaned: bool
    :param group_adjust: 控制如何构建因子权重
        -- 详见 `performance.factor_weights` 函数的说明
    :type group_adjust: bool
    :param equal_weight: 控制如何构建因子权重
        -- 详见 `performance.factor_weights` 函数的说明
    :type equal_weight: bool, 可选
    :param by_asset: 如果为True，则分别报告每个资产的收益。
    :type by_asset: bool, 可选
    :return: 基于因子值的每个时期的组合收益。
    :rtype: pd.DataFrame
    """

    def to_weights(group, is_long_short):
        if is_long_short:
            demeaned_vals = group - group.mean()
            return demeaned_vals / demeaned_vals.abs().sum()
        else:
            return group / group.abs().sum()

    grouper = [factor_data.index.get_level_values("date")]
    if group_adjust:
        grouper.append("group")

    weights = factor_data.groupby(grouper)["factor"].apply(to_weights, demeaned)
    if weights.index.names[0] == weights.index.names[1]:
        weights = weights.droplevel(level=0)

    if group_adjust:
        weights = weights.groupby(level="date").apply(to_weights, False)
    if weights.index.names[0] == weights.index.names[1]:
        weights = weights.droplevel(level=0)

    weighted_returns = factor_data[
        get_forward_returns_columns(factor_data.columns)
    ].multiply(weights, axis=0)

    returns = weighted_returns.groupby(level="date").sum()

    return returns


def factor_alpha_beta(
    factor_data, returns=None, demeaned=True, group_adjust=False, equal_weight=False
):
    """
    计算因子的Alpha（超额收益）、Alpha t统计量（Alpha显著性）和Beta（市场暴露）。通过将每个时期因子领域的平均收益作为自变量，将基于因子值加权的组合的平均收益作为因变量来进行回归分析。

    :param factor_data: 多重索引的 DataFrame，索引为日期（level 0）和资产（level 1），包含单一alpha因子值、未来收益、因子分位数/箱子信息（可选地包含资产所属的组）。
    :type factor_data: pd.DataFrame
    :param returns: 可选的每个时期因子组合的收益。如果为None，则将使用`factor_returns`函数计算收益，并传递`demeaned`、`group_adjust`、`equal_weight`标志。
    :type returns: pd.DataFrame, 可选
    :param demeaned: 控制如何构建用于Alpha/Beta计算的因子收益
        -- 详见 `performance.factor_returns` 函数的说明
    :type demeaned: bool
    :param group_adjust: 控制如何构建用于Alpha/Beta计算的因子收益
        -- 详见 `performance.factor_returns` 函数的说明
    :type group_adjust: bool
    :param equal_weight: 控制如何构建用于Alpha/Beta计算的因子收益
        -- 详见 `performance.factor_returns` 函数的说明
    :type equal_weight: bool, 可选
    :return: 包含因子Alpha、Beta和Alpha t统计量（显著性）的列表。
    :rtype: pd.Series
    """
    returns = factor_returns(factor_data, demeaned, group_adjust)

    universe_ret = (
        factor_data.groupby(level="date")[
            get_forward_returns_columns(factor_data.columns)
        ]
        .mean()
        .loc[returns.index]
    )

    if isinstance(returns, pd.Series):
        returns.name = universe_ret.columns.values[0]
        returns = pd.DataFrame(returns)

    alpha_beta = pd.DataFrame()
    for period in returns.columns.values:
        x = universe_ret[period].values
        y = returns[period].values
        x = add_constant(x)
        period_int = int(period.replace("period_", ""))

        reg_fit = OLS(y, x).fit()
        alpha, beta = reg_fit.params

        alpha_beta.loc["Ann. alpha", period] = (1 + alpha) ** (250.0 / period_int) - 1
        alpha_beta.loc["beta", period] = beta

    return alpha_beta


def cumulative_returns(returns, period=1):
    """
    从简单的每日收益计算累计收益。

    :param returns: 包含每日因子收益的 pd.Series。
    :type returns: pd.Series
    :return: 从简单的每日收益计算的累计收益系列。
    :rtype: pd.Series
    """
    if period == 1:
        return ep.cum_returns(returns, starting_value=1)
    elif period < 0:
        raise ValueError("period need larget than zero")

    def split_portfolio(ret, period):
        return pd.DataFrame(np.diag(ret))

    sub_portfolios = returns.groupby(
        np.arange(len(returns.index)) // period, axis=0
    ).apply(split_portfolio, period)
    sub_portfolios.index = returns.index

    #
    # 将 N 期收益转换为 1 期收益, 方便计算累积收益
    #

    def rate_of_returns(ret, period):
        return ((np.nansum(ret) + 1) ** (1.0 / period)) - 1

    sub_portfolios = rolling_apply(
        sub_portfolios,
        window=period,
        func=rate_of_returns,
        min_periods=1,
        args=(period,),
    )
    sub_portfolios = sub_portfolios.add(1).cumprod()

    #
    # 求 N 个投资组合累积收益均值
    #
    return sub_portfolios.mean(axis=1)


def positions(weights, period, freq=None):
    """
    构建净头寸值时间序列，表示每个头寸的投资百分比。

    :param weights: 包含因子权重的 pd.Series，索引包含计算交易的时间戳，值对应于资产的权重。
        - 详见 `factor_weights` 函数的说明
    :type weights: pd.Series
    :param period: 资产持有期（1天、2分钟、3小时等）。可以是 Timedelta 对象或 `Timedelta` 构造函数接受的字符串格式（如 '1 days', '1D', '30m', '3h', '1D1h' 等）。
    :type period: pandas.Timedelta 或字符串
    :param freq: 用于指定特定交易日历的 pandas DateOffset 对象。如果未提供，将使用 `weights.index.freq`。
    :type freq: pandas DateOffset, 可选
    :return: 资产头寸系列，索引为日期时间，列为资产。
    :rtype: pd.DataFrame
    """
    pass


def mean_return_by_quantile(
    factor_data, by_date=False, by_group=False, demeaned=True, group_adjust=False
):
    """
    计算因子分位数在提供的未来收益列上的平均收益。

    :param factor_data: 多重索引的 DataFrame，索引为日期（level 0）和资产（level 1），包含单一alpha因子值、未来收益、因子分位数/箱子信息（可选地包含资产所属的组）。
    :type factor_data: pd.DataFrame
    :param by_date: 如果为True，则对每个日期分别计算分位数桶的收益。
    :type by_date: bool
    :param by_group: 如果为True，则对每个组分别计算分位数桶的收益。
    :type by_group: bool
    :param demeaned: 计算去均值后的平均收益（多空组合）。
    :type demeaned: bool
    :param group_adjust: 返回的去均值处理将发生在组层面。
    :type group_adjust: bool
    :return: 按指定因子分位数计算的平均期望收益和收益标准误差。
    :rtype: pd.DataFrame
    """
    if group_adjust:
        grouper = [factor_data.index.get_level_values("date")] + ["group"]
        factor_data = demean_forward_returns(factor_data, grouper)
    elif demeaned:
        factor_data = demean_forward_returns(factor_data)
    else:
        factor_data = factor_data.copy()

    grouper = ["factor_quantile"]
    if by_date:
        grouper.append(factor_data.index.get_level_values("date"))

    if by_group and "group" in factor_data.columns:
        grouper.append("group")

    # fr_cols = get_forward_returns_columns(factor_data.columns)
    # for col in fr_cols:
    #     factor_data[col] = factor_data[col] * factor_data["weights"]
    #
    # group_stats = factor_data.groupby(grouper)[fr_cols].agg(["mean", "std", "count"])
    # mean_ret = group_stats.T.xs("mean", level=1).T
    #
    # std_error_ret = group_stats.T.xs("std", level=1).T / np.sqrt(
    #     group_stats.T.xs("count", level=1).T
    # )

    mean_ret, std_error_ret = weighted_mean_return(factor_data, grouper=grouper)


    return mean_ret, std_error_ret

def weighted_mean_return(factor_data, grouper):
    """计算(年化)加权平均/标准差"""
    forward_returns_columns = get_forward_returns_columns(factor_data.columns)

    def agg(values, weights):
        count = len(values)
        average = np.average(values, weights=weights, axis=0)
        # Fast and numerically precise
        variance = np.average(
            (values - average)**2, weights=weights, axis=0
        ) * count / max((count - 1), 1)
        return pd.Series(
            [average, np.sqrt(variance), count], index=['mean', 'std', 'count']
        )

    group_stats = factor_data.groupby(grouper)[
        forward_returns_columns.append(pd.Index(['weights']))] \
        .apply(lambda x: x[forward_returns_columns].apply(
            agg, weights=x['weights'].fillna(0.0).values
        ))

    mean_ret = group_stats.xs('mean', level=-1)

    std_error_ret = group_stats.xs('std', level=-1) \
        / np.sqrt(group_stats.xs('count', level=-1))

    return mean_ret, std_error_ret


def compute_mean_returns_spread(mean_returns, upper_quant, lower_quant, std_err=None):
    """
    计算两个分位数的平均收益差异。可选地，计算该差异的标准误差。

    :param mean_returns: 含有不同分位数的平均周期收益的 DataFrame。索引为日期和分位数。
    :type mean_returns: pd.DataFrame
    :param upper_quant: 用于从中减去较低分位数平均收益的分位数。
    :type upper_quant: int
    :param lower_quant: 用于从较高分位数平均收益中减去的分位数。
    :type lower_quant: int
    :param std_err: 可选的，按分位数计算的周期性标准误差的 DataFrame。格式与 mean_returns 相同。
    :type std_err: pd.DataFrame, optional
    :return: 平均收益差异的 Series 和该差异的标准误差（如果提供了 std_err）。
    :rtype: (pd.Series, pd.Series or None)
    """
    mean_return_difference = mean_returns.xs(
        upper_quant, level="factor_quantile"
    ) - mean_returns.xs(lower_quant, level="factor_quantile")

    if std_err is None:
        joint_std_err = None
    else:
        std1 = std_err.xs(upper_quant, level="factor_quantile")
        std2 = std_err.xs(lower_quant, level="factor_quantile")
        joint_std_err = np.sqrt(std1**2 + std2**2)

    return mean_return_difference, joint_std_err


def quantile_turnover(quantile_factor, quantile, period=1):
    """
    计算在给定的时间段内，某个因子分位数中不再出现的资产比例。

    :param quantile_factor: 包含日期、资产和因子分位数的 DataFrame。
    :type quantile_factor: pd.Series
    :param quantile: 要进行换手率分析的分位数。
    :type quantile: int
    :param period: 可选的，计算换手率的时间天数。
    :type period: int, optional
    :return: 每个时间段内该分位数的换手率。
    :rtype: pd.Series
    """
    #quant_names = quantile_factor[quantile_factor.factor_quantile == quantile]
    quant_names = quantile_factor[quantile_factor == quantile]
    quant_name_sets = quant_names.groupby(level=["date"]).apply(
        lambda x: set(x.index.get_level_values("asset"))
    )
    new_names = (quant_name_sets - quant_name_sets.shift(period)).dropna()
    quant_turnover = new_names.apply(lambda x: len(x)) / quant_name_sets.apply(
        lambda x: len(x)
    )
    quant_turnover.name = quantile
    return quant_turnover


def factor_rank_autocorrelation(factor_data, period=1):
    """
    计算指定时间跨度内因子排名的自相关性。此指标用于衡量因子的换手率。

    :param factor_data: 一个 MultiIndex DataFrame，索引为日期（级别 0）和资产（级别 1），包含了单一 alpha 因子的值、每期的前向收益、因子值所属的分位数/区间，以及（可选的）资产所属的组。
    :type factor_data: pd.DataFrame
    :param period: 可选的，计算换手率的时间天数。
    :type period: int, optional
    :return: 因子值的滚动一期（由时间规则定义）自相关性。
    :rtype: pd.Series
    """
    grouper = [factor_data.index.get_level_values('date')]

    ranks = factor_data.groupby(grouper)['factor'].rank()

    asset_factor_rank = ranks.reset_index().pivot(index='date',
                                                  columns='asset',
                                                  values='factor')

    asset_shifted = asset_factor_rank.shift(period)

    autocorr = asset_factor_rank.corrwith(asset_shifted, axis=1)
    autocorr.name = period
    return autocorr


def common_start_returns(
    factor, returns, before, after, cumulative=False, mean_by_date=False, demean_by=None
):
    """
    从因子 DataFrame 中提取每个索引行的日期和资产对，并为每对构建一个从因子日期前的 'before' 天到后的 'after' 天的收益系列。所有这些收益系列对齐到相同的索引（从 -before 到 after），并作为一个 DataFrame 返回。

    :param factor: 包含日期和资产作为索引的 DataFrame，列无关。
    :type factor: pd.DataFrame
    :param returns: 宽格式的 Pandas DataFrame，日期作为索引，资产作为列。收益数据应涵盖因子分析时间段，加上 'before' 和 'after' 期的缓冲窗口。
    :type returns: pd.DataFrame
    :param before: 因子日期之前加载多少天的收益。
    :type before: int
    :param after: 因子日期之后加载多少天的收益。
    :type after: int
    :param cumulative: 可选的，是否将给定的收益视为累计收益。如果为 False，则假定收益为每日收益。
    :type cumulative: bool, optional
    :param mean_by_date: 可选的，如果为 True，则计算每个日期的平均收益，而不是为每个资产返回一个收益系列。
    :type mean_by_date: bool, optional
    :param demean_by: 可选的，包含日期和资产作为索引的 DataFrame，列无关。对每个日期，从 'demean_by' 索引中提取一个资产列表，用作计算去均值的平均收益（多头空头投资组合）的 Universe。
    :type demean_by: pd.DataFrame, optional
    :return: 对齐的收益 DataFrame，索引为 -before 到 after。
    :rtype: pd.DataFrame
    """
    pass

def common_start_returns(
    factor,
    prices,
    before,
    after,
    cumulative=False,
    mean_by_date=False,
    demean_by=None
):

    if cumulative:
        returns = prices
    else:
        returns = prices.pct_change(axis=0)

    all_returns = []

    for timestamp, df in factor.groupby(level='date'):

        equities = df.index.get_level_values('asset')

        try:
            day_zero_index = returns.index.get_loc(timestamp)
        except KeyError:
            continue

        starting_index = max(day_zero_index - before, 0)
        ending_index = min(day_zero_index + after + 1, len(returns.index))

        equities_slice = list(equities)
        if demean_by is not None:
            demean_equities = demean_by.loc[timestamp] \
                .index.get_level_values('asset')
            equities_slice |= set(demean_equities)

        series = returns.loc[returns.
                             index[starting_index:ending_index], equities_slice]
        series.index = range(
            starting_index - day_zero_index, ending_index - day_zero_index
        )

        if cumulative:
            series = (series / series.loc[0, :]) - 1

        if demean_by is not None:
            mean = series.loc[:, demean_equities].mean(axis=1)
            series = series.loc[:, equities]
            series = series.sub(mean, axis=0)

        if mean_by_date:
            series = series.mean(axis=1)

        all_returns.append(series)

    return pd.concat(all_returns, axis=1)

def average_cumulative_return_by_quantile(
    factor_data,
    returns,
    periods_before=10,
    periods_after=15,
    demeaned=True,
    group_adjust=False,
    by_group=False
):
    """
    绘制在因子分位数范围内的平均累计收益，时间区间从 periods_before 到 periods_after。

    :param factor_data: 一个 MultiIndex DataFrame，索引为日期（级别 0）和资产（级别 1），包含了单一 alpha 因子的值、每期的前向收益、因子值所属的分位数/区间，以及（可选的）资产所属的组。
    :type factor_data: pd.DataFrame
    :param returns: 宽格式的 Pandas DataFrame，日期作为索引，资产作为列。收益数据应涵盖因子分析时间段，加上 periods_before 和 periods_after 期的缓冲窗口。
    :type returns: pd.DataFrame
    :param periods_before: 可选的，因子之前绘制多少个时间段的收益。
    :type periods_before: int, optional
    :param periods_after: 可选的，因子之后绘制多少个时间段的收益。
    :type periods_after: int, optional
    :param demeaned: 可选的，是否计算去均值的平均收益（多头空头投资组合）。
    :type demeaned: bool, optional
    :param group_adjust: 是否在组层面上进行去均值处理（组中性投资组合）。
    :type group_adjust: bool
    :param by_group: 如果为 True，则为每个组单独计算累计收益。
    :type by_group: bool
    :return: 各分位数的累计收益及标准差的 DataFrame，索引为分位数（级别 0）和均值/标准差（级别 1），列的范围从 -periods_before 到 periods_after。
    :rtype: pd.DataFrame
    """
    def cumulative_return(q_fact, demean_by):
        return common_start_returns(
            q_fact, returns, periods_before, periods_after, True, True, demean_by
        )

    def average_cumulative_return(q_fact, demean_by):
        q_returns = cumulative_return(q_fact, demean_by)
        return pd.DataFrame(
            {
                'mean': q_returns.mean(axis=1),
                'std': q_returns.std(axis=1)
            }
        ).T

    if by_group and "group" in factor_data.columns:

        returns_bygroup = []

        for group, g_data in factor_data.groupby('group'):
            g_fq = g_data['factor_quantile']
            if group_adjust:
                demean_by = g_fq  # demeans at group level
            elif demeaned:
                demean_by = factor_data['factor_quantile']  # demean by all
            else:
                demean_by = None
            #
            # Align cumulative return from different dates to the same index
            # then compute mean and std
            #
            avgcumret = g_fq.groupby(g_fq).apply(
                average_cumulative_return, demean_by
            )
            avgcumret['group'] = group
            avgcumret.set_index('group', append=True, inplace=True)
            returns_bygroup.append(avgcumret)

        return pd.concat(returns_bygroup, axis=0)

    else:

        if group_adjust:
            all_returns = []
            for group, g_data in factor_data.groupby('group'):
                g_fq = g_data['factor_quantile']
                avgcumret = g_fq.groupby(g_fq).apply(cumulative_return, g_fq)
                all_returns.append(avgcumret)
            q_returns = pd.concat(all_returns, axis=1)
            q_returns = pd.DataFrame(
                {
                    'mean': q_returns.mean(axis=1),
                    'std': q_returns.std(axis=1)
                }
            )
            return q_returns.unstack(level=1).stack(level=0)
        elif demeaned:
            fq = factor_data['factor_quantile']
            return fq.groupby(fq).apply(average_cumulative_return, fq)
        else:
            fq = factor_data['factor_quantile']
            return fq.groupby(fq).apply(average_cumulative_return, None)

def cumulative_return_around_event(q_fact, demean_by):
    pass


def average_cumulative_return(q_fact, demean_by):
    """
    计算因子分位数的平均累计收益及标准差。

    :param q_fact: 因子分位数的 DataFrame。
    :type q_fact: pd.Series
    :param demean_by: 用于去均值的 DataFrame。如果为 None，则不进行去均值处理。
    :type demean_by: pd.DataFrame, optional
    :return: 平均累计收益和标准差的 DataFrame。
    :rtype: pd.DataFrame
    """
    pass


def factor_cumulative_returns(
    factor_data,
    period,
    long_short=True,
    group_neutral=False,
    equal_weight=False,
    quantiles=None,
    groups=None,
):
    """
    使用输入的因子模拟一个投资组合，并返回该投资组合的累计收益。

    :param factor_data: 一个 MultiIndex DataFrame，索引为日期（级别 0）和资产（级别 1），包含了单一 alpha 因子的值、每期的前向收益、因子值所属的分位数/区间，以及（可选的）资产所属的组。
    :type factor_data: pd.DataFrame
    :param period: 对应于 'factor_data' 列名的 'period' 收益，用于计算投资组合收益。
    :type period: str
    :param long_short: 可选的，如果为 True，则模拟一个美元中性的多头空头投资组合。
    :type long_short: bool, optional
    :param group_neutral: 可选的，如果为 True，则模拟一个组中性的投资组合。
    :type group_neutral: bool, optional
    :param equal_weight: 可选的，控制资产权重。
    :type equal_weight: bool, optional
    :param quantiles: 可选的，计算时仅使用特定的分位数。默认使用所有分位数。
    :type quantiles: sequence[int], optional
    :param groups: 可选的，计算时仅使用特定的组。默认使用所有组。
    :type groups: sequence[string], optional
    :return: 投资组合的累计收益系列。
    :rtype: pd.Series
    """
    pass


def factor_positions(
    factor_data,
    period,
    long_short=True,
    group_neutral=False,
    equal_weight=False,
    quantiles=None,
    groups=None,
):
    """
    使用输入的因子模拟一个投资组合，并返回各资产在总投资组合中的持仓比例。

    :param factor_data: 一个 MultiIndex DataFrame，索引为日期（级别 0）和资产（级别 1），包含了单一 alpha 因子的值、每期的前向收益、因子值所属的分位数/区间，以及（可选的）资产所属的组。
    :type factor_data: pd.DataFrame
    :param period: 对应于 'factor_data' 列名的 'period' 收益，用于计算投资组合收益。
    :type period: str
    :param long_short: 可选的，如果为 True，则模拟一个美元中性的多头空头投资组合。
    :type long_short: bool, optional
    :param group_neutral: 可选的，如果为 True，则模拟一个组中性的投资组合。
    :type group_neutral: bool, optional
    :param equal_weight: 可选的，控制资产权重。
    :type equal_weight: bool, optional
    :param quantiles: 可选的，计算时仅使用特定的分位数。默认使用所有分位数。
    :type quantiles: sequence[int], optional
    :param groups: 可选的，计算时仅使用特定的组。默认使用所有组。
    :type groups: sequence[string], optional
    :return: 各资产在投资组合中的持仓比例。
    :rtype: pd.DataFrame
    """
    pass


def create_pyfolio_input(
    factor_data,
    period,
    capital=None,
    long_short=True,
    group_neutral=False,
    equal_weight=False,
    quantiles=None,
    groups=None,
    benchmark_period="1D",
):
    """
    使用输入的因子模拟一个投资组合，并返回适合 Pyfolio 分析的投资组合绩效数据。

    :param factor_data: 一个 MultiIndex DataFrame，索引为日期（级别 0）和资产（级别 1），包含了单一 alpha 因子的值、每期的前向收益、因子值所属的分位数/区间，以及（可选的）资产所属的组。
    :type factor_data: pd.DataFrame
    :param period: 对应于 'factor_data' 列名的 'period' 收益，用于计算投资组合收益。
    :type period: str
    :param capital: 可选的，如果设置了该参数，则以美元金额计算持仓，而非百分比。
    :type capital: float, optional
    :param long_short: 可选的，如果为 True，则强制执行一个美元中性的多头空头投资组合。
    :type long_short: bool, optional
    :param group_neutral: 可选的，如果为 True，则模拟一个组中性的投资组合。
    :type group_neutral: bool, optional
    :param equal_weight: 可选的，控制资产的权重设置。
    :type equal_weight: bool, optional
    :param quantiles: 可选的，计算时仅使用特定的因子分位数。
    :type quantiles: sequence[int], optional
    :param groups: 可选的，计算时仅使用特定的资产组。
    :type groups: sequence[string], optional
    :param benchmark_period: 可选的，指定用于计算基准收益的 'factor_data' 列名。默认使用 '1D' 频率计算基准收益。
    :type benchmark_period: str, optional
    :return: 投资组合的每日收益、持仓比例以及基准收益。
    :rtype: tuple(pd.Series, pd.DataFrame, pd.Series)
    """
    pass


def factor_autocorrelation(factor_data, period=1, rank=True):
    """
    计算指定时间跨度内平均因子排名/因子值的自相关性.
    该指标对于衡量因子的换手率非常有用.
    如果每个因子值在一个周期内随机变化，我们预计自相关为 0.

    参数
    ----------
    factor_data : pd.DataFrame - MultiIndex
        一个 DataFrame, index 为日期 (level 0) 和资产(level 1) 的 MultiIndex,
        values 包括因子的值, 各期因子远期收益, 因子分位数,
        因子分组(可选), 因子权重(可选)
    period: int, optional
        对应的因子远期收益时间跨度
    Returns
    -------
    autocorr : pd.Series
        滞后一期的因子自相关性
    """

    grouper = [factor_data.index.get_level_values('date')]

    if rank:
        ranks = factor_data.groupby(grouper)[['factor']].rank()
    else:
        ranks = factor_data[['factor']]
    asset_factor_rank = ranks.reset_index().pivot(
        index='date', columns='asset', values='factor'
    )

    autocorr = asset_factor_rank.corrwith(
        asset_factor_rank.shift(period), axis=1
    )
    autocorr.name = period
    return autocorr
