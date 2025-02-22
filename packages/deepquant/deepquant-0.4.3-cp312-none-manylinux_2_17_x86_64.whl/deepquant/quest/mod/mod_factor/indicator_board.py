# -*- coding: utf-8 -*-
# 版权所有 2020 深圳米筐科技有限公司（下称“米筐科技”）
#
# 除非遵守当前许可，否则不得使用本软件。
#
#     * 非商业用途（非商业用途指个人出于非商业目的使用本软件，或者高校、研究所等非营利机构出于教育、科研等目的使用本软件）：
#         遵守 Apache License 2.0（下称“Apache 2.0 许可”），
#         您可以在以下位置获得 Apache 2.0 许可的副本：http://www.apache.org/licenses/LICENSE-2.0。
#         除非法律有要求或以书面形式达成协议，否则本软件分发时需保持当前许可“原样”不变，且不得附加任何条件。
#
#     * 商业用途（商业用途指个人出于任何商业目的使用本软件，或者法人或其他组织出于任何目的使用本软件）：
#         未经米筐科技授权，任何个人不得出于任何商业目的使用本软件（包括但不限于向第三方提供、销售、出租、出借、转让本软件、
#         本软件的衍生产品、引用或借鉴了本软件功能或源代码的产品或服务），任何法人或其他组织不得出于任何目的使用本软件，
#         否则米筐科技有权追究相应的知识产权侵权责任。
#         在此前提下，对本软件的使用同样需要遵守 Apache 2.0 许可，Apache 2.0 许可与本许可冲突之处，以本许可为准。
#         详细的授权流程，请联系 public@ricequant.com 获取。
from typing import Callable
import datetime

from rqfactor.interface import AbstractFactor, UserDefinedLeafFactor
from rqfactor.fix import FixedFactor
from rqfactor.engine_v2 import execute_factor
from rqfactor.engine_v2.exec_context import PRICING_FACTORS
from rqfactor.utils import is_cross_sectional, get_leaves

from deepquant.quest.utils.exception import RQInvalidArgument
from deepquant.quest.environment import Environment
from deepquant.quest.core.execution_context import ExecutionContext
from deepquant.quest.const import EXECUTION_PHASE

from .min_level import exec_min_level_factor


class IndicatorBoard:
    def __init__(self):
        self._factors = {}
        self._cache = {}

    @ExecutionContext.enforce_phase(EXECUTION_PHASE.ON_INIT)
    def reg_indicator(self, name, factor, freq='1d', win_size=None):
        if not isinstance(freq, str) or (freq != '1d' and freq[-1] != 'm'):
            raise RQInvalidArgument('freq: invalid value, use 1d or 1m')

        if isinstance(factor, Callable):
            factor = factor()
        if not isinstance(factor, AbstractFactor):
            raise RQInvalidArgument('factor: expect a function returns a factor or a factor, got {}'.format(repr(factor)))
        if name in self._factors:
            raise RQInvalidArgument('name: conflict, factor with the same name ({}) exists'.format(name))
        if is_cross_sectional(factor):
            raise RQInvalidArgument('cross sectional factor is not supported: {}'.format(name))
        if freq.endswith('m'):
            for leaf in get_leaves(factor):
                if isinstance(leaf, UserDefinedLeafFactor):
                    raise RQInvalidArgument('UserDefinedLeafFactor is not supported: {}'.format(name))
                if isinstance(leaf, FixedFactor):
                    raise RQInvalidArgument('FIX operator is not supported yet with minute freq')
                if leaf not in PRICING_FACTORS:
                    raise RQInvalidArgument(
                        'only pricing factors (OHLC volume total_turnover) are supported in minute level factor, '
                        'a non-pricing factor found in factor {}'.format(name))

        self._factors[name] = (factor, freq)

    @ExecutionContext.enforce_phase(
        EXECUTION_PHASE.BEFORE_TRADING,
        EXECUTION_PHASE.ON_BAR,
        EXECUTION_PHASE.ON_TICK,
        EXECUTION_PHASE.OPEN_AUCTION,
        EXECUTION_PHASE.SCHEDULED,
    )
    def get_indicator(self, market_code, name):
        return self._get_indicator(market_code, name)

    def _get_indicator(self, market_code, name):
        raise NotImplementedError()


class BTIndicatorBoard(IndicatorBoard):
    def _get_indicator(self, market_code, name):
        env = Environment.get_instance()
        date = env.data_proxy.get_previous_trading_date(env.trading_dt)

        try:
            factor, freq = self._factors[name]
        except KeyError:
            raise RQInvalidArgument('indicator {} not found'.format(name))

        if freq[-1] == 'm':
            return exec_min_level_factor(factor, freq, market_code, env.calendar_dt)

        if (market_code, name) in self._cache:
            s = self._cache[market_code, name]
            try:
                return s[date]
            except KeyError:
                return None

        instrument = env.data_proxy.instruments(market_code)
        end_date = env.config.base.end_date
        if instrument.de_listed_date.date() != datetime.date(2999, 12, 31):
            end_date = min(
                env.config.base.end_date,
                env.data_proxy.get_previous_trading_date(instrument.de_listed_date).date()
            )

        df = execute_factor(factor, [market_code], date, end_date)
        s = df[market_code]
        self._cache[market_code, name] = s
        return s[date]


class PTIndicatorBoard(IndicatorBoard):
    def _get_indicator(self, market_code, name):
        env = Environment.get_instance()
        date = env.data_proxy.get_previous_trading_date(env.trading_dt)

        try:
            factor, freq = self._factors[name]
        except KeyError:
            raise RQInvalidArgument('indicator {} not found'.format(name))

        if freq[-1] == 'm':
            return exec_min_level_factor(factor, freq, market_code, env.calendar_dt)

        if (market_code, name) in self._cache:
            return self._cache[market_code, name]

        df = execute_factor(factor, [market_code], date, date)
        s = df[market_code]
        self._cache[market_code, name] = s.iloc[0]
        return s.iloc[0]
