import os
import glob
import tarfile
import tempfile
from itertools import chain
from reprlib import repr
from typing import List, Optional, Collection
from tqdm import tqdm
import click
import h5py
import hdf5plugin  # noqa
import numpy as np
import requests
import deepquant.quest.datac as yhdatac
import multiprocessing
from ctypes import c_bool
import sys

from deepquant.quest.cmds.bundle import download
from deepquant.quest.const import INSTRUMENT_TYPE
from deepquant.quest.data.bundle import ProgressedProcessPoolExecutor, update_bundle as update_daybar, process_init
from deepquant.quest.utils.datetime_func import convert_dt_to_int, datetime
from deepquant.quest.utils.logger import system_log
from deepquant.quest.mod.mod_quant_data.data_sources.data_store import H5TicksLoader, date_to_number, time_to_number

from deepquant.quest.alpha.utils.scripts import get_h5_mode
from deepquant.quest.alpha.utils import blosc_opts


EQUITIES_DTYPE = np.dtype([
    ('datetime', '<i8'),
    ('open', '<f8'),
    ('high', '<f8'),
    ('low', '<f8'),
    ('close', '<f8'),
    ('volume', '<f8'),
    ('total_turnover', '<f8')
])

DERIVATIVES_DTYPE = np.dtype([
    ('datetime', '<i8'),
    ('open', '<f8'),
    ('high', '<f8'),
    ('low', '<f8'),
    ('close', '<f8'),
    ('open_interest', '<i8'),
    ('volume', '<f8'),
    ('total_turnover', '<f8')
])

INDEX_DTYPE = np.dtype([
    ('date', '<i4'),
    ('line_no', '<u4'),
])

TAG_MAP = {
    "stock": (INSTRUMENT_TYPE.CS,),
    "futures": (INSTRUMENT_TYPE.FUTURE,),
    "fund": (INSTRUMENT_TYPE.ETF, INSTRUMENT_TYPE.LOF, INSTRUMENT_TYPE.INDX),
    "index": (INSTRUMENT_TYPE.INDX,),
    "option": (INSTRUMENT_TYPE.OPTION,),
    "convertible": (INSTRUMENT_TYPE.CONVERTIBLE,),
}

EQUITIES_INS_TYPE = [
    INSTRUMENT_TYPE.CS,
    INSTRUMENT_TYPE.ETF,
    INSTRUMENT_TYPE.LOF,
    INSTRUMENT_TYPE.INDX,
    INSTRUMENT_TYPE.CONVERTIBLE
]

MIN_START_DATE = 20050104
MAX_END_DATE = 29991231

REBUILD_COMFIRM_RETRY_TIMES = 3


def _merge_tags(tags, with_derivatives):
    tags = set(tags)
    df = yhdatac.all_instruments()
    option_df = yhdatac.all_instruments(INSTRUMENT_TYPE.OPTION)
    future_df = yhdatac.all_instruments(INSTRUMENT_TYPE.FUTURE)
    convertible_df = yhdatac.all_instruments(INSTRUMENT_TYPE.CONVERTIBLE)

    market_code_set = set()
    if "all" in tags:
        ins_types = list(chain(*TAG_MAP.values()))
        tags.remove("all")
    else:
        ins_types = list(chain(*(TAG_MAP[t] for t in tags if t in TAG_MAP)))

    for t in TAG_MAP.keys():
        tags.discard(t)

    underlying_symbol_df = future_df[future_df.underlying_symbol.isin(tags)]
    tags.update(underlying_symbol_df.market_code.to_list())
    [tags.remove(i) for i in set(underlying_symbol_df.underlying_symbol.to_list())]

    market_code_set.update(df[df.type.isin(ins_types)].market_code.to_list())
    market_code_set.update(df[df.market_code.isin(tags)].market_code.to_list())
    market_code_set.update(option_df[option_df.market_code.isin(tags)].underlying_market_code.to_list())
    tags = tags.difference(market_code_set)

    if with_derivatives:
        future_derivatives = future_df[future_df.underlying_market_code.isin(market_code_set)]
        market_code_set.update(future_derivatives.market_code.to_list())
        option_derivatives = option_df[option_df.underlying_market_code.isin(market_code_set)]
        market_code_set.update(option_derivatives.market_code.to_list())

    # convertible_instruments
    convertible_id_df = convertible_df[convertible_df.market_code.isin(market_code_set)]
    if convertible_id_df is not None and not convertible_id_df.empty:
        con_ins = yhdatac.convertible.instruments(convertible_id_df.market_code)
        if con_ins is not None:
            stock_code = [i.stock_code for i in con_ins] if isinstance(con_ins, list) else [con_ins.stock_code]
            market_code_set.update(stock_code)

    if tags:
        click.echo("不支持的参数值:[{}]，\n可选的参数值有 [{}] 或 underlying_symbol 或 market_code".
                   format(", ".join(tags), ", ".join(TAG_MAP.keys())))

    return market_code_set


