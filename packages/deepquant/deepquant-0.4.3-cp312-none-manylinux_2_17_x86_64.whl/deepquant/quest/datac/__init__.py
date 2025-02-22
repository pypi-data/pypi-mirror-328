# -*- coding: utf-8 -*-
import warnings

warnings.filterwarnings("ignore", message="[.\n]*Pandas[.\n]*")
warnings.simplefilter(action="ignore", category=FutureWarning)
from .client import init, reset, initialized  # noqa


__all__ = ["init", "reset", "initialized"]


def __go():
    import sys
    import importlib
    import pkgutil

    # 3.4 引入 asyncio，3.5 引入 async/await 语法，3.6 引入 async generator
    async_syntax_supported = sys.version_info[:2] >= (3, 6)

    for loader, module_name, is_pkg in pkgutil.walk_packages(__path__, "deepquant.quest.datac."):
        if module_name == "deepquant.quest.datac.services.async_live_md_client" and not async_syntax_supported:
            continue
        elif module_name.startswith("deepquant.quest.datac.services") and not is_pkg:
            importlib.import_module(module_name)


__go()

del __go



