import os
import numpy as np
import pandas as pd
import pyecharts
from scipy import stats
import pyecharts.options as opts
from pyecharts.globals import CurrentConfig, NotebookType
from pyecharts.globals import ThemeType

from pyecharts.charts import Line, Bar, Page, HeatMap
from pyecharts.components import Table

from . import perf
from . import utils
from ..data.utils import gqconfig

#CurrentConfig.ONLINE_HOST = "http://10.4.21.71/assets/"
assets_host = gqconfig.configs.c_server['host']
CurrentConfig.ONLINE_HOST = f"http://{assets_host}/gid/static/assets/"
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

conf = dict(theme=ThemeType.DARK, width="900px", height="400px", pos_right="10%")
formatter = pyecharts.commons.utils.JsCode(
    """function (params) {
    params.sort(function (a, b) {
        return b.value - a.value;
    });
    var tooltipText = params.map(function (item) {
        return item.seriesName + ': ' + item.value;
    }).join('<br/>');
    return tooltipText;
}"""
)
DECIMAL_TO_BPS = 1e4


def plot_factor_rank_auto_correlation(factor_autocorrelation, period=1):
    line = Line(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(title=f"period_{period}因子秩相关性系数", pos_left="center"),
        yaxis_opts=opts.AxisOpts(
            name="自相关系数",
            name_location="middle",
            name_gap="50",
            is_scale=True,
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis", axis_pointer_type="line", formatter=formatter
        ),
        legend_opts=opts.LegendOpts(pos_right="10%", pos_top="8%"),
    )
    x = factor_autocorrelation.index.strftime("%Y-%m-%d").tolist()
    line.add_xaxis(x)
    y = factor_autocorrelation.fillna(0).values.round(4).astype(float).tolist()
    line.add_yaxis(
        f"perid_{period}", y, label_opts=opts.LabelOpts(is_show=False), is_smooth=True
    )
    return line


def plot_top_bottom_quantile_turnover(quantile_turnover, period=1):
    top = quantile_turnover.max()
    bottom = quantile_turnover.min()
    t = {
        "top": perf.quantile_turnover(quantile_turnover, bottom, period),
        "bottom": perf.quantile_turnover(quantile_turnover, top, period),
    }
    line = Line(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(
            title=f"period_{period}最大分位组和最小分位组的换手率", pos_left="center"
        ),
        yaxis_opts=opts.AxisOpts(
            name="换手率",
            name_location="middle",
            name_gap="50",
            is_scale=True,
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis", axis_pointer_type="line", formatter=formatter
        ),
        legend_opts=opts.LegendOpts(pos_right="10%", pos_top="8%"),
    )
    x = t["top"].index.strftime("%Y-%m-%d").tolist()
    line.add_xaxis(x)
    for name, val in t.items():
        y = val.fillna(0).values.round(4).astype(float).tolist()
        line.add_yaxis(
            f"{name}组", y, label_opts=opts.LabelOpts(is_show=False), is_smooth=True
        )
    return line


def plot_ic_by_group(mean_group_ic):
    bar = Bar(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(title="按Group的IC均值"),
        yaxis_opts=opts.AxisOpts(
            name="IC", name_location="middle", name_gap=35, is_scale=True
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="line",
        ),
        legend_opts=opts.LegendOpts(pos_right="10%"),
    )
    x = list(mean_group_ic.index)
    for col in mean_group_ic.columns:
        y = np.round(mean_group_ic[col].values * 10000, 4).astype(float).tolist()
        bar.add_xaxis(x)
        bar.add_yaxis(
            f"{col}组",
            y,
            gap=0,
            bar_width="20%",
            label_opts=opts.LabelOpts(is_show=False),
        )
    return bar