def check_min_bar_data(data_bundle_path):
    # 检查分钟数据
    min_file_path_list = glob.glob(os.path.join(data_bundle_path, "bundle", "h5", "*", "*.h5"))

    if len(min_file_path_list) == 0:
        click.echo("当前目录下不存在分钟数据!")
        return
    else:
        click.echo("共有{}个分钟数据文件!".format(len(min_file_path_list)))

    # 数据异常的文件
    error_file_path_list = []
    for min_file_path in tqdm(min_file_path_list):
        with h5py.File(min_file_path, 'r') as h5:
            try:
                if "index" not in h5.keys():
                    continue
                latest_date, latest_index = h5['index'][-1]
                # 数据最新日期
                data_date = h5["data"][-1][0] // 1000000
                # 上一个交易日，当索引大于数据长度时，数据有误，则设置一个最新日期用于舍弃
                data_len = len(h5["data"])
                last_date = h5["data"][latest_index - 1][0] // 1000000 if 0 < latest_index <= data_len else None
                last_date = latest_date if latest_index > data_len else last_date
                # index和data对应不上时舍弃
                if latest_date != data_date or (last_date and last_date >= latest_date):
                    error_file_path_list.append(min_file_path)
            except Exception as e:
                error_file_path_list.append(min_file_path)
    len_err = len(error_file_path_list)
    if len_err == 0:
        click.echo("\n检测完成：分钟数据质量良好！")
        return
    else:
        click.echo("\n检测完成：共有{}个标的分钟数据存在异常。".format(len_err))

    err_symbol_list = [os.path.basename(path).split(".h5")[0] for path in error_file_path_list]
    click.echo("数据异常标的如下:\n{}\n".format(err_symbol_list))

    is_ok = input("是否删除异常数据(yes/no):").lower()

    if is_ok in ["yes", "y"]:
        click.echo("\n准备删除异常数据！")
        for min_file_path in tqdm(error_file_path_list):
            os.remove(min_file_path)
        click.echo("\n删除完成！共删除{}个标的。".format(len_err))
    elif is_ok in ["no", "n"]:
        click.echo("\n异常数据未删除！")
    else:
        click.echo("\n输入异常！异常数据未删除!")


def _get_end_date():
    # if time earlier than 17:30, return previous trading_date
    now = datetime.datetime.now()
    end_date = now if now > datetime.datetime(now.year, now.month, now.day, 17, 30) else now-datetime.timedelta(1)
    return int(end_date.strftime("%Y%m%d"))


def remove_h5(h5_file: str):
    try:
        os.remove(h5_file)
    except FileNotFoundError:
        pass


