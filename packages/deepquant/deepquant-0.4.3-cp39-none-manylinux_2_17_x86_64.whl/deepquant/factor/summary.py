import pandas as pd
from . import utils
from . import analysor
from . import perf

def create_returns_sheet(
    factor_data, long_short=True, group_neutral=False, by_group=False
    ):
    factor_returns = perf.factor_returns(
        factor_data, long_short, group_neutral
    )
    print("----factor_returns\n", factor_returns.head())

    mean_quant_ret, std_quantile = perf.mean_return_by_quantile(
        factor_data,
        by_group=False,
        demeaned=long_short,
        group_adjust=group_neutral,
    )
    print("----mean_return_by_quantile\n", std_quantile, mean_quant_ret.head())

    mean_quant_rateret = mean_quant_ret.apply(
        utils.rate_of_return, axis=0, base_period=1)
    print("----rate_of_return\n", mean_quant_rateret)

    mean_quant_ret_bydate, std_quant_daily = perf.mean_return_by_quantile(
        factor_data,
        by_date=True,
        by_group=False,
        demeaned=long_short,
        group_adjust=group_neutral,
    )
    print("---mean_return_by_quantile_date\n", mean_quant_ret_bydate.head())

    mean_quant_rateret_bydate = mean_quant_ret_bydate.apply(
        utils.rate_of_return,
        axis=0,
        base_period=1,
    )
    print("---mean_return_by_quantile_date_rate_of_return\n", mean_quant_rateret_bydate)

    compstd_quant_daily = std_quant_daily.apply(
        utils.std_conversion, axis=0, base_period=1
    )
    print("---compstd_quant_daily", compstd_quant_daily.head())

    alpha_beta = perf.factor_alpha_beta(
        factor_data, factor_returns, long_short, group_neutral
    )
    print("---alpha_beta", alpha_beta)

    mean_ret_spread_quant, std_spread_quant = perf.compute_mean_returns_spread(
        mean_quant_rateret_bydate,
        factor_data["factor_quantile"].max(),
        factor_data["factor_quantile"].min(),
        std_err=compstd_quant_daily,
    )
    print("---perf.compute_mean_returns_spread", mean_ret_spread_quant)
    
    print("\n======by group=======\n")

    if by_group:
        (
            mean_return_quantile_group,
            mean_return_quantile_group_std_err,
        ) = perf.mean_return_by_quantile(
            factor_data,
            by_date=False,
            by_group=True,
            demeaned=long_short,
            group_adjust=group_neutral,
        )
        print("---mean_return_quantile_group", mean_return_quantile_group.head())

        mean_quant_rateret_group = mean_return_quantile_group.apply(
            utils.rate_of_return,
            axis=0,
            base_period=1,
        )
        print("---mean_quant_rateret_group", mean_quant_rateret_group.head())
    

def create_information_sheet(
    factor_data, group_neutral=False, by_group=False
    ):
    ic = perf.factor_information_coefficient(factor_data, group_neutral)
    print("---ic----", ic)

    if not by_group:

        mean_monthly_ic = perf.mean_information_coefficient(
            factor_data,
            group_adjust=group_neutral,
            by_group=False,
            by_time="M",
        )
        print("---mean_monthly_ic----", mean_monthly_ic)

    if by_group:
        mean_group_ic = perf.mean_information_coefficient(
            factor_data, group_adjust=group_neutral, by_group=True
        )
        print("---mean_group_ic----", mean_group_ic)


def create_turnover_sheet(factor_data, turnover_periods=None):
    if turnover_periods is None:
        input_periods = utils.get_forward_returns_columns(
            factor_data.columns
        ).values
        turnover_periods = utils.timedelta_strings_to_integers(input_periods)
    else:
        turnover_periods = utils.timedelta_strings_to_integers(
            turnover_periods,
        )

    quantile_factor = factor_data["factor_quantile"]

    quantile_turnover = {
        p: pd.concat(
            [
                perf.quantile_turnover(quantile_factor, q, p)
                for q in quantile_factor.sort_values().unique().tolist()
            ],
            axis=1,
        )
        for p in turnover_periods
    }  
    print("----quantile_turnover----", quantile_turnover)

    autocorrelation = pd.concat(
        [
            perf.factor_rank_autocorrelation(factor_data, period)
            for period in turnover_periods
        ],
        axis=1,
    )
    print("----autocorrelation----", autocorrelation)


