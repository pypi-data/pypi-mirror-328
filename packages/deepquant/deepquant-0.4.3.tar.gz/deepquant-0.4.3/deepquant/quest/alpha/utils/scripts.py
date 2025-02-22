#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author：Ginta 
# time:2020/7/16
# email: 775650117@qq.com
import os
import shutil

import h5py


def check_tick(path):
    tick_path = os.path.join(path, "h5", "ticks")
    if os.path.exists(tick_path):
        if os.path.exists(os.path.join(path, "ticks")):
            shutil.rmtree(os.path.join(path, "ticks"))
        shutil.move(tick_path, path)


def get_h5_mode(path):
    mode = 'a'
    try:
        h5 = h5py.File(path, 'a')
        h5.close()
    except OSError:
        mode = 'w'
    return mode
