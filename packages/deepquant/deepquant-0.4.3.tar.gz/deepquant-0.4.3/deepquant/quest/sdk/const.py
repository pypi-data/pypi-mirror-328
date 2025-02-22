# -*- coding: utf-8 -*-
#
# Copyright 2016 Ricequant, Inc
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
import json
import os

RQDATAC_DEFAULT_ADDRESS = "rqdatad-pro.ricequant.com:16011"
PERMISSIONS_INFO_URL = "https://www.ricequant.com/api/rqlicense/get_permissions_readable_info"
DEFAULT_INDEX_URL = "https://pypi.tuna.tsinghua.edu.cn/simple/"
EXTRA_INDEX_URL = "https://rquser:Ricequant8@pypi2.ricequant.com/simple/"
BASH_FILE = [".bash_profile", ".bashrc", ".bash_profile", ".zshrc"]
TAG_MAP = ["stock", "futures", "fund", "index", "option", "convertible", ]
DEFAULT_BUNDLE_PATH = "D:\\sendData\\ricequant"
    #os.path.join(os.path.expanduser('~'), ".deepquant")

PRODUCTS = ["yhalpha_plus", "yhdatac", "rqoptimizer", "rqpattr"]
CONCERNED_PACKAGES = [
    "deepquant.quest",

    "wcwidth", "tabulate", 'requests', "cryptography", "click", "jwt", "patsy", "statsmodels",
    "scipy", "numpy", "pandas", "rapidjson",

    "talib",

     "ecos", "scs", "cvxpy", "osqp",

     "h5py", "hdf5plugin"
]
