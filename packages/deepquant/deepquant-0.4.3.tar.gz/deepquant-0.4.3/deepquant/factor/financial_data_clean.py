import sys
import bisect
from deepquant.factor.globals import BALANCESHEET_ITEMS, INCOME_ITEMS, CASHFLOW_ITEMS
import pandas as pd
import numpy as np

from dateutil.relativedelta import relativedelta

# 因子计算入口
def total_asset_growth_rate(data):
    data['total_asset_growth_rate'] = data['pre_0'] / data['pre_4'] - 1
    factor = data.pivot(index="dt", columns="code", values='total_asset_growth_rate')

    return factor


def get_financial_report_data(stk_codes, data_start_dt, data_end_dt, meta_fields, col_list, sheet_name='cashflow'):
    sheet_name = sheet_name.lower()
    if sheet_name not in ['cashflow', 'balancesheet', 'income']:
        raise ValueError(
            f"sheet_name '{sheet_name}' is incorrect.\n"
            f"Only one of the following is supported:\n"
            f"cashflow, balancesheet, income."
        )

    if sheet_name == 'cashflow':
        data, code, msg = gid.cashflow(stk_codes, data_start_dt, data_end_dt, fields=meta_fields+col_list)
    elif sheet_name == 'balancesheet':
        data, code, msg = gid.balancesheet(stk_codes, data_start_dt, data_end_dt, fields=meta_fields+col_list)
    else:
        data, code, msg = gid.income(stk_codes, data_start_dt, data_end_dt, fields=meta_fields+col_list)

    #item = fields[-1]
    data = data[data.statement_type.isin(['1', '4', '5'])]
    # data = data[['market_code', 'actual_ann_date', 'reporting_period', item]].reset_index(drop=True)
    data = data[['market_code', 'actual_ann_date', 'reporting_period'] + col_list].reset_index(drop=True)
    data.columns = ['code', 'actual_ann_date', 'report_dt'] + col_list
    data['actual_ann_date'] = pd.to_datetime(data['actual_ann_date'])
    data['report_dt'] = pd.to_datetime(data['report_dt'])
    data = data.sort_values(by=["actual_ann_date", "report_dt", "code"])
    # data = data.dropna(how="any")
    return data

def get_last_valid_index(row, cols):
    idx = row.last_valid_index()
    try:
        return bisect.bisect_left(cols, idx) + 1
    except:
        return 0


def extract_values(data_values, start_locs, end_locs, period):
    start_locs = np.maximum(end_locs - period, 0)
    values = np.empty(data_values.shape[0] * period, np.float64).reshape(
        data_values.shape[0], period
    )
    values[:] = np.nan
    filled_rows = (end_locs != start_locs).nonzero()
    for i in filled_rows[0]:
        values[i, start_locs[i] - end_locs[i]:] = data_values[
                                                  i, start_locs[i]: end_locs[i]
                                                  ]
    return values


def interpolate_4cols(x):
    to_fill = np.empty(x.shape[0] * 12, np.float64).reshape(x.shape[0], 12)
    # fill col 0
    to_fill[:, 0] = 2.0 * x[:, 1] - x[:, 2]
    to_fill[:, 1] = 1.5 * x[:, 1] - 0.5 * x[:, 3]
    to_fill[:, 2] = 3.0 * x[:, 2] - 2.0 * x[:, 3]

    # fill col 1
    to_fill[:, 3] = 0.5 * (x[:, 0] + x[:, 2])
    to_fill[:, 4] = 2.0 / 3.0 * x[:, 0] + 1.0 / 3.0 * x[:, 3]
    to_fill[:, 5] = 2.0 * x[:, 2] - x[:, 3]

    # fill col 2
    to_fill[:, 6] = 0.5 * (x[:, 1] + x[:, 3])
    to_fill[:, 7] = 2.0 / 3.0 * x[:, 3] + 1.0 / 3.0 * x[:, 0]
    to_fill[:, 8] = 2.0 * x[:, 1] - x[:, 0]

    # fill col3
    to_fill[:, 9] = 2.0 * x[:, 2] - x[:, 1]
    to_fill[:, 10] = 1.5 * x[:, 2] - 0.5 * x[:, 0]
    to_fill[:, 11] = 3.0 * x[:, 1] - 2.0 * x[:, 0]
    target = x.copy()
    col = 0
    for i in range(4):
        for _ in range(3):
            target[:, i] = np.where(
                target[:, i] == target[:, i], target[:, i], to_fill[:, col]
            )
            col += 1

    nan_sums = np.isnan(target).sum(axis=1)
    nan_rows = ((nan_sums > 0) & (nan_sums < 4)).nonzero()[0]

    target[nan_rows, :] /= np.array([1.0, 2.0, 3.0, 4.0])
    target[nan_rows, :] = np.where(
        target[nan_rows, :] == target[nan_rows, :], target[nan_rows, :], 0.0
    )
    tmp = target[nan_rows, :].sum(axis=1)
    target[nan_rows, :] = tmp.reshape(-1, 1)
    target[nan_rows, :] *= np.array([1.0, 2.0, 3.0, 4.0])
    return target


