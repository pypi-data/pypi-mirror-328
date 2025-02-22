# -*- coding: utf-8 -*-
# 版权所有 2019 深圳米筐科技有限公司（下称“米筐科技”）
#
# 除非遵守当前许可，否则不得使用本软件。
#
#     * 非商业用途（非商业用途指个人出于非商业目的使用本软件，或者高校、研究所等非营利机构出于教育、科研等目的使用本软件）：
#         遵守 Apache License 2.0（下称“Apache 2.0 许可”），您可以在以下位置获得 Apache 2.0 许可的副本：
#         http://www.apache.org/licenses/LICENSE-2.0。
#         除非法律有要求或以书面形式达成协议，否则本软件分发时需保持当前许可“原样”不变，且不得附加任何条件。
#
#     * 商业用途（商业用途指个人出于任何商业目的使用本软件，或者法人或其他组织出于任何目的使用本软件）：
#         未经米筐科技授权，任何个人不得出于任何商业目的使用本软件（包括但不限于向第三方提供、销售、出租、出借、转让本软件、本软件的衍生产品、引用或借鉴了本软件功能或源代码的产品或服务），任何法人或其他组织不得出于任何目的使用本软件，否则米筐科技有权追究相应的知识产权侵权责任。
#         在此前提下，对本软件的使用同样需要遵守 Apache 2.0 许可，Apache 2.0 许可与本许可冲突之处，以本许可为准。
#         详细的授权流程，请联系 public@ricequant.com 获取。
import datetime
import json
import os
import pickle
import re
from itertools import chain
from typing import Callable, Optional, Union, List
from filelock import FileLock, Timeout
import multiprocessing
from multiprocessing.sharedctypes import Synchronized
from ctypes import c_bool

import h5py
import numpy as np
from deepquant.quest.apis.api_yhdatac import yhdatac
from deepquant.quest.utils.concurrent import ProgressedProcessPoolExecutor, ProgressedTask
from deepquant.quest.utils.datetime_func import convert_date_to_date_int, convert_date_to_int, convert_dt_to_date_str, convert_int_to_date_str
from deepquant.quest.utils.i18n import gettext as _
from deepquant.quest.utils.functools import lru_cache
from deepquant.quest.utils.logger import init_logger, system_log
from deepquant.quest.environment import Environment
from deepquant.quest.model.instrument import Instrument


START_DATE = 20050104
END_DATE = 29991231


def gen_instruments(d):
    stocks = sorted(list(yhdatac.all_instruments().market_code))
    instruments = [i.__dict__ for i in yhdatac.instruments(stocks)]
    with open(os.path.join(d, 'instruments.pk'), 'wb') as out:
        pickle.dump(instruments, out, protocol=2)


def gen_yield_curve(d):
    yield_curve = yhdatac.get_yield_curve(start_date=START_DATE, end_date=datetime.date.today())
    yield_curve.index = [convert_date_to_date_int(d) for d in yield_curve.index]
    yield_curve.index.name = 'date'
    with h5py.File(os.path.join(d, 'yield_curve.h5'), 'w') as f:
        f.create_dataset('data', data=yield_curve.to_records())


def gen_trading_dates(d):
    dates = yhdatac.get_trading_dates(start_date=START_DATE, end_date='2999-01-01')
    dates = np.array([convert_date_to_date_int(d) for d in dates])
    np.save(os.path.join(d, 'trading_dates.npy'), dates, allow_pickle=False)


def gen_st_days(d):
    from deepquant.quest.datac.client import get_client
    stocks = yhdatac.all_instruments('stock').market_code.tolist()
    # st_days = get_client().execute('get_st_days', stocks, START_DATE,
    #                                convert_date_to_date_int(datetime.date.today()))
    st_days = yhdatac.get_st_days(stocks, '1990-01-01', '2999-01-01')
    with h5py.File(os.path.join(d, 'st_stock_days.h5'), 'w') as h5:
        # for market_code, days in st_days.items():
        #     h5[market_code] = days
        for market_code in stocks:
            ds = st_days.loc[st_days['market_code'] == market_code]
            ds['trade_days'] = ds['trade_days'].astype('int64')
            ds['trade_days'] = ds['trade_days'] * 1000000
            ds.sort_values(by='trade_days', ascending=False)
            ds = ds.select_dtypes(exclude=['object'])
            h5[market_code] = ds.to_records(index=False)


