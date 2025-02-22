import abc

from ._swordfishcpp._enums import create_type_enum, create_array_type_enum
from ._swordfishcpp._enums import VOID, BOOL, CHAR, SHORT, INT, LONG
from ._swordfishcpp._enums import DATE, MONTH, TIME, MINUTE, SECOND, DATETIME
from ._swordfishcpp._enums import TIMESTAMP, NANOTIME, NANOTIMESTAMP, DATEHOUR
from ._swordfishcpp._enums import FLOAT, DOUBLE, SYMBOL, STRING, UUID, FUNCTIONDEF
from ._swordfishcpp._enums import HANDLE, CODE, DATASOURCE, RESOURCE, ANY, DICTIONARY
from ._swordfishcpp._enums import IPADDR, INT128, BLOB, COMPLEX, POINT, DURATION, OBJECT
from ._swordfishcpp._enums import SCALAR, VECTOR, PAIR, MATRIX, SET, DICT, TABLE
from ._swordfishcpp._enums import VAR, SHARED, DEF
from ._swordfishcpp._enums import DEBUG, INFO, ERROR, WARNING
from ._swordfishcpp._enums import ALL, FIRST, LAST, NONE
from ._swordfishcpp import EnumInt, DataType, DataForm


class DECIMALENUM(abc.ABC):
    __decimal_type__: int

    def __call__(self, scale: int) -> DataType:
        return create_type_enum(self.__decimal_type__, scale)


class __DECIMAL32(DECIMALENUM):
    __decimal_type__ = 37


class __DECIMAL64(DECIMALENUM):
    __decimal_type__ = 38


class __DECIMAL128(DECIMALENUM):
    __decimal_type__ = 39


DECIMAL32 = __DECIMAL32()
DECIMAL64 = __DECIMAL64()
DECIMAL128 = __DECIMAL128()


class __ARRAY:
    def __call__(self, sub_type: DataType) -> DataType:
        return create_array_type_enum(sub_type)


ARRAY = __ARRAY()


def _create_new_type_class(name, type_enum: EnumInt):
    return _TYPE_HINT(
        "_" + name,
        (),
        {
            '_data_type': type_enum,
            '_data_form': name,
        },
    )


class _TYPE_HINT(type):
    def __new__(cls, name, bases, dct):
        return super().__new__(cls, name, bases, dct)


SCALAR.set_function(_create_new_type_class)


__all__ = [
    "EnumInt", "DataType", "DataForm",
    "VOID", "BOOL", "CHAR", "SHORT", "INT", "LONG",
    "DATE", "MONTH", "TIME", "MINUTE", "SECOND", "DATETIME",
    "TIMESTAMP", "NANOTIME", "NANOTIMESTAMP", "DATEHOUR",
    "FLOAT", "DOUBLE", "SYMBOL", "STRING", "UUID", "FUNCTIONDEF",
    "HANDLE", "CODE", "DATASOURCE", "RESOURCE", "ANY", "DICTIONARY",
    "IPADDR", "INT128", "BLOB", "COMPLEX", "POINT", "DURATION", "OBJECT",
    "DECIMAL32", "DECIMAL64", "DECIMAL128",
    "ARRAY",
    "SCALAR", "VECTOR", "PAIR", "MATRIX", "SET", "DICT", "TABLE",
    "VAR", "SHARED", "DEF",
    "DEBUG", "INFO", "ERROR", "WARNING",
    "ALL", "FIRST", "LAST", "NONE",
]