def interpolate_3cols(x, scales):
    to_fill = np.empty(x.shape[0] * 9, np.float64).reshape(x.shape[0], 9)
    to_fill[:, 0] = 2.0 * x[:, 1] - x[:, 2]
    to_fill[:, 1] = x[:, 1] / scales[1] * scales[0]
    to_fill[:, 2] = x[:, 2] / scales[2] * scales[0]
    to_fill[:, 3] = 0.5 * (x[:, 0] + x[:, 2])
    to_fill[:, 4] = x[:, 0] / scales[0] * scales[1]
    to_fill[:, 5] = x[:, 2] / scales[2] * scales[1]
    to_fill[:, 6] = 2.0 * x[:, 1] - x[:, 0]
    to_fill[:, 7] = x[:, 1] / scales[1] * scales[2]
    to_fill[:, 8] = x[:, 0] / scales[0] * scales[2]
    target = x.copy()
    col = 0
    for i in range(3):
        for _ in range(3):
            target[:, i] = np.where(
                target[:, i] == target[:, i], target[:, i], to_fill[:, col]
            )
            col += 1
    return target


def interpolate_2cols(x, scales):
    target = x.copy()
    target[:, 0] = np.where(
        target[:, 0] == target[:, 0], target[:, 0], x[:, 1] / scales[1] * scales[0]
    )
    target[:, 1] = np.where(
        target[:, 1] == target[:, 1], target[:, 1], x[:, 0] / scales[0] * scales[1]
    )
    return target


def interpolate_by_marks(values, marks):
    # first part needs to be deal with
    if marks[0] != 1:
        if marks[0] == 2:
            values[:, : marks[0]] = interpolate_2cols(
                values[:, : marks[0]], np.array([3.0, 4.0])
            )
        elif marks[0] == 3:
            values[:, : marks[0]] = interpolate_3cols(
                values[:, : marks[0]], np.array([2.0, 3.0, 4.0])
            )
        elif marks[0] == 4:
            values[:, : marks[0]] = interpolate_4cols(values[:, : marks[0]])

        values[:, 1: marks[0]] = values[:, 1: marks[0]] - values[:, : marks[0] - 1]

    for i in range(len(marks) - 2):
        values[:, marks[i]: marks[i + 1]] = interpolate_4cols(
            values[:, marks[i]: marks[i + 1]]
        )
        values[:, marks[i] + 1: marks[i + 1]] = (
                values[:, marks[i] + 1: marks[i + 1]]
                - values[:, marks[i]: marks[i + 1] - 1]
        )

    length = marks[-1] - marks[-2]
    if length != 1:
        if length == 2:
            values[:, marks[-2]: marks[-1]] = interpolate_2cols(
                values[:, marks[-2]: marks[-1]], np.array([1.0, 2.0])
            )
        elif length == 3:
            values[:, marks[-2]: marks[-1]] = interpolate_3cols(
                values[:, marks[-2]: marks[-1]], np.array([1.0, 2.0, 3.0])
            )
        elif length == 4:
            values[:, marks[-2]: marks[-1]] = interpolate_4cols(
                values[:, marks[-2]: marks[-1]]
            )
        values[:, marks[-2] + 1: marks[-1]] = (
                values[:, marks[-2] + 1: marks[-1]] - values[:, marks[-2]: marks[-1] - 1]
        )
    return values


def clean_process_variable(data, col_name, start_time, n_periods=9, ):
    # re-organize data
    data = data.pivot_table(
        index=["code", "actual_ann_date"], columns="report_dt", values=col_name
    )
    data = data.loc[:, data.columns >= pd.to_datetime(start_time)]  # type: ignore
    ## make sure all quarters are available
    report_periods = pd.date_range(data.columns.min(), data.columns.max(), freq="QE")
    data = data.reindex(report_periods, axis=1)
    data.sort_index(inplace=True)  # retrieve all available previous reports for a given ann_dt
    data = data.groupby(level=0, group_keys=False).ffill()

    end_locs = data.apply(lambda row: get_last_valid_index(row, data.columns), axis=1)
    end_locs = end_locs.values
    start_locs = np.maximum(end_locs - n_periods, 0)  # type: ignore

    data_values = data.values
    year_end_marks = (pd.DatetimeIndex(data.columns).month == 12).nonzero()[0]
    if year_end_marks[-1] != data.shape[1] - 1:
        year_end_marks = np.append(year_end_marks, data.shape[1] - 1)
    year_end_marks += 1
    data_values = interpolate_by_marks(data_values, year_end_marks)
    ## ffill using the latest available data from the previous corresponding quarter
    for i in range(4):
        data.iloc[:, i::4] = data.iloc[:, i::4].ffill(axis=1)

    values = extract_values(data_values, start_locs, end_locs, n_periods)

    results = pd.DataFrame(
        values, index=data.index, columns=range(n_periods - 1, -1, -1)
    )
    results["report_dt"] = [
        data.columns[i - 1] if i != 0 else pd.NaT for i in end_locs  # type: ignore
    ]

    new_col_name = [f"{col_name}" if i==0 else f"{col_name}_{i}q" for i in range(n_periods - 1, -1, -1)]
    results.columns = new_col_name + [
        "report_dt"
    ]  # type: ignore
    results.reset_index(inplace=True)
    results = results[["code", "actual_ann_date", "report_dt"] + new_col_name[::-1]].fillna(0.0)

    return results