def gen_suspended_days(d):
    stocks = yhdatac.all_instruments('stock').market_code.tolist()
    suspended_days = yhdatac.get_suspend_days(stocks, convert_int_to_date_str(START_DATE),
                                          convert_dt_to_date_str(datetime.date.today()))
    with h5py.File(os.path.join(d, 'suspended_days.h5'), 'w') as h5:
        for market_code, days in suspended_days.items():
            h5[market_code] = days


def gen_dividends(d):
    stocks = yhdatac.all_instruments().market_code.tolist()
    dividend = yhdatac.get_dividend(stocks)
    need_cols = ["dividend_cash_before_tax", "book_closure_date", "ex_dividend_date", "payable_date", "round_lot"]
    dividend = dividend[need_cols]
    dividend.reset_index(inplace=True)
    dividend.rename(columns={'declaration_announcement_date': 'announcement_date'}, inplace=True)
    for f in ('book_closure_date', 'ex_dividend_date', 'payable_date', 'announcement_date'):
        dividend[f] = [convert_date_to_date_int(d) for d in dividend[f]]
    dividend.set_index(['market_code', 'book_closure_date'], inplace=True)
    with h5py.File(os.path.join(d, 'dividends.h5'), 'w') as h5:
        for market_code in dividend.index.levels[0]:
            h5[market_code] = dividend.loc[market_code].to_records()


def gen_splits(d):
    stocks = yhdatac.all_instruments().market_code.tolist()
    # split = yhdatac.get_split(stocks)
    split = yhdatac.get_split(stocks, '1990-01-01', '2999-01-01')
    # split['split_factor'] = split['split_coefficient_to'] / split['split_coefficient_from']
    # split = split[['split_factor']]
    # split.reset_index(inplace=True)
    # split.rename(columns={'ex_dividend_date': 'ex_date'}, inplace=True)
    # split['ex_date'] = [convert_date_to_int(d) for d in split['ex_date']]
    # split.set_index(['market_code', 'ex_date'], inplace=True)
    split.rename(columns={'split': 'split_factor'}, inplace=True)
    with h5py.File(os.path.join(d, 'split_factor.h5'), 'w') as h5:
        # for market_code in split.index.levels[0]:
        #     h5[market_code] = split.loc[market_code].to_records()
        for market_code in stocks:
            ds = split.loc[split['market_code'] == market_code]
            ds['ex_date'] = ds['ex_date'].astype('int64')
            ds['ex_date'] = ds['ex_date'] * 1000000
            ds.sort_values(by='ex_date', ascending=False)
            ds = ds.select_dtypes(exclude=['object'])
            h5[market_code] = ds.to_records(index=False)


def gen_ex_factor(d):
    stocks = yhdatac.all_instruments().market_code.tolist()
    ex_factor = yhdatac.get_ex_factor(stocks)
    ex_factor.reset_index(inplace=True)
    ex_factor['ex_date'] = [convert_date_to_int(d) for d in ex_factor['ex_date']]
    ex_factor.rename(columns={'ex_date': 'start_date'}, inplace=True)
    ex_factor.set_index(['market_code', 'start_date'], inplace=True)
    ex_factor = ex_factor[['ex_cum_factor']]

    dtype = ex_factor.loc[ex_factor.index.levels[0][0]].to_records().dtype
    initial = np.empty((1,), dtype=dtype)
    initial['start_date'] = 0
    initial['ex_cum_factor'] = 1.0

    with h5py.File(os.path.join(d, 'ex_cum_factor.h5'), 'w') as h5:
        for market_code in ex_factor.index.levels[0]:
            h5[market_code] = np.concatenate([initial, ex_factor.loc[market_code].to_records()])


