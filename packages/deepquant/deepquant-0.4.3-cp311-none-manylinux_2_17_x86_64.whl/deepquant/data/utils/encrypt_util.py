#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: zhangluping_it
@time: 2024/8/21 9:05
@description: 
"""

import hashlib


def encrypt(msg, algorithm='HS256', key=None):
    if algorithm == 'HS256':
        return sha256_encrypt(msg)
    else:
        raise Exception("加密算法不支持:{}".format(algorithm))


def sha256_encrypt(msg):
    # 创建SHA-256对象
    sha256 = hashlib.sha256()
    # 更新哈希对象的内容
    sha256.update(msg.encode('utf-8'))
    # 计算哈希值
    hash_value = sha256.hexdigest()
    return hash_value