def clean_state_variable(data, col_name, start_time, n_periods=9, pad_width=4):
    # print('--------------orig data-------------------')
    # print(data)
    # re-organize data
    data = data.pivot_table(index=["code", "actual_ann_date"], columns="report_dt", values=col_name)
    # print('--------------pivot_table-------------------')
    # print(data)
    data = data.loc[:, data.columns >= start_time]  # type: ignore
    report_periods = pd.date_range(data.columns.min(), data.columns.max(), freq="QE")
    # print('--------------report_periods-------------------')
    # print(report_periods)
    data = data.reindex(report_periods, axis=1)
    data.sort_index(inplace=True)
    # print('--------------sort_index-------------------')
    # print(data)
    # retrieve all available previous reports for a given ann_dt
    data = data.groupby(data.index.get_level_values(0), group_keys=False).ffill()
    # print('--------------groupby-------------------')
    # print(data)
    period = n_periods + pad_width
    # print('--------------period-------------------')
    # print(period)
    end_locs = data.apply(lambda row: get_last_valid_index(row, data.columns), axis=1)
    # print('--------------end_locs-------------------')
    # print(end_locs)
    end_locs = end_locs.values
    # print('--------------end_locs-------------------')
    # print(end_locs)
    data_values = data.values
    # print('--------------data_values-------------------')
    # print(data_values)
    start_locs = np.maximum(end_locs - period, 0)  # type: ignore
    # print('--------------start_locs-------------------')
    # print(start_locs)

    values = extract_values(data_values, start_locs, end_locs, period)
    results = pd.DataFrame(values, index=data.index, columns=range(period - 1, -1, -1))

    labels = (~results.isna()).sum(axis=1) >= 2

    results.loc[labels, :] = results.loc[labels, :].interpolate(method="slinear", axis=1)

    results = results.iloc[:, pad_width:]
    results.loc[:, "report_dt"] = [data.columns[i - 1] if i != 0 else pd.NaT for i in end_locs]

    results.columns = [f"{col_name}_{i}q" for i in range(period - 1 - pad_width, -1, -1)] + ["report_dt"]  # type: ignore
    results.reset_index(inplace=True)
    results = results[["code", "actual_ann_date", "report_dt"] + [f"{col_name}_{i}q" for i in range(n_periods)]].fillna(0.0)

    return results


def clean_financial_item(one_factor_data, col_name, variable_type, n_periods, start_time, pad_width):
    if variable_type.lower() == "state":
        return clean_state_variable(
            data=one_factor_data, col_name=col_name, n_periods=n_periods, start_time=start_time, pad_width=pad_width
        )
    elif variable_type.lower() == "process":
        return clean_process_variable(
            data=one_factor_data, col_name=col_name, n_periods=n_periods, start_time=start_time
        )
    else:
        raise ValueError(
            f"Variable type: {variable_type} is unknown. Supported types are state and process"
        )


def get_trade_cal(start_dt, end_dt):
    trade_cal, _, _ = gid.get_kline(
        market_code=['000001.SH'],
        frequency='1d',
        fields=['orig_time', 'symbol'],
        start_time=f"{start_dt} 09:30:00",
        end_time=f"{end_dt} 09:30:00",
    )
    trade_cal['dt'] = pd.to_datetime(trade_cal['orig_time'])
    trade_cal = trade_cal[['dt']].set_index('dt')
    trade_cal = trade_cal.loc[f"{start_dt}":f"{end_dt}"].reset_index()

    return trade_cal


