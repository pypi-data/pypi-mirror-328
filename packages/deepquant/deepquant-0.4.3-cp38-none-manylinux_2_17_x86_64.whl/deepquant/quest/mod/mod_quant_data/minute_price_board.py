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

from deepquant.quest.data.bar_dict_price_board import BarDictPriceBoard
from deepquant.quest.core.events import EVENT


class MinutePriceBoard(BarDictPriceBoard):
    """
    For bt.
    In the strategy, avoid loading tick data without operating on the object
    Using day data instead of tick data to obtain close
    """

    def __init__(self):
        super(MinutePriceBoard, self).__init__()
        self._env.event_bus.prepend_listener(EVENT.PRE_BEFORE_TRADING, self._change_get_last_price)
        self._env.event_bus.prepend_listener(EVENT.AFTER_TRADING, self._change_get_last_price)

    def _change_get_last_price(self, event):
        """Use daily data during non-trading hours"""
        if event.event_type == EVENT.PRE_BEFORE_TRADING:
            self.get_last_price = super(MinutePriceBoard, self).get_last_price
        elif event.event_type == EVENT.AFTER_TRADING:
            self.last_price_dict = dict()
            self.trading_dt = event.trading_dt
            self.get_last_price = self.get_last_price_from_day_bar

    def get_last_price(self, market_code):
        return super(MinutePriceBoard, self).get_last_price(market_code)

    def get_last_price_from_day_bar(self, market_code):
        res = self.last_price_dict.get(market_code, None)
        if res is None:
            instrument = self._env.data_proxy.instruments(market_code)
            res = self._env.data_source.get_bar(instrument, self.trading_dt, "1d")
            # res = ['datetime', 'open', 'close', 'high', 'low', 'volume', 'total_turnover', 'high_limited', 'low_limited']
            res = res[2]  # 'close'
            self.last_price_dict[market_code] = res
        return res