def gen_share_transformation(d):
    df = yhdatac.get_share_transformation()
    df.drop_duplicates("predecessor", inplace=True)
    df.set_index('predecessor', inplace=True)
    df.effective_date = df.effective_date.astype(str)
    df.predecessor_delisted_date = df.predecessor_delisted_date.astype(str)

    json_file = os.path.join(d, 'share_transformation.json')
    with open(json_file, 'w') as f:
        f.write(df.to_json(orient='index'))


def gen_future_info(d):
    future_info_file = os.path.join(d, 'future_info.json')

    def _need_to_recreate():
        if not os.path.exists(future_info_file):
            return
        else:
            with open(future_info_file, "r") as f:
                all_futures_info = json.load(f)
                if "margin_rate" not in all_futures_info[0]:
                    return True
    
    def update_margin_rate(file):
        all_instruments_data = yhdatac.all_instruments("Future")
        with open(file, "r") as f:
            all_futures_info = json.load(f)
            new_all_futures_info = []
            for future_info in all_futures_info:
                if "market_code" in future_info:
                    future_info["margin_rate"] = all_instruments_data[all_instruments_data["market_code"] == future_info["market_code"]].iloc[0].margin_rate
                elif "underlying_symbol" in future_info:
                    dominant = yhdatac.futures.get_dominant(future_info["underlying_symbol"])[-1]
                    future_info["margin_rate"] = all_instruments_data[all_instruments_data["market_code"] == dominant].iloc[0].margin_rate
                new_all_futures_info.append(future_info)
        os.remove(file)
        with open(file, "w") as f:
            json.dump(new_all_futures_info, f, separators=(',', ':'), indent=2)

    if (_need_to_recreate()): update_margin_rate(future_info_file)

    # 新增 hard_code 的种类时，需要同时修改deepquant.quest.data.base_data_source.storages.FutureInfoStore.data_compatible中的内容
    hard_code = [
        {'underlying_symbol': 'TC',
          'close_commission_ratio': 4.0,
          'close_commission_today_ratio': 0.0,
          'commission_type': "by_volume",
          'open_commission_ratio': 4.0,
          'margin_rate': 0.05,
          'tick_size': 0.2},
         {'underlying_symbol': 'ER',
          'close_commission_ratio': 2.5,
          'close_commission_today_ratio': 2.5,
          'commission_type': "by_volume",
          'open_commission_ratio': 2.5,
          'margin_rate': 0.05,
          'tick_size': 1.0},
         {'underlying_symbol': 'WS',
          'close_commission_ratio': 2.5,
          'close_commission_today_ratio': 0.0,
          'commission_type': "by_volume",
          'open_commission_ratio': 2.5,
          'margin_rate': 0.05,
          'tick_size': 1.0},
         {'underlying_symbol': 'RO',
          'close_commission_ratio': 2.5,
          'close_commission_today_ratio': 0.0,
          'commission_type': "by_volume",
          'open_commission_ratio': 2.5,
          'margin_rate': 0.05,
          'tick_size': 2.0},
         {'underlying_symbol': 'ME',
          'close_commission_ratio': 1.4,
          'close_commission_today_ratio': 0.0,
          'commission_type': "by_volume",
          'open_commission_ratio': 1.4,
          'margin_rate': 0.06,
          'tick_size': 1.0},
        {'underlying_symbol': 'WT',
         'close_commission_ratio': 5.0,
         'close_commission_today_ratio': 5.0,
         'commission_type': "by_volume",
         'open_commission_ratio': 5.0,
         'margin_rate': 0.05,
         'tick_size': 1.0},
    ]

    if not os.path.exists(future_info_file):
        all_futures_info = hard_code
    else:
        with open(future_info_file, 'r') as f:
            all_futures_info = json.load(f)

    future_list = []
    symbol_list = []
    param = ['close_commission_ratio', 'close_commission_today_ratio', 'commission_type', 'open_commission_ratio']

    for i in all_futures_info:
        if i.get('market_code'):
            future_list.append(i.get('market_code'))
        else:
            symbol_list.append(i.get('underlying_symbol'))

    # 当修改了hard_code以后，避免用户需要手动删除future_info.json文件
    for info in hard_code:
        if info["underlying_symbol"] not in symbol_list:
            all_futures_info.append(info)
            symbol_list.append(info["underlying_symbol"])

    futures_market_code = yhdatac.all_instruments(type='Future')['market_code'].unique()
    commission_df = yhdatac.futures.get_commission_margin()
    for future in futures_market_code:
        underlying_symbol = re.match(r'^[a-zA-Z]*', future).group()
        if future in future_list:
            continue
        future_dict = {}
        commission = commission_df[commission_df['market_code'] == future]
        if not commission.empty:
            future_dict['market_code'] = future
            commission = commission.iloc[0]
            for p in param:
                future_dict[p] = commission[p]
            instruemnts_data = yhdatac.instruments(future)
            future_dict['margin_rate'] = instruemnts_data.margin_rate
            future_dict['tick_size'] = instruemnts_data.tick_size()
        elif underlying_symbol in symbol_list:
            continue
        else:
            symbol_list.append(underlying_symbol)
            future_dict['underlying_symbol'] = underlying_symbol
            try:
                dominant = yhdatac.futures.get_dominant(underlying_symbol).iloc[-1]
            except AttributeError:
                # FIXME: why get_dominant return None???
                continue
            commission = commission_df[commission_df['market_code'] == dominant].iloc[0]

            for p in param:
                future_dict[p] = commission[p]
            instruemnts_data = yhdatac.instruments(dominant)
            future_dict['margin_rate'] = instruemnts_data.margin_rate
            future_dict['tick_size'] = instruemnts_data.tick_size()
        all_futures_info.append(future_dict)

    with open(os.path.join(d, 'future_info.json'), 'w') as f:
        json.dump(all_futures_info, f, separators=(',', ':'), indent=2)


