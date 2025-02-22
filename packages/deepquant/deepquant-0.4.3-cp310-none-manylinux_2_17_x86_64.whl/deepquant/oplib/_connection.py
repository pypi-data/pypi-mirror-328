from ._swordfishcpp import Constant
from ._swordfishcpp import ConnectionImpl
from ._swordfishcpp import DefaultSessionConnectionImpl
from typing import Dict, Any, Optional


class Connection:
    def __init__(self, impl: ConnectionImpl) -> None:
        self.impl = impl

    def __enter__(self):
        self.impl.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.impl.__exit__(exc_type, exc_value, traceback)


def connect() -> Connection:
    return Connection(DefaultSessionConnectionImpl.create())