def _append_h5(market_code: str, path: str, file_name: Optional[str] = None, min_start_date: int = MIN_START_DATE, rebuild: bool = False):
    ins = yhdatac.instruments(market_code)
    de_listed_date = int(ins.de_listed_date.replace("-", ""))

    if de_listed_date and de_listed_date < MIN_START_DATE:
        return

    def _get_price(start_date):
        if de_listed_date and de_listed_date < int(datetime.datetime.now().strftime("%Y%m%d")):
            end_date = de_listed_date
        else:
            end_date = _get_end_date()

        if end_date < start_date:
            return None, None
        df = yhdatac.get_price(
            market_code, start_date=start_date, end_date=end_date,
            frequency="1m", adjust_type="none", expect_df=True
        )
        if df is None or df.empty:
            return None, None
        df = df[~df.index.duplicated(keep="first")]
        date_index = df.index.levels[1]
        if "trading_date" in df:
            df["trading_date"] = df.trading_date.map(date_to_number)
        else:
            df["trading_date"] = date_index.map(date_to_number)
        df["datetime"] = date_index.map(convert_dt_to_int)
        df.reset_index(inplace=True, drop=True)
        data = np.array([tuple(d) for d in df[list(dtypes.names)].values], dtype=dtypes)
        index = np.array([
            (d, i) for i, d in df.drop_duplicates("trading_date", keep="first").trading_date.items()
        ], dtype=INDEX_DTYPE)
        return index, data

    def _append(origin, new):
        origin_len, new_len = len(origin), len(new)
        origin.resize(origin_len + new_len, axis=0)
        origin[origin_len: origin_len + new_len] = new

    if ins.type in EQUITIES_INS_TYPE:
        dtypes = EQUITIES_DTYPE
        path = os.path.join(path, "equities")
    elif ins.type == INSTRUMENT_TYPE.FUTURE:
        dtypes = DERIVATIVES_DTYPE
        path = os.path.join(path, "future")
    elif ins.type == INSTRUMENT_TYPE.OPTION:
        dtypes = DERIVATIVES_DTYPE
        path = os.path.join(path, "option")
    else:
        return
    os.makedirs(path, exist_ok=True)

    h5_file = os.path.join(path, file_name or "{}.h5".format(market_code))
    if rebuild:
        remove_h5(h5_file)
    mode = get_h5_mode(h5_file)
    from deepquant.quest.data.bundle import sval
    try:
        with h5py.File(h5_file, mode) as h5:
            if 'index' not in h5.keys():
                # new file
                index, data = _get_price(min_start_date)
                if "data" in h5:
                    # 上一次更新时可能只写入了 data 未写入 index
                    del h5["data"]
                if not (index is None or data is None):
                    h5.create_dataset('data', data=data, chunks=True, compression=9, shuffle=False, maxshape=(None,))
                    h5.create_dataset('index', data=index, maxshape=(None,), compression=9, shuffle=False)
            else:
                latest_date, latest_index = h5['index'][-1] if len(h5["index"]) else (MIN_START_DATE, 0)
                data_date = h5["data"][-1]["datetime"] // 1000000 if len(h5["data"]) else MIN_START_DATE
                if latest_date != data_date:
                    min_date = min(latest_date, data_date)
                    h5["data"].resize((h5["data"]["datetime"] // 1000000).searchsorted(min_date), axis=0)
                    h5["index"].resize((h5["index"]["date"]).searchsorted(min_date), axis=0)
                    latest_date, latest_index = h5['index'][-1] if len(h5["index"]) else (MIN_START_DATE, 0)
                if de_listed_date and latest_date >= de_listed_date:
                    return
                index, data = _get_price(int(yhdatac.get_next_trading_date(int(latest_date)).strftime("%Y%m%d")))
                if not (index is None or data is None):
                    index["line_no"] += (latest_index + len(h5['data'][latest_index:]))
                    _append(h5["index"], index)
                    _append(h5["data"], data)
    except OSError as e:
        system_log.error(f"更新 {h5_file} 失败，请检查文件的权限以及是否被其他进程占用\n{e}")
        sval.value = False
    except Exception as e:
        system_log.error(f"更新 {h5_file} 失败，该文件可能已经损坏，您可以尝试删除该文件并重新执行更新命令\n{e}")
        sval.value = False


TICK_DATE_CHUNK_SIZE = 100
COMPRESSION_KWARGS = blosc_opts(9, "blosc:lz4")


def _append_h5_tick(market_code, path, file_name=None, min_start_date=MIN_START_DATE, rebuild: bool = False):
    """更新tick级h5文件"""
    os.makedirs(path, exist_ok=True)
    h5_file = os.path.join(path, file_name or "{}.h5".format(market_code))
    if rebuild:
        remove_h5(h5_file)
    mode = get_h5_mode(h5_file)
    from deepquant.quest.data.bundle import sval
    try:
        with h5py.File(h5_file, mode) as h5:
            start_date = max(h5.keys()) if h5.keys() else min_start_date
            end_date = _get_end_date()
            if end_date < int(start_date):
                return
            day_dt = yhdatac.get_price(market_code, start_date, end_date, expect_df=True)
            if day_dt is None or day_dt.empty:
                return
            trading_dates = day_dt.index.levels[1].date

            for trading_dates_chunk in (trading_dates[i:i+TICK_DATE_CHUNK_SIZE] for i in range(
                    0, len(trading_dates), TICK_DATE_CHUNK_SIZE
            )):
                print(trading_dates_chunk[0], trading_dates_chunk[-1])
                tick_df = yhdatac.get_price(
                    market_code, trading_dates_chunk[0], trading_dates_chunk[-1],
                    frequency="tick", adjust_type="none", expect_df=True
                )
                if tick_df is None or tick_df.empty:
                    continue
                tick_df = tick_df[~tick_df.index.duplicated(keep="last")]
                for trading_date, _df in tick_df.groupby("trading_date"):
                    _df['date'] = _df.index.get_level_values(1).map(date_to_number)
                    _df['time'] = _df.index.get_level_values(1).map(time_to_number)
                    if 'open_interest' not in _df.columns:
                        _df['open_interest'] = 0
                    _df = _df[H5TicksLoader.COLUMNS]

                    data = [tuple([v * float(f[2]) for v, f in zip(d, H5TicksLoader.FIELDS)]) for d in _df.values]
                    ticks = np.array(data, dtype=H5TicksLoader.DTYPES)
                    key = trading_date.strftime("%Y%m%d")
                    if key in h5.keys():
                        del h5[key]
                    h5.create_dataset(name=key, data=ticks, **COMPRESSION_KWARGS)
                    del _df
    except OSError as e:
        system_log.error(f"更新 {h5_file} 失败，请检查文件的权限以及是否被其他进程占用\n{e}")
        sval.value = False
    except Exception as e:
        system_log.error(f"更新 {h5_file} 失败，该文件可能已经损坏，您可以尝试删除该文件并重新执行更新命令\n{e}")
        sval.value = False


def update_minbar(path: str, tags: Collection[str], with_derivatives: bool, concurrency: int, rebuild: bool = False):
    _market_code_set = _merge_tags(tags, with_derivatives)

    click.echo("开始更新 {} 只标的的分钟线数据：{}".format(len(_market_code_set), repr(_market_code_set)))
    succeed = multiprocessing.Value(c_bool, True)
    with ProgressedProcessPoolExecutor(
            max_workers=concurrency, initializer=process_init, initargs=(succeed, )
    ) as executor:
        for market_code in _market_code_set:
            executor.submit(_append_h5, market_code, path, rebuild=rebuild)
    return succeed.value


def update_tick(path: str, tags: Collection[str], with_derivatives: bool, concurrency: int, rebuild: bool = False):
    _market_code_set = _merge_tags(tags, with_derivatives)

    os.makedirs(path, exist_ok=True)

    click.echo("开始更新 {} 只标的的tick数据：{}".format(len(_market_code_set), repr(_market_code_set)))
    succeed = multiprocessing.Value(c_bool, True)
    with ProgressedProcessPoolExecutor(
            max_workers=concurrency, initializer=process_init, initargs=(succeed, )
    ) as executor:
        for market_code in _market_code_set:
            executor.submit(_append_h5_tick, market_code, path, rebuild=rebuild)
    return succeed.value


def download_simple_bundle(data_bundle_path, sample, file_path=None):
    # Prepare the bundle directory
    data_bundle_path = os.path.join(data_bundle_path, "bundle")
    if not os.path.exists(data_bundle_path):
        os.makedirs(data_bundle_path, exist_ok=True)

    if not file_path:
        # download tar file
        tmp = os.path.join(tempfile.gettempdir(), 'yhalpha_plus.bundle')
        url = 'http://bundle.assets.ricequant.com/bundles_v4/rqbundle_sample.tar.bz2'
        proxy_uri = os.environ.get('yhalpha_PROXY')
        r = requests.get(url, stream=True, proxies={'http': proxy_uri, 'https': proxy_uri})
        total_length = int(r.headers.get('content-length'))
        with open(tmp, 'wb') as out:
            download(out, total_length, url)
        print("bundle 数据下载完毕，解压中...")
    else:
        # Use files prepared by the user
        if not os.path.exists(file_path):
            print("{}文件不存在".format(file_path))
            return
        if os.path.basename(file_path) != "rqbundle_sample.tar.bz2":
            print("{}文件名不为 rqbundle_sample.tar.bz2".format(file_path))
            print("请使用下列连接下载：")
            print("http://bundle.assets.ricequant.com/bundles_v4/rqbundle_sample.tar.bz2")
            return
        tmp = file_path
        print("解压中...")

    tar = tarfile.open(tmp, 'r:bz2')
    tar.extractall(data_bundle_path)
    tar.close_price()
    if not file_path:
        os.remove(tmp)
    print("bundle 数据解压完成")


def update_bundle_from_yhdatac(concurrency, data_bundle_path, base, minbar, tick, with_derivatives, rebuild=False):
    """通过rqdatac更新指定标的的数据"""
    path = os.path.join(data_bundle_path, "bundle")
    succeed = True
    if rebuild:
        for i in range(REBUILD_COMFIRM_RETRY_TIMES):  # 允许 3 次错误的输入
            click.echo("本次会将指定的[合约分钟]和[合约tick]的h5文件从头进行更新，是否确认?[Y/n]")
            comfirm = input()
            if comfirm == "Y":
                break
            elif comfirm == "n":
                sys.exit()
            else:
                if i >= REBUILD_COMFIRM_RETRY_TIMES - 1:
                    sys.exit()
                continue

    if base:
        click.echo("开始更新日线及基础数据")
        if not os.path.exists(path):
            os.makedirs(path)
            succeed = update_daybar(path, create=True, enable_compression=True, concurrency=concurrency)
        else:
            succeed = update_daybar(path, create=False, enable_compression=True, concurrency=concurrency)
    if minbar:
        succeed = update_minbar(os.path.join(path, "h5"), minbar, with_derivatives, concurrency, rebuild) and succeed
    if tick:
        succeed = update_tick(os.path.join(path, "ticks"), tick, with_derivatives, concurrency, rebuild) and succeed
    return succeed


def update_bundle_from_exist_file(concurrency, data_bundle_path):
    """从bundle数据中查看已存在的标的文件 进行增量更新"""
    path = os.path.join(data_bundle_path, "bundle")
    click.echo("开始智能更新已下载数据")
    # daybar
    click.echo("开始更新日线及基础数据")
    succeed = update_daybar(path, create=False, enable_compression=True, concurrency=concurrency)

    # 分钟数据
    min_bar_folder = os.path.join(path, "h5")
    minbar_dirs = [s for s in os.listdir(min_bar_folder) if os.path.isdir(os.path.join(min_bar_folder, s))]
    if "ticks" in minbar_dirs:
        minbar_dirs.remove("ticks")
    min_ids = []
    for _dir in minbar_dirs:
        for file in os.listdir(os.path.join(path, "h5", _dir)):
            if file.endswith(".h5") and not file.endswith("-sample.h5"):
                min_ids.append(file[:-3])
    if min_ids:
        succeed = update_minbar(os.path.join(path, "h5"), min_ids, False, concurrency) and succeed

    # tick
    tick_ids = []
    for file in os.listdir(os.path.join(path, "ticks")):
        if file.endswith(".h5") and not file.endswith("-sample.h5"):
            tick_ids.append(file[:-3])
    if tick_ids:
        succeed = update_tick(os.path.join(path, "ticks"), tick_ids, False, concurrency) and succeed
    
    return succeed
