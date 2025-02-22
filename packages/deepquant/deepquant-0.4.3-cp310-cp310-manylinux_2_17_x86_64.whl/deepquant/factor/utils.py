import numpy as np
import pandas as pd

def get_forward_returns_columns(columns):
    return columns[columns.astype('str').str.startswith("period_")]

def convert_to_forward_returns_columns(period):
    try:
        return 'period_{:d}'.format(period)
    except ValueError:
        return period

PD_VERSION = pd.__version__


def rolling_apply(
    x,
    window,
    func,
    min_periods=None,
    freq=None,
    center=False,
    args=None,
    kwargs=None
):
    if args is None:
        args = tuple()
    if kwargs is None:
        kwargs = dict()

    if PD_VERSION >= '0.23.0':
        return x.rolling(
            window, min_periods=min_periods, center=center
        ).apply(
            func, False, args=args, kwargs=kwargs
        )
    elif PD_VERSION >= '0.18.0':
        return x.rolling(
            window, min_periods=min_periods, center=center
        ).apply(
            func, args=args, kwargs=kwargs
        )
    else:
        return pd.rolling_apply(
            x,
            window,
            func,
            min_periods=min_periods,
            freq=freq,
            center=center,
            args=args,
            kwargs=kwargs
        )

def rate_of_return(period_ret, base_period=1):
    period_len = int(period_ret.name.replace('period_', ''))
    conversion_factor = (pd.Timedelta(base_period) /
                         pd.Timedelta(period_len))
    return period_ret.add(1).pow(conversion_factor).sub(1)

def std_conversion(period_std, base_period=1):
    period_len = float(period_std.name.replace('period_', ''))/base_period
    return period_std / np.sqrt(period_len)

def timedelta_strings_to_integers(sequence):
    sequence = [s.replace('period_', '')+'D' for s in sequence]
    return list(map(lambda x: pd.Timedelta(x).days, sequence))

