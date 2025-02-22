# -*- coding: utf-8 -*-
import datetime

from deepquant.quest.environment import Environment
from deepquant.quest.model.tick import TickObject


class LazyTick(TickObject):
    def __init__(self, instrument, raw_tick, trading_date):
        
        super(LazyTick, self).__init__(instrument, raw_tick)

        self._trading_date = trading_date
        self.__bar = None

    @property
    def _bar(self):
        if self.__bar is None:
            dt = datetime.datetime.combine(self._trading_date, datetime.time(23, 59, 59))
            self.__bar = Environment.get_instance().data_proxy.get_bar(self.market_code, dt, frequency="1d")
        return self.__bar

    @property
    def open(self):
        return self._bar.open

    @property
    def prev_close(self):
        return self._bar.prev_close

    @property
    def prev_settlement(self):
        return self._bar.prev_settlement

    @property
    def high_limited(self):
        return self._bar.high_limited

    @property
    def low_limited(self):
        return self._bar.low_limited
