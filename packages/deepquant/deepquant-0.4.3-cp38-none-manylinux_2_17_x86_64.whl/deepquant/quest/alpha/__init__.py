# -*- coding: utf-8 -*-

"""
yhalpha-Internal - a Algorithm Trading System Under Ricequant
"""
from deepquant.quest import run_code, run_file, run_func

from deepquant.quest.alpha._version import get_versions
from deepquant.quest.alpha.cmds import *

__version__ = get_versions()['version']
del get_versions

__all__ = [
    '__version__',
    "run_file",
    "run_code",
    "run_func",
]


def load_ipython_extension(ipython):
    """call by ipython"""
    from deepquant.quest import run_ipython_cell
    from deepquant.quest.mod.utils import inject_mod_commands
    inject_mod_commands()

    ipython.register_magic_function(run_ipython_cell, 'line_cell', 'deepquant.quest.alpha')
