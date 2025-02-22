# -*- coding: utf-8 -*-
# 版权所有 2019 深圳米筐科技有限公司（下称“米筐科技”）
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

import six
from datetime import datetime
import numpy as np

from deepquant.quest.core.execution_context import ExecutionContext
from deepquant.quest.environment import Environment
from deepquant.quest.const import RUN_TYPE
from deepquant.quest.utils.datetime_func import convert_int_to_datetime
from deepquant.quest.utils.i18n import gettext as _
from deepquant.quest.utils.logger import system_log
from deepquant.quest.utils.exception import patch_user_exc
from deepquant.quest.utils.repr import PropertyReprMeta
from deepquant.quest.utils.class_helper import cached_property
from deepquant.quest.const import EXECUTION_PHASE

NAMES = ['open_price', 'close_price', 'low_price', 'high_price', 'settlement', 'high_limited', 'low_limited', 'volume', 'total_turnover',
         'discount_rate', 'acc_net_value', 'unit_net_value', 'open_interest',
         'basis_spread', 'prev_settlement', 'datetime']
NANDict = {i: np.nan for i in NAMES}


class PartialBarObject(metaclass=PropertyReprMeta):
    # 用于 open_auction
    __repr_properties__ = (
        "market_code", "orig_time", "open_price", "high_limited", "low_limited", "last_price"
    )

    def __init__(self, instrument, data, dt=None):
        self._dt = dt
        self._data = data if data is not None else NANDict
        self._instrument = instrument
        self._env = Environment.get_instance()

    @cached_property
    def orig_time(self):
        """
        [datetime.datetime] 时间戳
        """
        if self._dt is not None:
            return self._dt
        dt = self._data["orig_time"]
        if isinstance(dt, datetime):
            return dt
        return convert_int_to_datetime(dt)

    @cached_property
    def instrument(self):
        return self._instrument

    @cached_property
    def market_code(self):
        """
        [str] 交易标的代码
        """
        return self._instrument.market_code

    @cached_property
    def symbol(self):
        """
        [str] 合约简称
        """
        return self._instrument.security_name

    @cached_property
    def open(self):
        """
        [float] 开盘价
        """
        return self._data["open_price"]

    @cached_property
    def high_limited(self):
        """
        [float] 涨停价
        """
        try:
            v = self._data['high_limited']
            return v if v != 0 else np.nan
        except (KeyError, ValueError):
            return np.nan

    @cached_property
    def low_limited(self):
        """
        [float] 跌停价
        """
        try:
            v = self._data['low_limited']
            return v if v != 0 else np.nan
        except (KeyError, ValueError):
            return np.nan

    @cached_property
    def last(self):
        """
        [float] 当前最新价
        """
        return self._data["last_price"]

    @cached_property
    def volume(self):
        """
        [float] 截止到当前的成交量
        """
        return self._data["volume"]

    @cached_property
    def total_turnover(self):
        """
        [float] 截止到当前的成交额
        """
        return self._data['total_turnover']

    @cached_property
    def prev_close(self):
        """
        [float] 昨日收盘价
        """
        try:
            return self._data['pre_close_price']
        except (ValueError, KeyError):
            return self._env.data_proxy.get_prev_close(self._instrument.market_code, self._env.trading_dt)

    @cached_property
    def prev_settlement(self):
        """
        [float] 昨日结算价（期货专用）
        """
        try:
            return self._data['prev_settlement']
        except (ValueError, KeyError):
            return self._env.data_proxy.get_prev_settlement(self._instrument.market_code, self._env.trading_dt)

    @cached_property
    def isnan(self):
        return np.isnan(self._data['close_price'])


