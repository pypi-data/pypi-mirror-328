# -*- coding: utf-8 -*-

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions


def load_mod():
    from .mod import ConvertibleMod

    return ConvertibleMod()


__config__ = {
    "commission_rate": 0,
    "min_commission": 0,
    "priority": 220
}
