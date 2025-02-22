from deepquant.quest.utils import is_run_from_ipython

if is_run_from_ipython():
    try:
        # noinspection PyUnresolvedReferences
        from rqfactor import *
    except ImportError:
        pass

    try:
        # noinspection PyUnresolvedReferences
        from deepquant.quest.apis import *
    except ImportError:
        pass

    try:
        # noinspection PyUnresolvedReferences
        from deepquant.quest.mod.mod_optimizer2.api import *
    except ImportError:
        pass

    try:
        # noinspection PyUnresolvedReferences
        from deepquant.quest.mod.mod_factor.apis import *
    except ImportError:
        pass

del is_run_from_ipython
