from typing import Any, Dict, List, Optional

from ._swordfishcpp import sw_init, sw_uninit
from ._swordfishcpp import Constant
from .config import convert_config

import atexit


class Runtime(object):
    # static
    _instanc = None
    _initial = False

    def __new__(cls, *args, **kwargs):
        if cls._instanc is None:
            cls._instanc = super().__new__(cls)
        return cls._instanc

    def initialize(self, args: Optional[List[str]] = None):
        if args is None:
            args = []
        if not Runtime._initial:
            sw_init(args)
            atexit.register(self.clean)
            Runtime._initial = True

    def clean(self):
        if Runtime._initial:
            sw_uninit()
            Runtime._initial = False

    def __del__(self):
        self.clean()


def init(*, args: Optional[List[str]] = None) -> List[str]:
    """Initialize Swordfish, and return the list of startup parameters.

    ```
    >>> import swordfish as sf
    >>> sf.init(["-home", "/path_to_home/"])
    ["swordfish", "-home", "/path_to_home/"]
    ```

    Parameters
    ----------
    args : Optional[List[str]], optional
        Initialization parameter for Swordfish, consistent with the
        DolphinDB console startup parameters. Defaults to None.
    """
    if args is None:
        args = []
    args = ["swordfish"] + args + convert_config()
    Runtime().initialize(args)
    return args
