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

from deepquant.quest.environment import Environment
from deepquant.quest.interface import AbstractPriceBoard
from deepquant.quest.core.events import EVENT
from deepquant.quest.model.bar import NANDict
from deepquant.quest.model.tick import TickObject


class TickPriceBoard(AbstractPriceBoard):
    def __init__(self, redis_store):
        self._env = Environment.get_instance()
        self._redis_store = redis_store
        self._env.event_bus.prepend_listener(EVENT.TICK, self._on_tick)
        self._tick_board = {}
        self._tick_updated_dt = {}

    def _on_tick(self, event):
        tick = event.tick
        self._tick_board[tick.market_code] = tick
        self._tick_updated_dt[tick.market_code] = tick.orig_time

    def _get_last(self, market_code):
        # FIXME: dirty hack
        if self._redis_store is None:
            instrument = self._env.data_proxy.instrument(market_code)
            _tick = self._env.data_source.current_snapshot(instrument, "tick", self._env.calendar_dt)
            if _tick is None:
                _tick = TickObject(instrument, NANDict)
            return _tick

        if market_code in self._tick_updated_dt:
            if (Environment.get_instance().calendar_dt - self._tick_updated_dt[market_code]).total_seconds() <= 5:
                return self._tick_board[market_code]
            else:
                del self._tick_updated_dt[market_code]
                del self._tick_board[market_code]

        return self._redis_store.get_snapshot(market_code)

    def get_last_price(self, market_code):
        last = self._get_last(market_code)
        if not last:
            return np.nan
        try:
            return last['last']
        except KeyError:
            return np.nan

    def get_high_limited(self, market_code):
        try:
            return self._get_last(market_code)['high_limited']
        except KeyError:
            return np.nan

    def get_low_limited(self, market_code):
        try:
            return self._get_last(market_code)['low_limited']
        except KeyError:
            return np.nan

    def get_a1(self, market_code):
        try:
            return self._tick_board[market_code].asks[0]
        except (KeyError, TypeError, IndexError):
            return 0

    def get_b1(self, market_code):
        try:
            return self._tick_board[market_code].bids[0]
        except (KeyError, TypeError, IndexError):
            return 0
