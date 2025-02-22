import pandas as pd
import numpy as np

from .utils import get_forward_returns_columns

class MaxLossExceededError(Exception):
    pass

def get_clean_factor_and_forward_returns(
    factor,
    prices,
    groupby=None,
    weights=None,
    binning_by_group=False,
    quantiles=5,
    bins=None,
    periods=(1, 5, 10),
    max_loss=0.35,
    zero_aware=False,
):
    """
    将因子数据, 价格数据, 分组映射和权重映射格式化为
    由包含时间和资产的 MultiIndex 作为索引的 DataFrame

    :param factor:
    :type pd.DataFrame: index(level 0)为日期, index(level 1)为资产code, value为因子值、因子前向收益、因子分位数
    :param price: 资产的价格数据，如收盘价close, prices中包含factor中对应的时间和前向period后的数据
    :type pd.DataFrame: index为日期, columns为资产code
    :param groupby: 为每个资产每天的分组，或资产-分组映射的字典, 如果传递了dict，则假定分组映射在整个时间段内保持不变
    :type pd.Series: MultiIndex or dict, index 为日期和资产的 Series
    :param weights: 为每个资产每天的权重，或资产-权重映射的字典, 如果传递了dict，则假定权重映射在整个时间段内保持不变
    :type pd.Series: index 为日期和资产的 Series
    :param binning_by_group: 如果为 True, 则对每个组分别计算分位数
    :type bool:
    :param quantiles: 因子分组中按照因子数值大小分组的分组数
    :type int or list[float]: 分为quantiles个组, 或者指定分位数序列(可以不是均匀分组)
    :param bins: 等长度分组的分组数，quantiles和bins只有一个, 优先quantiles
    :type int or list[float]:
    :param periods: periods(按日)后的时间间隔
    :type tuple:
    :param max_loss: 允许的丢弃因子数据的最大百分比 (0.00 到 1.00)
    :type float:
    :param zero_aware: 如果为True，则分别为正负因子值计算分位数
    :type bool:
    :return : merged_data   values 包括因子的值, 各期因子远期收益, 因子分位数, 因子分组(可选), 因子权重(可选)
    :rtype : pd.DataFrame index(level 0)为日期, index(level 1)为资产code
    """

    forward_returns = compute_forward_returns(factor, prices, periods)

    factor_data = get_clean_factor(
        factor,
        forward_returns,
        groupby=groupby,
        weights=weights,
        quantiles=quantiles,
        bins=bins,
        binning_by_group=binning_by_group,
        max_loss=max_loss,
        zero_aware=zero_aware,
    )

    return factor_data


def get_clean_factor(
    factor,
    forward_returns,
    groupby=None,
    weights=None,
    binning_by_group=False,
    quantiles=5,
    bins=None,
    max_loss=0.35,
    zero_aware=False,
):
    """
    因子值, 因子前向收益, 因子分组(groupby), 因子权重数据
    格式化为以时间和资产的 MultiIndex 作为索引的 DataFrame.

    -------
    merged_data : pd.DataFrame - MultiIndex
        一个 DataFrame, index 为日期 (level 0) 和资产(level 1) 的 MultiIndex,
        values 包括因子的值, 各期因子远期收益, 因子分位数,
        因子分组(可选), 因子权重(可选)
        - 各期因子远期收益的列名满足 'period_1', 'period_5' 的格式
    """

    initial_amount = float(len(factor.index))

    factor_copy = factor.copy()
    factor_copy.index = factor_copy.index.rename(["date", "asset"])

    merged_data = forward_returns.copy()
    merged_data["factor"] = factor_copy

    if groupby is not None:
        if isinstance(groupby, dict):
            diff = set(factor_copy.index.get_level_values("asset")) - set(
                groupby.keys()
            )
            if len(diff) > 0:
                raise KeyError("Assets {} not in group mapping".format(list(diff)))

            ss = pd.Series(groupby)
            groupby = pd.Series(
                index=factor_copy.index,
                data=ss[factor_copy.index.get_level_values("asset")].values,
            )
        elif isinstance(groupby, pd.DataFrame):
            groupby = groupby.stack()
        merged_data["group"] = groupby

    if weights is not None:
        if isinstance(weights, dict):
            diff = set(factor_copy.index.get_level_values("asset")) - set(
                weights.keys()
            )
            if len(diff) > 0:
                raise KeyError("Assets {} not in weights mapping".format(list(diff)))

            ww = pd.Series(weights)
            weights = pd.Series(
                index=factor_copy.index,
                data=ww[factor_copy.index.get_level_values("asset")].values,
            )
        elif isinstance(weights, pd.DataFrame):
            weights = weights.stack()
        merged_data["weights"] = weights

    merged_data = merged_data.dropna()

    quantile_data = quantize_factor(
        merged_data, quantiles, bins, binning_by_group, True, zero_aware
    )

    merged_data["factor_quantile"] = quantile_data
    merged_data = merged_data.dropna()
    merged_data["factor_quantile"] = merged_data["factor_quantile"].astype(int)

    if "weights" in merged_data.columns:
        merged_data["weights"] = (
            merged_data.set_index("factor_quantile", append=True)
            .groupby(level=["date", "factor_quantile"])["weights"]
            .apply(lambda s: s.divide(s.sum()))
            .reset_index("factor_quantile", drop=True)
        )

    binning_amount = float(len(merged_data.index))

    tot_loss = (initial_amount - binning_amount) / initial_amount

    no_raise = True if max_loss == 0 else False
    if tot_loss > max_loss and not no_raise:
        message = "max_loss (%.1f%%) 超过 %.1f%%" % (tot_loss * 100, max_loss * 100)
        raise MaxLossExceededError(message)

    return merged_data