class GenerateFileTask(ProgressedTask):
    def __init__(self, func):
        self._func = func
        self._step = 100

    @property
    def total_steps(self):
        # type: () -> int
        return self._step

    def __call__(self, *args, **kwargs):
        self._func(*args, **kwargs)
        yield self._step


STOCK_FIELDS = ['open_price', 'close_price', 'high_price', 'low_price', 'pre_close', 'high_limited', 'low_limited', 'volume', 'total_turnover']
INDEX_FIELDS = ['open_price', 'close_price', 'high_price', 'low_price', 'pre_close', 'volume', 'total_turnover']
FUTURES_FIELDS = STOCK_FIELDS + ['settlement', 'prev_settlement', 'open_interest']
FUND_FIELDS = STOCK_FIELDS


class DayBarTask(ProgressedTask):
    def __init__(self, market_code):
        self._market_code = market_code

    @property
    def total_steps(self):
        # type: () -> int
        return len(self._market_code)

    def __call__(self, path, fields, **kwargs):
        raise NotImplementedError


class GenerateDayBarTask(DayBarTask):
    def __call__(self, path, fields, **kwargs):
        try:
            h5 = h5py.File(path, "w")
        except OSError:
            system_log.error("File {} update failed, if it is using, please update later, "
                            "or you can delete then update again".format(path))
            sval.value = False
            yield 1
        else:
            with h5:
                i, step = 0, 300
                while True:
                    market_code = self._market_code[i:i + step]
                    df = yhdatac.get_price(market_code, START_DATE, datetime.date.today(), '1d',
                                        adjust_type='none', fields=fields, expect_df=True)
                    if not (df is None or df.empty):
                        df.reset_index(inplace=True)
                        df['datetime'] = [convert_date_to_int(d) for d in df['date']]
                        del df['date']
                        df.set_index(['market_code', 'datetime'], inplace=True)
                        df.sort_index(inplace=True)
                        for market_code in df.index.levels[0]:
                            h5.create_dataset(market_code, data=df.loc[market_code].to_records(), **kwargs)
                    i += step
                    yield len(market_code)
                    if i >= len(self._market_code):
                        break


