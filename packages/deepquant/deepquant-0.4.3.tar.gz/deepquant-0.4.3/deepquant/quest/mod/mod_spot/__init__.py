# -*- coding: utf-8 -*-
from .mod import SpotMod

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


__config__ = {
    "commission_multiplier": 1,
    "priority": 240
}


def load_mod():
    return SpotMod()
