#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author：Ginta 
# time:2020/6/30
# email: 775650117@qq.com
import numpy as np

DTYPE_MAP = {
    "ETF": np.dtype([
        ('orig_time', '<i8'), ('open', '<f8'), ('high', '<f8'), ('low', '<f8'), ('close', '<f8'),
        ('volume', '<f8'), ('total_turnover', '<f8'), ('iopv', '<f8')
    ]),
    "LOF": np.dtype([
        ('orig_time', '<i8'), ('open', '<f8'), ('high', '<f8'), ('low', '<f8'), ('close', '<f8'),
        ('volume', '<f8'), ('total_turnover', '<f8'), ('iopv', '<f8')
    ]),
    "CS": np.dtype([
        ('orig_time', '<i8'), ('open', '<f8'), ('high', '<f8'), ('low', '<f8'), ('close', '<f8'),
        ('volume', '<f8'), ('total_turnover', '<f8')
    ]),
    "INDX": np.dtype([
        ('orig_time', '<i8'), ('open', '<f8'), ('high', '<f8'), ('low', '<f8'), ('close', '<f8'),
        ('volume', '<f8'), ('total_turnover', '<f8')
    ]),
    "Future": np.dtype([
        ('orig_time', '<i8'),
        ('trading_date', '<i4'),
        ('open', '<f8'),
        ('high', '<f8'),
        ('low', '<f8'),
        ('close', '<f8'),
        ('open_interest', '<i8'),
        ('volume', '<f8'),
        ('total_turnover', '<f8')
    ]),
}