def get_processed_financial_data(stk_codes, start_dt, end_dt, table, item, n_periods=9, pad_width=4):
    # index_stk_df, code, msg = gid.index_con(index_code=[task_info["stockIndex"]])
    # stk_codes = index_stk_df['con_code'].to_list()
    #stk_codes = ['000001.SZ', '600000.SH']

    # 因子起止时间，从task info中获取
    # factor_start_dt = task_info['startDate']
    # factor_end_dt = task_info['startDate']
    # 数据开始时间，取因子开始三年前数据
    data_start_dt = (pd.to_datetime(start_dt) - relativedelta(years=3)).strftime("%Y-%m-%d")
    data_end_dt = pd.to_datetime(end_dt).strftime("%Y-%m-%d")

    # 要获取的数据列名
    # item = 'free_cash_flow'
    col_set = set()
    if table == 'cashflow':
        for key in item:
            if key in CASHFLOW_ITEMS:
                col_set.add(key)
            else:
                real_key = '_'.join(key.split('_')[:-1])
                if real_key in CASHFLOW_ITEMS:
                    col_set.add(real_key)
                else:
                    raise ValueError("Invalid item.")
    elif table == 'balancesheet':
        for key in item:
            if key in BALANCESHEET_ITEMS:
                col_set.add(key)
            else:
                real_key = '_'.join(key.split('_')[:-1])
                if real_key in BALANCESHEET_ITEMS:
                    col_set.add(real_key)
                else:
                    raise ValueError("Invalid item.")
    elif table == 'income':
        for key in item:
            if key in INCOME_ITEMS:
                col_set.add(key)
            else:
                real_key = '_'.join(key.split('_')[:-1])
                if real_key in INCOME_ITEMS:
                    col_set.add(real_key)
                else:
                    raise ValueError("Invalid item.")
    else:
        raise ValueError("Invalid table.")
    col_list = list(col_set)
    meta_fields = ['market_code', 'actual_ann_date', 'reporting_period', 'statement_type']
    # fields = meta_fields + col_list  # 前四项必取
    # 原始数据
    data = get_financial_report_data(stk_codes, data_start_dt, data_end_dt, meta_fields, col_list, table)
    # print(data)
    if table == "balancesheet":
        variable_type = "state"
    else:
        variable_type = "process"
    sort_cols = ['code', 'actual_ann_date', 'report_dt']
    all_factor_data = pd.DataFrame()
    for column in col_list:
        if column not in data.columns:
            print(f"{column} not in gid return data")
            continue
        one_factor_data = data[sort_cols + [column]]
        one_factor_data = one_factor_data.dropna(how="any")
        if len(one_factor_data) == 0:
            print(f"{column} has no data")
            continue
        one_factor_data = clean_financial_item(one_factor_data, column, variable_type, n_periods, data_start_dt, pad_width)
        # print('---------clean data------------------')
        # print(one_factor_data)
        one_factor_data["report_dt"] = pd.to_datetime(one_factor_data["report_dt"])
        one_factor_data["actual_ann_date"] = pd.to_datetime(one_factor_data["actual_ann_date"])
        one_factor_data = one_factor_data.drop_duplicates(subset=["code", "actual_ann_date"], keep="last")
        one_factor_data = one_factor_data.set_index(["code", "actual_ann_date"])

        one_factor_data.index.names = ('code', 'dt')
        # print('---------reindex data------------------')
        # print(one_factor_data)

        all_dates = pd.DataFrame({stk: True for stk in stk_codes}, index=pd.date_range('2015-01-01',
                                                                                       f"{data_end_dt}")).stack().to_frame().swaplevel().sort_index()
        # print('---------all_dates------------------')
        # print(all_dates)
        all_dates.index.names = ('code', 'dt')
        # print('---------all_dates------------------')
        # print(all_dates)
        one_factor_data = pd.merge(all_dates, one_factor_data, left_index=True, right_index=True, how='left')
        one_factor_data = one_factor_data.groupby(level=0).ffill()
        one_factor_data = one_factor_data.drop(columns={0})
        one_factor_data = one_factor_data.dropna(how='all')
        one_factor_data = one_factor_data.reset_index()

        # print(data.columns)

        # 关联交易日
        trade_cal = get_trade_cal(data_start_dt, data_end_dt)
        # print(trade_cal)
        one_factor_data = one_factor_data[one_factor_data['dt'].isin(trade_cal.dt.values)].reset_index(drop=True)  # 清洗
        # print('-------one_factor_data----------')
        # print(one_factor_data.columns)
        # print(one_factor_data)
        if len(all_factor_data.columns) == 0:
            all_factor_data = one_factor_data
        else:
            all_factor_data = pd.merge(all_factor_data, one_factor_data, on=['code', 'dt', 'report_dt'], how="outer")
    return all_factor_data


if __name__ == '__main__':

    data = get_processed_financial_data( ['000001.SZ', '600000.SH'], '2020-07-01', '2024-08-01', 'balancesheet', ['total_assets_1q','total_assets_3q', 'total_liab'], n_periods=9, pad_width=4)
    print(data)
