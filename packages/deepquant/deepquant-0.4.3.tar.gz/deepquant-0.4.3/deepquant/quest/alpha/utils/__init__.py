#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author：Ginta 
# time:2020/7/16
# email: 775650117@qq.com


def blosc_opts(complevel=9, complib='blosc:lz4', shuffle=False) -> dict:
    shuffle = 2 if shuffle == 'bit' else 1 if shuffle else 0
    compressors = ['blosclz', 'lz4', 'lz4hc', 'snappy', 'zlib', 'zstd']
    complib = ['blosc:' + c for c in compressors].index(complib)
    args = {
        'compression': 32001,
        'compression_opts': (0, 0, 0, 0, complevel, shuffle, complib),
        "shuffle": shuffle
    }
    return args