def plot_ic_ts(ic):
    line = Line(
        init_opts=dict(
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(title="信息比率(IC)时间序列图", pos_left="center"),
        yaxis_opts=opts.AxisOpts(
            name="IC",
            name_location="middle",
            name_gap="50",
            is_scale=True,
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis", axis_pointer_type="line", formatter=formatter
        ),
        legend_opts=opts.LegendOpts(pos_right="10%", pos_top="8%"),
    )
    x = ic.index.strftime("%Y-%m-%d").tolist()
    line.add_xaxis(x)
    for col in ic.columns:
        y = np.round(ic[col].values, 4).astype(float).tolist()
        line.add_yaxis(
            f"ic_{col}", y, label_opts=opts.LabelOpts(is_show=False), is_smooth=True
        )
    return line

def plot_ic_qq(ic, theoretical_dist=stats.norm):

    pass

def plot_ic_hist(ic_data, col="period_1", numbins=30):
    vals = ic_data[col].values
    bin_edges = np.linspace(vals.min(), vals.max(), numbins + 1)
    binned_data = pd.cut(vals, bins=bin_edges)
    df = binned_data.value_counts().reset_index()
    df["mid"] = df["index"].apply(lambda x: x.mid.round(4))
    y = []
    for idx, row in df.iterrows():
        y.append(
            opts.BarItem(
                name=row["mid"],
                value=row["count"],
            )
        )
    x = df["mid"].values.tolist()
    bar = Bar(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(
            title=f"IC分布直方图（均值: {vals.mean():.3f}, 标准差:{vals.std():.3f}）"
        ),
        yaxis_opts=opts.AxisOpts(
            name="Density", name_location="middle", name_gap=35, is_scale=True
        ),
        xaxis_opts=opts.AxisOpts(
            name="IC", name_location="middle", name_gap=25, is_scale=True
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="line",
        ),
        legend_opts=opts.LegendOpts(pos_right="10%"),
    )
    bar.add_xaxis(x).add_yaxis(f"{col}", y, category_gap=1)
    return bar


def plot_quantile_returns_bar(
    mean_quant_rateret, by_group=False, ylim_percentiles=None, ax=None
):
    bar = Bar(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(title="按分组平均收益"),
        yaxis_opts=opts.AxisOpts(
            name="平均收益率", name_location="middle", name_gap=35, is_scale=True
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="line",
        ),
        legend_opts=opts.LegendOpts(pos_right="10%"),
    )
    x = list(mean_quant_rateret.index)
    for col in mean_quant_rateret.columns:
        y = np.round(mean_quant_rateret[col].values * 10000, 4).astype(float).tolist()
        bar.add_xaxis(x)
        bar.add_yaxis(
            f"{col}组",
            y,
            gap=0,
            bar_width="20%",
            label_opts=opts.LabelOpts(is_show=False),
        )

    return bar


def plot_quantile_returns_bars(
    mean_quant_rateret, by_group=False, ylim_percentiles=None, ax=None, conf=conf
):

    def create_bar(sub_df, title, width, height):
        bar = Bar(
            init_opts=dict(
                # theme=ThemeType.WALDEN,
                theme=conf["theme"],
                width=width,
                height=height,
            )
        ).set_global_opts(
            opts.TitleOpts(title=title),
            yaxis_opts=opts.AxisOpts(
                name="平均收益率", name_location="middle", name_gap=35, is_scale=True
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="axis",
                axis_pointer_type="line",
            ),
            legend_opts=opts.LegendOpts(pos_right="10%"),
        )
        x = list(sub_df.index)
        for col in sub_df.columns:
            y = np.round(sub_df[col].values * DECIMAL_TO_BPS, 4).astype(float).tolist()
            bar.add_xaxis(x)
            bar.add_yaxis(
                f"{col}组",
                y,
                gap=0,
                bar_width="20%",
                label_opts=opts.LabelOpts(is_show=False),
            )
        return bar

    bars = []
    if by_group and "group" in mean_quant_rateret.columns:
        grp_names = (
            mean_quant_rateret.index.get_level_values("group").unique().values.tolist()
        )
        for i, grp in enumerate(grp_names):
            bars.append(
                create_bar(
                    mean_quant_rateret.xs(grp, level="group"),
                    title=f"Group[{grp}]按分位平均收益",
                    width=conf["width"],
                    height=conf["height"],
                )
            )
    else:
        bars.append(
            create_bar(
                mean_quant_rateret,
                title="按分位平均收益",
                width=conf["width"],
                height=conf["height"],
            )
        )
    return bars


def plot_cumulative_returns_by_quantile(
    quantile_returns, period, freq=None, ax=None, conf=conf
):
    cum_returns = (
        quantile_returns[f"period_{period}"]
        .unstack("factor_quantile")
        .apply(perf.cumulative_returns)
    )
    line = Line(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(title="按分组累积收益曲线"),
        yaxis_opts=opts.AxisOpts(
            name="净值", name_location="middle", name_gap=35, is_scale=True
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis", axis_pointer_type="line", formatter=formatter
        ),
        legend_opts=opts.LegendOpts(pos_right="10%"),
    )
    x = list(cum_returns.index.strftime("%Y-%m-%d"))
    for col in cum_returns.columns:
        y = np.round(cum_returns[col].values, 4).astype(float).tolist()
        line.add_xaxis(x)
        line.add_yaxis(
            f"{col}组", y, label_opts=opts.LabelOpts(is_show=False), is_smooth=True
        )
    return line


def plot_cumulative_returns(
    factor_returns, periods=[1], freq=None, title=None, conf=conf
):
    cum_returns = perf.cumulative_returns(factor_returns)
    line = Line(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(title="组合累积收益曲线"),
        yaxis_opts=opts.AxisOpts(
            name="净值", name_location="middle", name_gap=35, is_scale=True
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis", axis_pointer_type="line", formatter=formatter
        ),
        legend_opts=opts.LegendOpts(pos_right="10%"),
    )
    x = list(cum_returns.index.strftime("%Y-%m-%d"))
    for col in utils.get_forward_returns_columns(cum_returns.columns).values:
        if int(col.replace("period_", "")) not in periods:
            continue
        y = np.round(cum_returns[col].values, 4).astype(float).tolist()
        line.add_xaxis(x)
        line.add_yaxis(col, y, label_opts=opts.LabelOpts(is_show=False), is_smooth=True)
    return line


def plot_information_table(ic_data):
    table = Table()
    headers = [""] + ic_data.columns.values.tolist()
    row = [
        ["IC Mean"] + ic_data.mean().values.round(4).tolist(),
        ["IC Std"] + ic_data.std().values.round(4).tolist(),
        ["Risk-Adjusted IC"]
        + (ic_data.mean() / ic_data.std()).values.round(4).tolist(),
    ]
    t_stat, p_value = stats.ttest_1samp(ic_data, 0)
    row.extend(
        [
            ["t-stat(IC)"] + t_stat.round(4).tolist(),
            ["p-value(IC)"] + p_value.round(4).tolist(),
            ["IC Skew"] + stats.skew(ic_data).round(4).tolist(),
            ["IC Kurtosis"] + stats.kurtosis(ic_data).round(4).tolist(),
        ]
    )
    table.add(headers, row)
    start_dt = ic_data.index.min().strftime("%Y-%m-%d")
    end_dt = ic_data.index.max().strftime("%Y-%m-%d")
    table.set_global_opts(
        title_opts=opts.ComponentTitleOpts(
            title="IC分析表", subtitle=f"时间范围: {start_dt}-{end_dt}"
        )
    )
    return table


def plot_mean_quantile_returns_spread_time_series(
    mean_ret_spread, std_spread=None, bandwidth=1, col="period_1", win_size=22
):
    mean_ret_spread = mean_ret_spread * DECIMAL_TO_BPS
    std_spread = std_spread * DECIMAL_TO_BPS
    line = Line(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(
            title=f"最大分位组减去最小分位组的收益({col})", pos_left="center"
        ),
        yaxis_opts=opts.AxisOpts(
            name="按quantile的平均收益差异(bps)",
            name_location="middle",
            name_gap="50",
            is_scale=True,
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis", axis_pointer_type="line", formatter=formatter
        ),
        legend_opts=opts.LegendOpts(pos_right="10%", pos_top="8%"),
    )
    x = list(mean_ret_spread.index.strftime("%Y-%m-%d"))
    y = mean_ret_spread[col].values.round(4).astype(float).tolist()
    y_up = (
        (mean_ret_spread[col] + std_spread[col]).values.round(4).astype(float).tolist()
    )
    y_down = (
        (mean_ret_spread[col] - std_spread[col]).values.round(4).astype(float).tolist()
    )
    y_mean = mean_ret_spread[col].rolling(win_size).mean()
    line.add_xaxis(x)
    line.add_yaxis(
        f"{col}组", y, label_opts=opts.LabelOpts(is_show=False), is_smooth=True
    )
    line.add_yaxis(
        f"{col}组+{bandwidth}std",
        y_up,
        stack="confidence-band",
        symbol=None,
        label_opts=opts.LabelOpts(is_show=False),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    )
    line.add_yaxis(
        f"{col}组-{bandwidth}std",
        y_down,
        stack="confidence-band",
        symbol=None,
        label_opts=opts.LabelOpts(is_show=False),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    )
    line.add_yaxis(
        f"{col}组-{win_size}ma",
        y_mean,
        linestyle_opts=opts.LineStyleOpts(width=2),
        symbol=None,
        label_opts=opts.LabelOpts(is_show=False),
    )
    return line


def plot_quantile_average_cumulative_return(
    avg_cumulative_returns,
    by_quantile=False,
    std_bar=False,
    ax=None,
    periods_before='',
    periods_after=''
):
    avg_cumulative_returns = avg_cumulative_returns.multiply(DECIMAL_TO_BPS)
    line = Line(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(title="因子预测能力平均累计收益图", pos_left="center", pos_bottom="1%"),
        yaxis_opts=opts.AxisOpts(
            name="均值和标准差", name_location="middle", name_gap=35, is_scale=True
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis", axis_pointer_type="line", formatter=formatter
        ),
        legend_opts=opts.LegendOpts(pos_right="10%"),
    )
    for i, (quantile, q_ret) in enumerate(
            avg_cumulative_returns.groupby(level='factor_quantile')
        ):

            mean = q_ret.loc[(quantile, 'mean')]
            mean = mean.sort_index()
            if i == 0: 
                x = mean.index.tolist()
                line.add_xaxis(x)
            y = mean.values.round(4).astype(float).tolist()
            line.add_yaxis(
            f"{quantile}分位mean", y, label_opts=opts.LabelOpts(is_show=False), is_smooth=True
            )
            if std_bar:
                std = q_ret.loc[(quantile, 'std')]
                std = std.sort_index()
                y = std.values.round(4).astype(float).tolist()
                line.add_yaxis(
                f"{quantile}分位std", y, label_opts=opts.LabelOpts(is_show=False), is_smooth=True
                )
    return line

def print_table(table, name=None, fmt=None):

    from IPython.display import display

    if isinstance(table, pd.Series):
        table = pd.DataFrame(table)

    if isinstance(table, pd.DataFrame):
        table.columns.name = name

    prev_option = pd.get_option('display.float_format')
    if fmt is not None:
        pd.set_option('display.float_format', lambda x: fmt.format(x))

    display(table)

    if fmt is not None:
        pd.set_option('display.float_format', prev_option)

def plot_returns_table(alpha_beta, mean_ret_quantile, mean_ret_spread_quantile):
    returns_table = pd.DataFrame()
    returns_table = pd.concat([returns_table, alpha_beta])
    returns_table.loc["Mean Period Wise Return Top Quantile (bps)"] = \
        mean_ret_quantile.iloc[-1] * DECIMAL_TO_BPS
    returns_table.loc["Mean Period Wise Return Bottom Quantile (bps)"] = \
        mean_ret_quantile.iloc[0] * DECIMAL_TO_BPS
    returns_table.loc["Mean Period Wise Spread (bps)"] = \
        mean_ret_spread_quantile.mean() * DECIMAL_TO_BPS

    print("收益分析")
    print_table(returns_table.apply(lambda x: x.round(3)))

def plot_turnover_table(autocorrelation_data, quantile_turnover):
    turnover_table = pd.DataFrame()
    for period in sorted(quantile_turnover.keys()):
        for quantile, p_data in quantile_turnover[period].items():
            turnover_table.loc["Quantile {} Mean Turnover ".format(quantile),
                               "{}".format(period)] = p_data.mean()
    auto_corr = pd.DataFrame()
    for period, p_data in autocorrelation_data.items():
        auto_corr.loc["Mean Factor Rank Autocorrelation", "{}"
                      .format(period)] = p_data.mean()

    print("换手率分析")
    print_table(turnover_table.apply(lambda x: x.round(3)))
    print_table(auto_corr.apply(lambda x: x.round(3)))


def plot_information_table(ic_data):
    ic_summary_table = pd.DataFrame()
    ic_summary_table["IC Mean"] = ic_data.mean()
    ic_summary_table["IC Std."] = ic_data.std()
    ic_summary_table["IR"] = ic_data.mean() / ic_data.std()
    t_stat, p_value = stats.ttest_1samp(ic_data, 0)
    ic_summary_table["t-stat(IC)"] = t_stat
    ic_summary_table["p-value(IC)"] = p_value
    ic_summary_table["IC Skew"] = stats.skew(ic_data)
    ic_summary_table["IC Kurtosis"] = stats.kurtosis(ic_data)

    print("IC 分析")
    print_table(ic_summary_table.apply(lambda x: x.round(3)).T)

def plot_quantile_statistics_table(factor_data):
    quantile_stats = factor_data.groupby('factor_quantile') \
        .agg(['min', 'max', 'mean', 'std', 'count'])['factor']
    quantile_stats['count %'] = quantile_stats['count'] \
        / quantile_stats['count'].sum() * 100.

    print("分位数统计")
    print_table(quantile_stats)

def plot_events_distribution(events, num_days=5, full_dates=None, ax=None):

    if full_dates is None:
        full_dates = events.index.get_level_values('date').unique()

    group = pd.Series(range(len(full_dates)), index=full_dates) // num_days
    grouper_label = group.drop_duplicates()
    grouper = group.reindex(events.index.get_level_values('date'))

    count = events.groupby(grouper.values).count()
    count = count.reindex(grouper_label.values, fill_value=0)
    count.index = grouper_label.index.map(lambda x: x.strftime('%Y-%m-%d'))


    bar = Bar(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(title="有效因子数量统计"),
        yaxis_opts=opts.AxisOpts(
            name="数量", name_location="middle", name_gap=35, is_scale=True
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="line",
        ),
        legend_opts=opts.LegendOpts(pos_right="10%"),
    )
    x = count.index.tolist()
    
    y = count.values.tolist()
    bar.add_xaxis(x)
    bar.add_yaxis(
        f"数量",
        y,
        gap=0,
        bar_width="20%",
        label_opts=opts.LabelOpts(is_show=False),
    )
    return bar

def plot_monthly_ic_heatmap(mean_monthly_ic, periods_num):

    heatmap = HeatMap(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"]
        )
    ).set_global_opts(
        opts.TitleOpts(title="月度信息系数(IC)图"),
        visualmap_opts=opts.VisualMapOpts(max_ = 1),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="line",
        ),
        legend_opts=opts.LegendOpts(pos_right="10%"),
    )
    mean_monthly_ic = mean_monthly_ic.fillna(0).round(4).astype(float)
    x = mean_monthly_ic.index.tolist()
    yaxis_data = mean_monthly_ic.columns.tolist()
    value = []
    i = 0
    for index, row in mean_monthly_ic.iterrows():
        j = 0
        for col_name in mean_monthly_ic.columns:
            ele = [i, j, row[col_name]]
            value.append(ele)
            j = j + 1
        i = i +1
    heatmap.add_xaxis(x)
    heatmap.add_yaxis(
        f"periods{periods_num}",
        yaxis_data = yaxis_data,
        value = value,
        label_opts=opts.LabelOpts(is_show=True, position='inside'))
    
    return heatmap

