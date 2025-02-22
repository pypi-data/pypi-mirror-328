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

from deepquant.quest.interface import AbstractPriceBoard


class SnapshotPriceBoard(AbstractPriceBoard):
    def __init__(self, env):
        self._env = env

    def get_last_price(self, market_code):
        snapshot = self._env.data_proxy.current_snapshot(market_code, '1m', self._env.calendar_dt)
        if snapshot is None:
            return np.nan
        return snapshot.last

    def get_a1(self, market_code):
        return np.nan

    def get_b1(self, market_code):
        return np.nan

    def get_low_limited(self, market_code):
        return self._env.get_bar(market_code).low_limited

    def get_high_limited(self, market_code):
        return self._env.get_bar(market_code).high_limited