def quantize_factor(
    factor_data,
    quantiles=5,
    bins=None,
    by_group=False,
    no_raise=False,
    zero_aware=False,
):
    """
    计算每期因子分位数

    :param factor_data:
    :type pd.DataFrame: index(level 0)为日期, index(level 1)为资产code, value为因子值、因子前向收益、因子分位数
    :param quantiles: 因子分组中按照因子数值大小分组的分组数
    :type int or list[float]: 分为quantiles个组, 或者指定分位数序列(可以不是均匀分组)
    :param bins: 等长度分组的分组数，quantiles和bins只有一个, 优先quantiles
    :type int or list[float]:
    :param by_group: 按照 group 分别计算分位数
    :type bool:
    :param no_raise: 如果为 True，则不抛出任何异常，并且将抛出异常的值设置为 np.NaN
    :type bool:
    :param zero_aware: 如果为True，则分别为正负因子值计算分位数
    :type bool:
    :return factor_quantile: index(level 0)为日期, index(level 1)为资产code
    :rtype : pd.DataFrame
    """
    if not (
        (quantiles is not None and bins is None)
        or (quantiles is None and bins is not None)
    ):
        raise ValueError("quantiles 和 bins 至少要输入一个")

    if zero_aware and not (isinstance(quantiles, int) or isinstance(bins, int)):
        msg = "只有 quantiles 或 bins 为 int 类型时， 'zero_aware' 才能为 True"
        raise ValueError(msg)

    def quantile_calc(x, _quantiles, _bins, _zero_aware, _no_raise):
        try:
            if _quantiles is not None and _bins is None and not _zero_aware:
                return pd.qcut(x, _quantiles, labels=False) + 1
            elif _quantiles is not None and _bins is None and _zero_aware:
                pos_quantiles = (
                    pd.qcut(x[x >= 0], _quantiles // 2, labels=False)
                    + _quantiles // 2
                    + 1
                )
                neg_quantiles = pd.qcut(x[x < 0], _quantiles // 2, labels=False) + 1
                return pd.concat([pos_quantiles, neg_quantiles]).sort_index()
            elif _bins is not None and _quantiles is None and not _zero_aware:
                return pd.cut(x, _bins, labels=False) + 1
            elif _bins is not None and _quantiles is None and _zero_aware:
                pos_bins = pd.cut(x[x >= 0], _bins // 2, labels=False) + _bins // 2 + 1
                neg_bins = pd.cut(x[x < 0], _bins // 2, labels=False) + 1
                return pd.concat([pos_bins, neg_bins]).sort_index()
        except Exception as e:
            if _no_raise:
                return pd.Series(index=x.index)
            raise e

    grouper = [factor_data.index.get_level_values("date")]
    if by_group:
        if "group" not in factor_data.columns:
            raise ValueError("只有输入了 groupby 参数时 binning_by_group 才能为 True")
        grouper.append("group")

    factor_quantile = factor_data.groupby(grouper)["factor"].apply(
        quantile_calc, quantiles, bins, zero_aware, no_raise
    )
    factor_quantile.name = "factor_quantile"
    if factor_quantile.index.names[0] == factor_quantile.index.names[1]:
        factor_quantile = factor_quantile.droplevel(level=0)
    return factor_quantile.dropna()


def compute_forward_returns(
    factor: pd.Series, prices: pd.DataFrame, periods: tuple = (1, 5, 10, 20)
) -> pd.DataFrame:
    """
    计算每个因子值对应的 N 期因子远期收益

    :param factor: 因子值向量
    :type pd.Series: index(level 0)为日期, index(level 1)为资产code, 值为因子数值
    :param price: 资产的价格数据，如收盘价close, prices中包含factor中对应的时间和前向period后的数据
    :type pd.DataFrame: index为日期, columns为资产code
    :param periods: periods(按日)后的时间间隔
    :type tuple:
    :return: 前向收益(如5日后收益率)矩阵,index(level 0)为日期(date), index(level 1)为资产code(asset), column为对应的period日期间隔(period_{p})
    :rtype: pd.DataFrame
    """

    factor_dateindex = factor.index.levels[0]
    factor_dateindex = factor_dateindex.intersection(prices.index)

    if len(factor_dateindex) == 0:
        raise ValueError(
            "Factor and prices indices don't match: make sure "
            "they have the same convention in terms of datetimes "
            "and symbol-names"
        )

    prices = prices.filter(items=factor.index.levels[1])

    forward_returns = pd.DataFrame(
        index=pd.MultiIndex.from_product(
            [prices.index, prices.columns], names=["date", "asset"]
        )
    )

    for period in periods:
        delta = prices.pct_change(period).shift(-period).reindex(factor_dateindex)
        forward_returns["period_{p}".format(p=period)] = delta.stack()

    forward_returns.index = forward_returns.index.rename(["date", "asset"])

    return forward_returns


def demean_forward_returns(factor_data, grouper=None):
    """
    根据相关分组为因子远期收益去均值.
    分组去均值包含了投资组合分组中性化约束的假设，因此允许跨组评估因子.


    :param factor_data:
    :type pd.DataFrame: index(level 0)为日期, index(level 1)为资产code, value为因子值、因子前向收益、因子分位数
    :param grouper: 默认为None，此时只根据日期作为分组计算均值; 否则按grouper组内计算均值
    :type list:
    :return: adjusted_forward_returns 按分组去均值后的factor_data
    :rtype: pd.DataFrame
    """

    factor_data = factor_data.copy()

    if not grouper:
        grouper = factor_data.index.get_level_values("date")

    cols = get_forward_returns_columns(factor_data.columns)
    factor_data[cols] = factor_data.groupby(grouper)[cols].transform(
        lambda x: x - x.mean()
    )

    return factor_data
