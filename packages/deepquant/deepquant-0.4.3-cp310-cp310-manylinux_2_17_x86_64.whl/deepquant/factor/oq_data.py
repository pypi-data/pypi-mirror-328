import re
import logging
from urllib.parse import quote_plus

import datetime
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

from deepquant import gid
from .financial_data_clean import clean_financial_item


class DataSDKError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class OqData:

    def __init__(self, username="", password=""):
        gid.init(username, password)
        print(username, password)
        self.username = username
        self.apis = {
            "get_kline": self.get_kline,
            "QueryKline": self.get_kline,
            "get_factor": self.get_factor,
            "yield_factor": self.get_yield_factor,
            "derivind_factor": self.get_derivind_factor,
            "balancesheet": self.get_balancesheet,
            "income": self.get_income,
            "cashflow": self.get_cashflow,
            "fina_indicator": self.get_fina_indicator,
        }

    def oq_sdk(self, api_name, **params):
        data, code, msg = gid.__dict__[api_name](**params)
        if str(code) not in ("ApiRspCode.SUCCESS", "0"):
            raise (
                DataSDKError(
                    f"SDK({api_name}, fields:{params.get('fields')})错误: {code}, {msg}"
                )
            )
        if isinstance(data, pd.DataFrame):
            if data.empty:
                raise (
                    DataSDKError(
                        f"SDK({api_name}, fields:{params.get('fields')})空dataframe: {code}, {msg}"
                    )
                )
        if not isinstance(data, pd.DataFrame):
            raise (
                DataSDKError(
                    f"SDK({api_name}, fields:{params.get('fields')})返回{data}: {code}, {msg}"
                )
            )
        return data

    def get_yield_factor(self, fields, **params):
        params["fields"] = ["trade_date", "market_code"] + list(fields.values())
        if "frequency" in params:
            del params["frequency"]
        data = self.oq_sdk("yield_factor", **params)
        data["trade_date"] = pd.to_datetime(data["trade_date"], format="%Y%m%d")
        data = data.rename(
            columns={
                "market_code": "code",
                "trade_date": "dt",
            }
        )
        return data

    def get_findata(self, sheet, fields, **params):
        # stk_codes = self.get_index_stk_codes(params["symbol_pool"][0])
        if sheet in ["fina_indicator"]:
            fields_with_dt = fields + ["market_code", "ann_date", "report_period"]
        else:
            fields_with_dt = fields + [
                "market_code",
                "actual_ann_date",
                "reporting_period",
                "statement_type",
            ]
        data = self.oq_sdk(
            sheet,
            **dict(
                market_code=params["market_code"],
                start_time=params["start_time"],
                end_time=params["end_time"],
                fields=fields_with_dt,
            ),
        )
        if sheet not in ["fina_indicator"]:
            data = data[data.statement_type.isin(["1", "4", "5"])]  # 合并报表
        remain_cols = list(set(fields_with_dt) - set(data.columns))
        if len(remain_cols) > 0:
            raise (DataSDKError(f"字段错误: {remain_cols}"))
        data = data.rename(
            columns={
                "reporting_period": "report_dt",
                "report_period": "report_dt",
                "market_code": "code",
                "ann_date": "actual_ann_date",
            }
        )
        data["actual_ann_date"] = pd.to_datetime(data["actual_ann_date"])
        data["report_dt"] = pd.to_datetime(data["report_dt"])
        data = data.sort_values(by=["actual_ann_date", "report_dt", "code"])
        return data

    def findata_process(
        self,
        sheet,
        data,
        fields,
        real_fields,
        variable_type,
        n_periods=9,
        pad_width=4,
        **params,
    ):
        base_cols = ["code", "actual_ann_date", "report_dt"]
        trade_cal = self.get_calendar(
            **dict(start_time=params["start_time"], end_time=params["end_time"])
        )
        data_start_dt = params["start_time"][:10]
        data_end_dt = params["end_time"][:10]
        all_factor_data = pd.DataFrame()
        stk_codes = list(set(data.code.values))
        for col in real_fields:
            one_factor_data = data[base_cols + [col]]
            one_factor_data = one_factor_data.dropna(how="any")
            if len(one_factor_data) == 0:
                raise (DataSDKError(f"{col}无数据"))
            one_factor_data = clean_financial_item(
                one_factor_data, col, variable_type, n_periods, data_start_dt, pad_width
            )

            one_factor_data["report_dt"] = pd.to_datetime(one_factor_data["report_dt"])
            one_factor_data["actual_ann_date"] = pd.to_datetime(
                one_factor_data["actual_ann_date"]
            )
            one_factor_data = one_factor_data.drop_duplicates(
                subset=["code", "actual_ann_date"], keep="last"
            )
            one_factor_data = one_factor_data.set_index(["code", "actual_ann_date"])
            one_factor_data.index.names = ("code", "dt")

            all_dates = (
                pd.DataFrame(
                    {stk: True for stk in stk_codes},
                    index=pd.date_range("2015-01-01", f"{data_end_dt}"),
                )
                .stack()
                .to_frame()
                .swaplevel()
                .sort_index()
            )

            all_dates.index.names = ("code", "dt")
            one_factor_data = pd.merge(
                all_dates,
                one_factor_data,
                left_index=True,
                right_index=True,
                how="left",
            )
            one_factor_data = one_factor_data.groupby(level=0).ffill()
            one_factor_data = one_factor_data.drop(columns={0})
            one_factor_data = one_factor_data.dropna(how="all")
            one_factor_data = one_factor_data.reset_index()
            one_factor_data = one_factor_data[
                one_factor_data["dt"].isin(trade_cal.index.values)
            ].reset_index(drop=True)
            if len(all_factor_data.columns) == 0:
                all_factor_data = one_factor_data
            else:
                all_factor_data = pd.merge(
                    all_factor_data,
                    one_factor_data,
                    on=["code", "dt", "report_dt"],
                    how="outer",
                )
        # return all_factor_data
        return all_factor_data[
            [
                "code",
                "dt",
            ]
            + list(fields.keys())
        ]

    def get_fina_indicator(self, fields, **params):
        real_fields = self.gen_real_cols(fields)
        data = self.get_findata("fina_indicator", real_fields, **params)
        all_factor_data = self.findata_process(
            "fina_indicator", data, fields, real_fields, "process", **params
        )
        return all_factor_data

    def get_cashflow(self, fields, **params):
        real_fields = self.gen_real_cols(fields)
        data = self.get_findata("cashflow", real_fields, **params)
        all_factor_data = self.findata_process(
            "cashflow", data, fields, real_fields, "process", **params
        )
        return all_factor_data

    def get_balancesheet(self, fields, **params):
        real_fields = self.gen_real_cols(fields)
        data = self.get_findata("balancesheet", real_fields, **params)
        all_factor_data = self.findata_process(
            "balancesheet", data, fields, real_fields, "state", **params
        )
        return all_factor_data

    def get_income(self, fields, **params):
        real_fields = self.gen_real_cols(fields)
        data = self.get_findata("income", real_fields, **params)
        all_factor_data = self.findata_process(
            "income", data, fields, real_fields, "process", **params
        )
        return all_factor_data

    def gen_real_cols(self, fields):
        new_fields = set()
        for field in fields:
            is_suffix, new_name = self.check_dt_suffix(field)
            if is_suffix:
                new_fields.add(new_name)
            else:
                new_fields.add(field)
        return list(new_fields)

    def check_dt_suffix(self, colname):
        target = r"(_\dq)$"
        match = re.search(target, colname)
        if match:
            ori_colname = colname.replace(match.group(1), "")
            return True, ori_colname
        else:
            return False, colname

    def get_cashflow_factor(self, fields, **params):
        data = get_processed_financial_data(
            params["market_code"],
            params["start_time"],
            params["end_time"],
            "cashflow",
            fields,
        )
        return data[fields]

    def get_balancesheet_factor(self, fields, **params):
        data = get_processed_financial_data(
            params["market_code"],
            params["start_time"],
            params["end_time"],
            "balancesheet",
            fields,
        )
        return data[fields]

    def get_income_factor(self, fields, **params):
        data = get_processed_financial_data(
            params["market_code"],
            params["start_time"],
            params["end_time"],
            "income",
            fields,
        )
        return data[fields]

    def get_derivind_factor(self, fields, **params):
        params["fields"] = ["trade_date", "market_code"] + list(fields.values())
        if "frequency" in params:
            del params["frequency"]
        data = self.oq_sdk("derivind_factor", **params)
        data["trade_date"] = pd.to_datetime(data["trade_date"], format="%Y%m%d")
        data = data.rename(
            columns={
                "market_code": "code",
                "trade_date": "dt",
            }
        )
        return data

    def get_factor_rows_by_stks(self, **params):
        stks_df = self.get_index_stks_his(
            params["symbol_pool"][0], 
            params['start_time'], 
            params['end_time']
        )
        factor = self.get_factor_rows(**params)
        factor["date_s"] = factor['date'].dt.date
        date_list = list(set(factor['date_s']))
        date_list.sort()
        conn_by_date = []
        for dd in date_list:
            dt = dd.strftime("%Y%m%d")
            today_con = stks_df[
                (stks_df.con_indate<=str(dt)) & (
                    (stks_df.con_outdate.isna()) | (stks_df.con_outdate>=str(dt))
            )]
            conn_by_date.append(pd.DataFrame({
                'asset': today_con.con_code,
                'date_s': dd
            }))
        conn_by_date = pd.concat(conn_by_date)
        factor = pd.merge(factor, conn_by_date, on=['asset', 'date_s']).drop(columns=['date_s'])
        return factor

    def get_factor_rows(self, **params):
        if params["factor_name"].startswith("cgs."):
            params["market_code"] = self.get_index_stk_codes(params["symbol_pool"][0])
            params["symbol_pool"] = []
        elif params["factor_name"].startswith("public.") and self.username!="public":
            stks_df = self.get_index_stks_his(
                params["symbol_pool"][0],
                params['start_time'],
                params['end_time']
            )
            params["market_code"] = list(set(stks_df.con_code.values))
            params["symbol_pool"] = ["000985.SH"]
        #data = self.oq_sdk("get_factor", **params)
        data = self.oq_sdk("get_factor_by_date", **params)
        if params["factor_name"].startswith("cgs."):
            data["name"] = params["factor_name"]
        data["data_time"] = pd.to_datetime(
            data["data_time"], format="%Y-%m-%d %H:%M:%S.%f"
        )
        data = data.rename(
            columns={
                "security_code": "asset",
                "data_time": "date",
                "value": "factor",
            }
        )
        return data

    def get_factor(self, fields, **params):
        if "factor_name" not in params:
            fname = list(fields.values())[0]
            params["factor_name"] = fname
        if params["factor_name"].startswith("cgs."):
            params["market_code"] = self.get_index_stk_codes(params["symbol_pool"][0])
            params["symbol_pool"] = []
        data = self.oq_sdk("get_factor", **params)
        if params["factor_name"].startswith("cgs."):
            data["name"] = params["factor_name"]
        data["data_time"] = pd.to_datetime(
            data["data_time"], format="%Y-%m-%d %H:%M:%S.%f"
        )
        data = data.rename(columns={"security_code": "code", "data_time": "dt"})
        data = data.pivot(
            index=["dt", "code"], columns=["name"], values="value"
        ).reset_index()
        return data

    def get_kline(self, fields, **params):
        # params["fields"] = ["orig_time", "symbol"] + list(fields.values())
        # params.update(dict(limit=100000000))
        # params.update(dict(adj='hfq'))
        #data = self.oq_sdk("get_kline", **params)
        data = self.oq_sdk("get_kline_by_date", **params)
        data["orig_time"] = pd.to_datetime(
            data["orig_time"], format="%Y-%m-%d %H:%M:%S.%f"
        )
        data = data.rename(
            columns={
                "symbol": "code",
                "orig_time": "dt",
            }
        )
        if params.get("frequency", "1d") == "1d":
            data["dt"] = data['dt'].dt.normalize()
        return data

    def get_data(self, api_name, fields, **params):
        data = self.apis[api_name](fields, **params)
        col_change = {v: k for k, v in fields.items()}
        data = data.rename(columns=col_change)
        return data

    def get_calendar(self, **params):
        params = dict(
            market_code=["000300.SH"],
            frequency="1d",
            start_time=params["start_time"],
            end_time=params["end_time"],
            adj=None,
            variety='index',
        )
        df = self.get_kline({}, **params)
        df = df.set_index("dt")
        return df

    def get_industry_l1(self, stk_codes, batch=500):
        data = []
        for i in range(0, len(stk_codes), batch):
            data.append(self.oq_sdk("industry", market_code=stk_codes[i: i+batch]))
        data = pd.concat(data)
        return data[data.industries_type == 10][["market_code", "ind_name_l1"]]

    def get_index_stk_codes(self, index_code):
        index_stk_df = self.get_index_stks(index_code)
        stk_codes = [row["con_code"] for idx, row in index_stk_df.iterrows()]
        return stk_codes

    def get_index_stks(self, index_code):
        index_stk_df = self.oq_sdk("index_con", index_code=[index_code])
        return index_stk_df

    def get_index_stks_his(self, index_code, start_dt, end_dt):
        df = self.oq_sdk("index_con_his", index_code=[index_code], start_time=start_dt, end_time=end_dt)
        start_dt = "".join(start_dt.split("-"))
        end_dt = "".join(end_dt.split("-"))
        if 'con_outdate' not in df.columns:
            df['con_outdate'] = np.nan
        df['con_outdate'] = df['con_outdate'].astype(str)
        df = df[
            (df.con_indate <= end_dt)
            & ((df.con_outdate=='nan') | (df.con_outdate >= start_dt))
        ]
        return df

    def get_prices_data(self, index_code, start_time, end_time, freq='1d'):
        index_stk_df = self.get_index_stks_his(index_code, start_time, end_time)
        stk_codes =  list({row["con_code"] for idx, row in index_stk_df.iterrows()})
        params = dict(
            market_code=stk_codes,
            frequency=freq,
            start_time=start_time,
            end_time=end_time,
        )
        dfs = self.get_data(
            "QueryKline",
            {
                "close": "close_price",
            },
            **params,
        )
        return dfs


def test():
    od = OqData()
    api2fields = {"QueryKline": {"close": "closePrice"}}
    api = "QueryKline"
    codes = ["000001.SZ"]
    freq = "1d"
    start_date = "2021-07-01"
    end_date = "2024-08-01"
    params = dict(
        symbol_pool=["000905.SH"],
        start_time=f"{start_date} 08:00:00",
        end_time=f"{end_date} 08:00:00",
    )
    params.update(dict(freq='1d'), factor_name='public.6日ATR')
    df = od.get_factor_rows_by_stks(**params)
    print(df)


if __name__ == "__main__":
    test()
