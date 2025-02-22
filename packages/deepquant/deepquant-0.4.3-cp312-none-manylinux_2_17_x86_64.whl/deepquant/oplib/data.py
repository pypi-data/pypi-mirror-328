from typing import Any, List, Union
import typing

from ._swordfishcpp import Constant, Scalar, Vector, Table, Matrix, Set, Dictionary
from ._swordfishcpp import AnyVector, ArrayVector, Pair
from ._swordfishcpp import Void, Bool, Char, Short, Int, Long, Float, Double
from ._swordfishcpp import String, Blob, Date, Month, Time, Minute, Second
from ._swordfishcpp import DateTime, Timestamp, NanoTime, NanoTimestamp, DateHour
from ._swordfishcpp import Uuid, Int128, Ipaddr, Duration, MetaCode
from ._swordfishcpp import Decimal32, Decimal64, Decimal128
from ._swordfishcpp import FunctionDef

from ._swordfishcpp import convert_scalar, convert_vector, create_partial
from ._swordfishcpp import convert_matrix, convert_set, convert_dictionary, convert_table
from ._swordfishcpp import create_vector, create_any_vector, create_array_vector, create_pair
from ._swordfishcpp import create_matrix, create_set, create_dictionary_with_key_and_val, create_dictionary, create_table
from ._swordfishcpp._exception import ConvertError

from .function import isNull as F_isNull
from .function import rows as F_rows
from .function import cols as F_cols
from .function import rowRank as F_rowRank
from .function import rename_ as F_rename_
from .function import keys as F_keys
from .function import values as F_values
from .function import schema as F_schema
from .function import head as F_head
from .function import tail as F_tail
from .function import count as F_count

from .types import DataType, TypeDict, TypeList
from .types import ANY


NULL = Void.NULL_VALUE
DFLT = Void.NULL_VALUE
Nothing = Void.VOID_VALUE


def partial(func: FunctionDef, *args, **kwargs):
    return create_partial(func, *args, **kwargs)


def scalar(data: Any, *, type: DataType = None) -> Scalar:
    return convert_scalar(data, type)


@typing.overload
def vector(data: Any = None, *, type: DataType = None) -> Vector:
    ...


@typing.overload
def vector(*, type: DataType = None, size: int = 0, capacity: int = 1, default: Any = None) -> Vector:
    ...


def vector(
    data: Any = None,
    *,
    type: DataType = None,
    size: int = 0,
    capacity: int = 1,
    default: Any = None
):
    # overload 1
    if data is not None:
        return convert_vector(data, 0, type)
    # overload 2
    return create_vector(type, size, capacity, default)


@typing.overload
def any_vector(data: Any = None) -> AnyVector:
    ...


@typing.overload
def any_vector(*, size: int = 0, capacity: int = 1, default: Any = None) -> AnyVector:
    ...


def any_vector(
    data: Any = None,
    *,
    size: int = 0,
    capacity: int = 1,
    default: Any = None
) -> AnyVector:
    if data is not None:
        return convert_vector(data, 1, ANY)
    return create_any_vector(size, capacity, default)


@typing.overload
def array_vector(data: Any = None, *, type: DataType = None) -> ArrayVector:
    ...


@typing.overload
def array_vector(*, index: Any = None, value: Any = None, type: DataType = None) -> ArrayVector:
    ...


def array_vector(
    data: Any = None,
    *,
    index: Any = None,
    value: Any = None,
    type: DataType = None
) -> ArrayVector:
    if data is not None:
        return convert_vector(data, 2, type)
    if index is None or value is None:
        raise RuntimeError("ERROR!")
    return create_array_vector(index, value, type)


def pair(a: Any, b: Any, *, type: DataType = None) -> Pair:
    if not isinstance(a, Constant):
        a = scalar(a, type=type)
    if not isinstance(b, Constant):
        b = scalar(b, type=type)
    return create_pair(a, b)


@typing.overload
def matrix(data: Any = None, *, type: DataType = None) -> Matrix:
    ...


@typing.overload
def matrix(*, type: DataType = None, rows: int = 1, cols: int = 1, columns_capacity: int = 1, default: Any = None) -> Matrix:
    ...


def matrix(
    data: Any = None,
    *,
    type: DataType = None,
    rows: int = 1,
    cols: int = 1,
    columns_capacity: int = 1,
    default: Any = None
) -> Matrix:
    if data is not None:
        return convert_matrix(data, type)
    return create_matrix(type, rows, cols, columns_capacity, default)


@typing.overload
def set(data: Any = None, *, type: DataType = None) -> Set:
    ...


