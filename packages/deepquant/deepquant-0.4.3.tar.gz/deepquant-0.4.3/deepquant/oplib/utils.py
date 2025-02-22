from ._swordfishcpp import get_home_dir
from ._swordfishcpp import get_working_dir
from ._swordfishcpp import get_exec_dir


class Info:
    @property
    def HOME_DIR(self):
        return get_home_dir()

    @property
    def WORKING_DIR(self):
        return get_working_dir()

    @property
    def EXEC_DIR(self):
        return get_exec_dir()


info = Info()

__all__ = [
    "info",
]