class UpdateDayBarTask(DayBarTask):
    def h5_has_valid_fields(self, h5, wanted_fields):
        obid_gen = (k for k in h5.keys())
        wanted_fields = set(wanted_fields)
        wanted_fields.add('datetime')
        try:
            h5_fields = set(h5[next(obid_gen)].dtype.fields.keys())
        except StopIteration:
            pass
        else:
            return h5_fields == wanted_fields
        return False

    def __call__(self, path, fields, **kwargs):
        need_recreate_h5 = False
        try:
            with h5py.File(path, 'r') as h5:
                need_recreate_h5 = not self.h5_has_valid_fields(h5, fields)
        except (OSError, RuntimeError):
            need_recreate_h5 = True
        if need_recreate_h5:
            yield from GenerateDayBarTask(self._market_code)(path, fields, **kwargs)
        else:
            h5 = None
            try:
                h5 = h5py.File(path, 'a')
            except OSError:
                system_log.error("File {} update failed, if it is using, please update later, "
                                "or you can delete then update again".format(path))
                sval.value = False
                yield 1
            else:
                is_futures = "futures" == os.path.basename(path).split(".")[0]
                for market_code in self._market_code:
                    # 特殊处理前复权合约，需要全量更新
                    is_pre = is_futures and "888" in market_code
                    if market_code in h5 and not is_pre:
                        try:
                            last_date = int(h5[market_code]['datetime'][-1] // 1000000)
                        except OSError:
                            system_log.error("File {} update failed, if it is using, please update later, "
                                            "or you can delete then update again".format(path))
                            sval.value = False
                            yield 1
                            break
                        except ValueError:
                            h5.pop(market_code)
                            start_date = START_DATE
                        else:
                            start_date = yhdatac.get_next_trading_date(last_date)
                    else:
                        start_date = START_DATE
                    df = yhdatac.get_price(market_code, start_date, END_DATE, '1d',
                                        adjust_type='none', fields=fields, expect_df=True)
                    if not (df is None or df.empty):
                        df = df[fields]  # Future market_code like SC888 will auto add 'dominant_id'
                        df = df.loc[market_code]
                        df.reset_index(inplace=True)
                        df['datetime'] = [convert_date_to_int(d) for d in df['date']]
                        del df['date']
                        df.set_index('datetime', inplace=True)
                        if market_code in h5:
                            data = np.array(
                                [tuple(i) for i in chain(h5[market_code][:], df.to_records())],
                                dtype=h5[market_code].dtype
                            )
                            del h5[market_code]
                            h5.create_dataset(market_code, data=data, **kwargs)
                        else:
                            h5.create_dataset(market_code, data=df.to_records(), **kwargs)
                    yield 1
            finally:
                if h5:
                    h5.close()


def process_init(args: Optional[Synchronized] = None):
    import warnings
    #with warnings.catch_warnings(record=True):
        # catch warning: yhdatac is already inited. Settings will be changed
        #yhdatac.init()
    init_logger()
    # Initialize process shared variables
    if args:
        global sval
        sval = args


def update_bundle(path, create, enable_compression=False, concurrency=1):
    if create:
        _DayBarTask = GenerateDayBarTask
    else:
        _DayBarTask = UpdateDayBarTask

    init_logger()
    kwargs = {}
    if enable_compression:
        kwargs['compression'] = 9


    day_bar_args = (
        ("stocks.h5", yhdatac.all_instruments('stock').market_code.tolist(), STOCK_FIELDS),
        ("indexes.h5", yhdatac.all_instruments('INDX').market_code.tolist(), INDEX_FIELDS),
        ("futures.h5", yhdatac.all_instruments('Future').market_code.tolist(), FUTURES_FIELDS),
        ("funds.h5", yhdatac.all_instruments('FUND').market_code.tolist(), FUND_FIELDS),
    )
    
    yhdatac.reset()

    gen_file_funcs = (
        gen_instruments, gen_trading_dates, gen_dividends, gen_splits, gen_ex_factor, gen_st_days,
        gen_suspended_days, gen_yield_curve, gen_share_transformation, gen_future_info
    )
    '''
    day_bar_args = ()

    gen_file_funcs = (
        gen_trading_dates,
    )
    '''
    succeed = multiprocessing.Value(c_bool, True)
    with ProgressedProcessPoolExecutor(
            max_workers=concurrency, initializer=process_init, initargs=(succeed, )
    ) as executor:
        # windows上子进程需要执行yhdatac.init, 其他os则需要执行yhdatac.reset; yhdatac.init包含了yhdatac.reset的功能
        for func in gen_file_funcs:
            executor.submit(GenerateFileTask(func), path)
        for file, market_code, field in day_bar_args:
            executor.submit(_DayBarTask(market_code), os.path.join(path, file), field, **kwargs)
    return succeed.value


class AutomaticUpdateBundle(object):
    def __init__(self, path: str, filename: str, api: Callable, fields: List[str], end_date: datetime.date, start_date: Union[int, datetime.date] = START_DATE) -> None:
        if not os.path.exists(path):
            os.makedirs(path)
        self._file = os.path.join(path, filename)
        self._trading_dates = None
        self._filename = filename
        self._api = api
        self._fields = fields
        self._start_date = start_date
        self._end_date = end_date
        self.updated = []
        self._env = Environment.get_instance()
        self._file_lock = FileLock(self._file + ".lock")

    def get_data(self, instrument: Instrument, dt: datetime.date) -> Optional[np.ndarray]:
        dt = convert_date_to_date_int(dt)
        data = self._get_data_all_time(instrument)
        if data is None:
            return data
        else:
            try:
                data = data[np.searchsorted(data['trading_dt'], dt)]
            except IndexError:
                data = None
            return data

    @lru_cache(128)
    def _get_data_all_time(self, instrument: Instrument) -> Optional[np.ndarray]:
        if instrument.market_code not in self.updated:
            self._auto_update_task(instrument)
            self.updated.append(instrument.market_code)
        with h5py.File(self._file, "r") as h5:
            data = h5[instrument.market_code][:]
            if len(data) == 0:
                return None
        return data
    
    def _auto_update_task(self, instrument: Instrument) -> None:
        """
        在 yhalpha 策略运行过程中自动更新所需的日线数据

        :param instrument: 合约对象
        :type instrument: `Instrument`
        """
        market_code = instrument.market_code
        start_date = self._start_date
        try:
            with self._file_lock.acquire():
                h5 = h5py.File(self._file, "a")
                if market_code in h5 and h5[market_code].dtype.names:
                    if 'trading_dt' in h5[market_code].dtype.names:
                        # 需要兼容此前的旧版数据，对字段名进行更新
                        if len(h5[market_code][:]) != 0:
                            last_date = datetime.datetime.strptime(str(h5[market_code][-1]['trading_dt']), "%Y%m%d").date()
                            if last_date >= self._end_date:
                                return
                            start_date = self._env.data_proxy._data_source.get_next_trading_date(last_date).date()
                            if start_date > self._end_date:
                                return
                    else:
                        del h5[market_code]
                
                arr = self._get_array(instrument, start_date)
                if arr is None:
                    if market_code not in h5:
                        arr = np.array([])
                        h5.create_dataset(market_code, data=arr)
                else:
                    if market_code in h5:
                        data = np.array(
                            [tuple(i) for i in chain(h5[market_code][:], arr)],
                            dtype=h5[market_code].dtype)
                        del h5[market_code]
                        h5.create_dataset(market_code, data=data)
                    else:
                        h5.create_dataset(market_code, data=arr)
        except (OSError, Timeout) as e:
            raise OSError(_("File {} update failed, if it is using, please update later, "
                          "or you can delete then update again".format(self._file))) from e
        finally:
            h5.close()
    
    def _get_array(self, instrument: Instrument, start_date: datetime.date) -> Optional[np.ndarray]:
        df = self._api(instrument.market_code, start_date, self._end_date, self._fields)
        if not (df is None or df.empty):
            df = df[self._fields].loc[instrument.market_code] # yhdatac.get_open_auction_info get Futures's data will auto add 'open_interest' and 'prev_settlement'
            record = df.iloc[0: 1].to_records()
            dtype = [('trading_dt', 'int')]
            for field in self._fields:
                dtype.append((field, record.dtype[field]))
            trading_dt = self._env.data_proxy._data_source.batch_get_trading_date(df.index)
            trading_dt = convert_date_to_date_int(trading_dt)
            arr = np.ones((trading_dt.shape[0], ), dtype=dtype)
            arr['trading_dt'] = trading_dt
            for field in self._fields:
                arr[field] = df[field].values
            return arr
        return None