def plot_top_down_cumulative_returns(factor_returns, period=1, ax=None):

    line = Line(
        init_opts=dict(
            # theme=ThemeType.WALDEN,
            theme=conf["theme"],
            width=conf["width"],
            height=conf["height"],
        )
    ).set_global_opts(
        opts.TitleOpts(
            title=f"做多最大分位数做空最小分位数组合每日累积收益图", pos_left="center"
        ),
        yaxis_opts=opts.AxisOpts(
            name="收益",
            name_location="middle",
            name_gap="50",
            is_scale=True
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis", axis_pointer_type="line", formatter=formatter
        ),
        legend_opts=opts.LegendOpts(pos_right="10%", pos_top="8%"),
    )
    x = factor_returns.index.strftime("%Y-%m-%d").tolist()
    line.add_xaxis(x)
    y = factor_returns.fillna(0).values.round(4).astype(float).tolist()
    y_1 = [1 for _ in y]
    line.add_yaxis(
            f"period_{period}", y, label_opts=opts.LabelOpts(is_show=False), is_smooth=True
    )
    line.add_yaxis(
            f"收益1", y_1, linestyle_opts=opts.LineStyleOpts(color='red'),label_opts=opts.LabelOpts(is_show=False), is_smooth=True
    )
    
    return line
    
def show_one_page(charts, filename="", base_path=""):
    # charts = [
    #    plot_quantile_returns_bar(mean_quant_rateret),
    #    plot_cumulative_returns(factor_returns),
    #    plot_cumulative_returns_by_quantile(mean_quant_ret_bydate, period=5),
    # ]
    if not filename:
        filename = "factor_analyser.html"
    page = Page(layout=Page.DraggablePageLayout, page_title="deepquant.factor")
    for chart in charts:
        page.add(chart)
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    page.render(os.path.join(base_path, filename))
