# -*- coding: utf-8 -*-
#
# Copyright 2017 Ricequant, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import numpy as np
from .tight_loops import to_minutes, unique_sorted

FIELD_AGG_FUNCTIONS = {
    'orig_time': 'last',
    'open': 'first',
    'close': 'last',
    'high': np.maximum,
    'low': np.minimum,
    'high_limited': 'first',
    'low_limited': 'first',
    'total_turnover': np.add,
    'volume': np.add,
    'acc_net_value': 'last',
    'unit_net_value': 'last',
    'discount_rate': 'last',
    'settlement': 'last',
    'prev_settlement': 'last',
    'open_interest': 'last',
    'basis_spread': 'last',
    'trading_date': 'last',
}


def resample_bars(instrument, bars, fields, resample, include_last=True):
    if instrument.type == 'Future' and instrument.exchange not in ("CFFEX", "CCFX"):
        return _resample_future_bars(bars, fields, resample, include_last)
    else:
        return _simple_resample_bars(bars, fields, resample, include_last)


def _simple_resample_bars(bars, fields, resample, include_last=True):
    if not include_last:
        result_len = len(bars) // resample
        bars = bars[:result_len*resample]
    else:
        result_len = (len(bars) + resample - 1) // resample

    if fields is None:
        dtype = bars.dtype
    elif isinstance(fields, str):
        dtype = np.dtype([(fields, bars.dtype[fields])])
    else:
        dtype = np.dtype([(fn, bars.dtype[fn]) for fn in fields])

    result = np.empty((result_len, ), dtype)
    if result_len == 0:
        return result

    for f in dtype.names:
        how = FIELD_AGG_FUNCTIONS[f]
        if how == 'last':
            result[f][:-1] = bars[f][resample-1:-1:resample]
            result[f][-1] = bars[f][-1]
        elif how == 'first':
            result[f] = bars[f][::resample]
        else:
            result[f] = how.reduceat(bars[f], list(range(0, len(bars), resample)))

    if isinstance(fields, str):
        result = result[fields]
    return result


TIME_MODULER = np.int64(1e6)
HUNDREND = np.int64(100)
MINUTES_PER_HOUR = np.int64(60)
MINUTES_PER_DAY = np.int64(60*24)


def _resample_future_bars(bars, fields, resample, include_last=True):
    minutes = to_minutes(bars['orig_time'])
    time_series = np.arange(0, minutes[-1] + 1, resample)

    if fields is None:
        dtype = bars.dtype
    elif isinstance(fields, str):
        dtype = np.dtype([(fields, bars.dtype[fields])])
    else:
        dtype = np.dtype([(fn, bars.dtype[fn]) for fn in fields])

    indexes = minutes.searchsorted(time_series)
    if len(indexes) == 0:
        if include_last:
            indexes = np.array([0])
        else:
            return np.empty((0, ), dtype=dtype)
    else:
        indexes = unique_sorted(minutes.searchsorted(time_series))
        if not include_last:
            if (minutes[-1] + 1) % resample != 0:
                bars = bars[:indexes[-1]]
                indexes = indexes[:-1]

    result_len = len(indexes)
    result = np.empty((result_len, ), dtype)
    if result_len == 0:
        return result

    for f in dtype.names:
        how = FIELD_AGG_FUNCTIONS[f]
        if how == 'last':
            result[f][:-1] = bars[f][indexes[1:] - 1]
            result[f][-1] = bars[f][-1]
        elif how == 'first':
            result[f] = bars[f][indexes]
        else:
            result[f] = how.reduceat(bars[f], indexes)

    if isinstance(fields, str):
        result = result[fields]

    return result

