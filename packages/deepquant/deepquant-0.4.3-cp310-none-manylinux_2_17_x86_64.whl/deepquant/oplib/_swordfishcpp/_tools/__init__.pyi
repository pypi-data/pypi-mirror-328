from swordfish.data import Constant, FunctionDef


def check_aggregate_function(func: FunctionDef, arg_nums: int = -1):
    ...


def check_builtin_function(func: FunctionDef):
    ...


def check_is_nothing(obj: Constant):
    ...
