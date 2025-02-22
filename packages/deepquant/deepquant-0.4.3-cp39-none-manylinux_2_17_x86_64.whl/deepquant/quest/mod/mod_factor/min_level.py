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
import numbers

import numpy
from deepquant.quest.environment import Environment
from deepquant.quest.utils.logger import user_system_log
from rqfactor.engine_v2.exec_context import UNADJUSTED_PRICING_FACTORS
from rqfactor.interface import LeafFactor
from rqfactor.utils import get_leaves, use_dma


def _exec_expr(expr, context):
    if isinstance(expr, numbers.Real):
        return expr

    if isinstance(expr, LeafFactor):
        return context.get(expr)

    if isinstance(expr, tuple):
        func, args = expr
        return func(*[_exec_expr(arg, context) for arg in args])

    return expr


def exec_min_level_factor(factor, freq, market_code, dt):
    data_proxy = Environment.get_instance().data_proxy
    leaves = get_leaves(factor)
    bar_count = factor.shift + 1
    if use_dma(factor):
        bar_count += 126

    context = {}
    unadjusted = [leaf for leaf in leaves if leaf.name in UNADJUSTED_PRICING_FACTORS]
    if unadjusted:
        bars = data_proxy.history_bars(market_code, bar_count, freq,
                                       [f.name[:-len('_unadjusted')] for f in unadjusted], dt,
                                       adjust_type='none')
        if bars is None or bars.size == 0:
            user_system_log.warning("{}无历史数据，请检查bundle。dt={}".format(market_code, dt))
            return numpy.nan
        context.update((f, bars[f.name[:-len('_unadjusted')]]) for f in unadjusted)

    adjusted = [leaf for leaf in leaves if leaf.name not in UNADJUSTED_PRICING_FACTORS]
    if adjusted:
        bars = data_proxy.history_bars(market_code, bar_count, freq, [f.name for f in adjusted], dt,
                                       adjust_type='post')
        if bars is None or bars.size == 0:
            user_system_log.warning("{}无历史数据，请检查bundle。dt={}".format(market_code, dt))
            return numpy.nan
        context.update((f, bars[f.name]) for f in adjusted)

    result = _exec_expr(factor.expr, context)
    return result[-1]
