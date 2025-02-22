# -*- coding: utf-8 -*-

from .mod import OptionMod

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


__config__ = {
    # 行权滑点
    "exercise_slippage": 0,
    # 自定义品种手续费
    #   key:    underlying_symbol  标的品种
    #   value:  Dict
    #       open            开仓手续费
    #       close           平仓手续费
    #       exercise        行权手续费
    #       close_today     平今手续费
    "commission": {},
    "priority": 210,
}


def load_mod():
    return OptionMod()


