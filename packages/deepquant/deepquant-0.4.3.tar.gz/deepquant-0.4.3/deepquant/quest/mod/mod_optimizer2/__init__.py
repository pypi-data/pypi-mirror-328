# -*- coding: utf-8 -*-
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def load_mod():
    from .mod import Optimizer2Mod
    return Optimizer2Mod()