class BarObject(PartialBarObject):
    __repr_properties__ = (
        "market_code", "orig_time", "open_price", "close_price", "high_price", "low_price", "high_limited", "low_limited"
    )

    @cached_property
    def close_price(self):
        """
        [float] 收盘价
        """
        return self._data["close_price"]

    @cached_property
    def low_price(self):
        """
        [float] 最低价
        """
        return self._data["low_price"]

    @cached_property
    def high(self):
        """
        [float] 最高价
        """
        return self._data["high_price"]

    @cached_property
    def last(self):
        """
        [float] 当前最新价
        """
        return self.close_price

    @cached_property
    def discount_rate(self):
        return self._data['discount_rate']

    @cached_property
    def acc_net_value(self):
        return self._data['acc_net_value']

    @cached_property
    def unit_net_value(self):
        return self._data['unit_net_value']

    INDEX_MAP = {
        'IF': '000300.XSHG',
        'IH': '000016.XSHG',
        'IC': '000905.XSHG',
    }

    @cached_property
    def basis_spread(self):
        try:
            return self._data['basis_spread']
        except (ValueError, KeyError):
            if self._instrument.type != 'Future' or Environment.get_instance().config.base.run_type != RUN_TYPE.PAPER_TRADING:
                raise
            if self._instrument.underlying_symbol in ['IH', 'IC', 'IF']:
                market_code = self.INDEX_MAP[self._instrument.underlying_symbol]
                bar = Environment.get_instance().data_proxy.get_bar(market_code, None, '1m')
                return self.close_price - bar.close_price
            else:
                return np.nan

    @cached_property
    def settlement(self):
        """
        [float] 结算价（期货专用）
        """
        return self._data['settlement']

    @cached_property
    def open_interest(self):
        """
        [float] 截止到当前的持仓量（期货专用）
        """
        return self._data['open_interest']

    @cached_property
    def is_trading(self):
        """
        [bool] 是否有成交量
        """
        return self._data['volume'] > 0

    @cached_property
    def isnan(self):
        return np.isnan(self._data['close_price'])

    @cached_property
    def suspended(self):
        if self.isnan:
            return True

        return Environment.get_instance().data_proxy.is_suspended(self._instrument.market_code, int(self._data['datetime'] // 1000000))

    def mavg(self, intervals, frequency='1d'):
        if frequency == 'day':
            frequency = '1d'
        if frequency == 'minute':
            frequency = '1m'

        # copy form history
        env = Environment.get_instance()
        dt = env.calendar_dt

        if (env.config.base.frequency == '1m' and frequency == '1d') or ExecutionContext.phase() == EXECUTION_PHASE.BEFORE_TRADING:
            # 在分钟回测获取日线数据, 应该推前一天
            dt = env.data_proxy.get_previous_trading_date(env.calendar_dt.date())
        bars = env.data_proxy.fast_history(self._instrument.market_code, intervals, frequency, 'close', dt)
        return bars.mean()

    def vwap(self, intervals, frequency='1d'):
        if frequency == 'day':
            frequency = '1d'
        if frequency == 'minute':
            frequency = '1m'

        # copy form history
        env = Environment.get_instance()
        dt = env.calendar_dt

        if (env.config.base.frequency == '1m' and frequency == '1d') or ExecutionContext.phase() == EXECUTION_PHASE.BEFORE_TRADING:
            # 在分钟回测获取日线数据, 应该推前一天
            dt = env.data_proxy.get_previous_trading_date(env.calendar_dt.date())
        bars = env.data_proxy.fast_history(self._instrument.market_code, intervals, frequency, ['close', 'volume'], dt)
        sum = bars['volume'].sum()
        if sum == 0:
            # 全部停牌
            return 0

        return np.dot(bars['close_price'], bars['volume']) / sum

    def __repr__(self):
        base = [
            ('symbol', repr(self._instrument.security_name)),
            ('market_code', repr(self._instrument.market_code)),
            ('orig_time', repr(self.orig_time)),
        ]

        if self.isnan:
            base.append(('error', repr('DATA UNAVAILABLE')))
            return 'Bar({0})'.format(', '.join('{0}: {1}'.format(k, v) for k, v in base) + ' NaN BAR')

        if isinstance(self._data, dict):
            # in pt
            base.extend((k, v) for k, v in self._data.items() if k != 'orig_time')
        else:
            base.extend((n, self._data[n]) for n in self._data.dtype.names if n != 'orig_time')
        return "Bar({0})".format(', '.join('{0}: {1}'.format(k, v) for k, v in base))

    def __getitem__(self, key):
        return self.__dict__[key]

    def __getattr__(self, item):
        try:
            if item in self._data.dtype.names:
                value = self._data[item]
            elif item+"_price" in self._data.dtype.names:
                value = self._data[item+"_price"]
        except KeyError:
            raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__, item))
        else:
            if isinstance(value, bytes):
                return value.decode("utf-8")
            return value


class BarMap(object):
    def __init__(self, data_proxy, frequency):
        self._dt = None
        self._data_proxy = data_proxy
        self._frequency = frequency
        self._cache = {}

    def update_dt(self, dt):
        self._dt = dt
        self._cache.clear()

    def items(self):
        return ((o, self.__getitem__(o)) for o in Environment.get_instance().get_universe())

    def keys(self):
        return (o for o in Environment.get_instance().get_universe())

    def values(self):
        return (self.__getitem__(o) for o in Environment.get_instance().get_universe())

    def __contains__(self, o):
        return o in Environment.get_instance().get_universe()

    def __len__(self):
        return len(Environment.get_instance().get_universe())

    def __getitem__(self, key):
        if not isinstance(key, six.string_types):
            raise patch_user_exc(ValueError('invalid key {} (use market_code please)'.format(key)))

        instrument = self._data_proxy.instrument(key)
        if instrument is None:
            raise patch_user_exc(ValueError('invalid order book id or symbol: {}'.format(key)))
        market_code = instrument.market_code

        try:
            return self._cache[market_code]
        except KeyError:
            try:
                if not self._dt:
                    return BarObject(instrument, NANDict, self._dt)
                if ExecutionContext.phase() == EXECUTION_PHASE.OPEN_AUCTION:
                    trading_date = self._dt if self._frequency == "1d" else self._data_proxy.get_trading_dt(self._dt).date()
                    bar = self._data_proxy.get_open_auction_bar(market_code, trading_date)
                else:
                    bar = self._data_proxy.get_bar(market_code, self._dt, self._frequency)
            except PermissionError:
                raise
            except Exception as e:
                system_log.exception(e)
                raise patch_user_exc(KeyError(_(u"id_or_symbols {} does not exist").format(key)))
            if bar is None:
                return BarObject(instrument, NANDict, self._dt)
            else:
                self._cache[market_code] = bar
                return bar

    @cached_property
    def dt(self):
        return self._dt

    def __repr__(self):
        keys = list(self.keys())
        s = ', '.join(keys[:10]) + (' ...' if len(keys) > 10 else '')
        return "{}({})".format(type(self).__name__, s)