@typing.overload
def set(*, type: DataType = None, capacity: int = 0) -> Set:
    ...


def set(data: Any = None, *, type: DataType = None, capacity: int = 0) -> Set:
    if data is not None:
        return convert_set(data, type)
    return create_set(type, capacity)


@typing.overload
def dictionary(
    data: Any = None,
    *,
    key_type: DataType = None,
    val_type: DataType = None,
    ordered: bool = True,
) -> Dictionary:
    ...


@typing.overload
def dictionary(
    *,
    keys: Any = None,
    vals: Any = None,
    key_type: DataType = None,
    val_type: DataType = None,
    ordered: bool = True,
) -> Dictionary:
    ...


@typing.overload
def dictionary(
    *,
    key_type: DataType = None,
    val_type: DataType = None,
    ordered: bool = True,
) -> Dictionary:
    ...


def dictionary(
    data: Any = None,
    *,
    keys: Any = None,
    vals: Any = None,
    key_type: DataType = None,
    val_type: DataType = None,
    ordered: bool = True,
) -> Dictionary:
    if data is not None:
        # func1
        return convert_dictionary(data, key_type, val_type, ordered)
    if keys is not None and vals is not None:
        # func2
        return create_dictionary_with_key_and_val(keys, vals, key_type, val_type, ordered)
    # func3
    return create_dictionary(key_type, val_type, ordered)


@typing.overload
def table(data: Any = None, *, types: TypeDict = None) -> Table:
    ...


@typing.overload
def table(data: Any = None, *, names: List[str] = None, types: TypeList = None) -> Table:
    ...


@typing.overload
def table(*, types: TypeDict = None, size: int = 0, capacity: int = 0) -> Table:
    ...


@typing.overload
def table(*, names: List[str] = None, types: TypeList = None, size: int = 0, capacity: int = 0) -> Table:
    ...


def table(
    data: Any = None,
    *,
    names: List[str] = None,
    types: Union[TypeDict, TypeList] = None,
    size: int = 0,
    capacity: int = 0,
) -> Table:
    if data is not None:
        if names is None and types is None:
            return convert_table(data, dict())
        if isinstance(names, list) and isinstance(types, list):
            if len(names) != len(types):
                raise ConvertError("The number of column names should be the same as the number of data types.")
            new_types = dict()
            for n, t in zip(names, types):
                new_types[n] = t
            return convert_table(data, new_types)
        elif isinstance(types, dict):
            return convert_table(data, types)
        elif types is None:
            return convert_table(data, dict())
        else:
            raise ConvertError("Invalid names or types.")
    if names is None and types is None:
        raise ConvertError("Can't create Table with empty names and empty types.")
    if isinstance(names, list) and isinstance(types, list):
        if len(names) != len(types):
            raise ConvertError("The number of column names should be the same as the number of data types.")
        new_types = dict()
        for n, t in zip(names, types):
            new_types[n] = t
        types = new_types
    if isinstance(types, dict):
        return create_table(types, size, capacity)
    if types is None:
        raise ConvertError("Can't create Table with empty names and empty types.")
    raise ConvertError("Can't create Table with invalid names or types.")


Constant.isNull = F_isNull
Constant.rows = F_rows
Constant.cols = F_cols

Vector.rowRank = F_rowRank
Vector.rename_ = F_rename_

Set.keys = F_keys

Dictionary.keys = F_keys
Dictionary.values = F_values

Table.schema = F_schema
Table.keys = F_keys
Table.values = F_values
Table.head = F_head
Table.tail = F_tail
Table.count = F_count


__all__ = [
    "Constant",
    "Scalar",
    "Vector",
    "Matrix",
    "Set",
    "Dictionary",
    "Table",

    "AnyVector",
    "ArrayVector",

    "Void",
    "NULL",
    "DFLT",
    "Nothing",
    "Bool",
    "Char",
    "Short",
    "Int",
    "Long",
    "Float",
    "Double",
    "String",
    "Blob",
    "Date",
    "Month",
    "Time",
    "Minute",
    "Second",
    "DateTime",
    "Timestamp",
    "NanoTime",
    "NanoTimestamp",
    "DateHour",
    "Uuid",
    "Int128",
    "Ipaddr",
    "Duration",
    "MetaCode",
    "Decimal32",
    "Decimal64",
    "Decimal128",
    "FunctionDef",

    "partial",
    "scalar",
    "vector",
    "any_vector",
    "array_vector",
    "pair",
    "matrix",
    "set",
    "dictionary",
    "table",
]
