from __future__ import annotations
from decimal import Decimal
from typing import overload, List, Dict, Any, Union
from types import FunctionType
import numpy as np
import pandas as pd

from swordfish.function import DFLT


def sw_init(args: List[str]) -> None: ...


def sw_uninit() -> None: ...


EXPARAM_DEFAULT = -0x7fffffff - 1


class Session:
    """Swordfish sessions for script execution and function calls."""
    pass


class ConnectionImpl:
    def __enter__(self) -> ConnectionImpl: ...
    def __exit__(self, exc_type, exc_value, traceback): ...
    def session(self) -> Session: ...


class BaseConnectionImpl(ConnectionImpl):
    pass


class DefaultSessionConnectionImpl(BaseConnectionImpl):
    @classmethod
    def create() -> DefaultSessionConnectionImpl: ...


class Constant:
    """The base class for swordfish objects.
    All data types (such as `Int`, `String`) and data
    forms (such as `Vector`, `Table`) are from this class.
    """
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __int__(self) -> int: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, o) -> Bool: ...
    def __neg__(self) -> Constant: ...
    def __abs__(self) -> Constant: ...
    def __add__(self, o: Union[Constant, Any]) -> Constant: ...
    def __radd__(self, o: Union[Constant, Any]) -> Constant: ...
    def __sub__(self, o: Union[Constant, Any]) -> Constant: ...
    def __rsub__(self, o: Union[Constant, Any]) -> Constant: ...
    def __mul__(self, o: Union[Constant, Any]) -> Constant: ...
    def __rmul__(self, o: Union[Constant, Any]) -> Constant: ...
    def __truediv__(self, o: Union[Constant, Any]) -> Constant: ...
    def __rtruediv__(self, o: Union[Constant, Any]) -> Constant: ...
    def __floordiv__(self, o: Union[Constant, Any]) -> Constant: ...
    def __rfloordiv__(self, o: Union[Constant, Any]) -> Constant: ...
    def __mod__(self, o: Union[Constant, Any]) -> Constant: ...
    def __rmod__(self, o: Union[Constant, Any]) -> Constant: ...
    def __pow__(self, o: Union[Constant, Any]) -> Constant: ...
    def __rpow__(self, o: Union[Constant, Any]) -> Constant: ...
    def __lt__(self, o: Union[Constant, Any]) -> Constant: ...
    def __le__(self, o: Union[Constant, Any]) -> Constant: ...
    def __eq__(self, o: Union[Constant, Any]) -> Constant: ...
    def __ne__(self, o: Union[Constant, Any]) -> Constant: ...
    def __gt__(self, o: Union[Constant, Any]) -> Constant: ...
    def __ge__(self, o: Union[Constant, Any]) -> Constant: ...
    def __and__(self, o: Union[Constant, Any]) -> Constant: ...
    def __rand__(self, o: Union[Constant, Any]) -> Constant: ...
    def __or__(self, o: Union[Constant, Any]) -> Constant: ...
    def __ror__(self, o: Union[Constant, Any]) -> Constant: ...
    def __xor__(self, o: Union[Constant, Any]) -> Constant: ...
    def __rxor__(self, o: Union[Constant, Any]) -> Constant: ...

    def form(self) -> DataForm:
        """Retrieve the data form (`DataForm`) of a `Constant` object.

        Returns:
            DataForm: Represents the data format.
        """
        ...

    def type(self) -> DataType:
        """Retrieve the data type (`DataType`) of a `Constant` object.

        Returns:
            DataType: Represents the data type.
        """
        ...

    def isNull(self) -> Constant:
        """Check if object is a NULL value or contains NULL elements.

        Returns:
            Constant: True if an element is NULL.
                      For non-scalar input, the result has the same shape as the input.
        """
        ...

    def rows(self) -> Int:
        """Return the number of rows

        Returns:
            Int: The number of rows
        """
        ...

    def cols(self) -> Int:
        """Return the number of columns

        Returns:
            Int: The number of columns
        """
        ...


class Iterator(Constant):
    """Iterator for Constant objects.
    It provides a standard way to iterate over the elements any swordfish object.
    """
    def __iter__(self) -> Iterator: ...
    def __next__(self) -> Constant: ...


class Scalar(Constant):
    """Superclass for Scalar types like `Int`, `String`, and `Float`,
    inheriting from `Constant`, representing a single variable.
    """
    def to_python(self) -> Any:
        """Convert the Scalar to a python type.

        Returns:
            Any: A python object that represents the same value as the Scalar.
        """
        ...


class EnumInt(Scalar):
    """A base class for enumerated integer constants.
    This class serves as the parent class for various enumeration types
    such as DataType and DataForm.
    """
    def __init__(self, desc: str, val: int, type: int) -> None: ...
    def __int__(self) -> int: ...
    def __getitem__(self) -> Any: ...
    def set_function(self, func): ...


class DataType(EnumInt):
    """Enumeration defining swordfish data types such as INT, FLOAT, etc.
    It inherits from EnumInt.
    The data type of a Constant object can be retrieved using the Constant.type() method.
    """
    ...


class DataForm(EnumInt):
    """Enumeration defining swordfish data forms such as SCALAR, VECTOR, etc.
    It inherits from EnumInt.
    The data form of a Constant object can be retrieved using the Constant.form() method.
    """
    ...


class ObjectType(EnumInt):
    """Enumeration defining swordfish object types, including VAR (local variable),
    SHARED (shared variable), and DEF (function definition).
    """
    ...


class LogLevel(EnumInt):
    ...


class FunctionDef(Constant):
    """Represents a function definition, inherenting from the Scalar class.
    It provides a way to treat function definitions as Scalars
    """
    @overload
    def __init__(self, func: FunctionType, *, name: str = "<lambda>", aggregation: bool = None):
        ...

    @overload
    def __init__(self, code: str):
        ...

    def __copy__(self) -> FunctionDef: ...
    def __deepcopy__(self) -> FunctionDef: ...
    def __get__(self): ...
    def __call__(self, *args, **kwargs) -> Constant: ...
    def set_meta(self, signature, alias) -> None: ...


class Vector(Constant):
    """Represents a one-dimensional vector, inheriting from the Constant class."""
    def __getitem__(self, index) -> Scalar: ...
    def __setitem__(self, index, value) -> None: ...
    def __iter__(self) -> Iterator: ...

    @classmethod
    def from_list(cls, data: list, type: DataType = None) -> Vector:
        """Construct a Vector object from a python list.

        Args:
            data (list): The input data as a python list instance.
            type (DataType, optional): An enumeration value from the DataType enum,
                                       specifying the target data type for the vector elements.

        Returns:
            Vector: A new Vector object containing the data from the input list,
                    converted to the specified data type.
        """
        ...

    @classmethod
    def from_tuple(cls, data: tuple, type: DataType = None) -> Vector:
        """Construct a Vector object from a python tuple.

        Args:
            data (tuple): The input data as a python tuple instance.
            type (DataType, optional): An enumeration value from the DataType enum,
                                       specifying the target data type for the vector elements.

        Returns:
            Vector: A new Vector object containing the data from the input tuple,
                    converted to the specified data type.
        """
        ...

    @classmethod
    def from_numpy(cls, data: np.ndarray, type: DataType = None) -> Vector:
        """Construct a Vector object from a numpy array.

        Args:
            data (np.ndarray): The input data as a 1-dimensional ndarray.
            type (DataType, optional): An enumeration value from the DataType enum,
                                       specifying the target data type for the vector elements.

        Returns:
            Vector: A new Vector object containing the data from the input numpy array.
        """
        ...

    def to_numpy(self) -> np.ndarray:
        """Convert the Vector object to a numpy ndarray containing all the elements
        of the Vector object.

        Returns:
            np.ndarray: A new 1-dimensional NumPy array containing the elements of the Vector.
        """
        ...

    def to_list(self) -> list:
        """Convert the Vector object to a python list containing all the elements
        of the Vector object.

        Returns:
            list: A new python list containing the elements of the Vector.
        """
        ...


class AnyVector(Vector):
    def __getitem__(self, index) -> Constant: ...
    def __setitem__(self, index, value) -> None: ...

    @classmethod
    def from_list(cls, data: list) -> AnyVector:
        ...

    @classmethod
    def from_tuple(cls, data: tuple) -> AnyVector:
        ...

    @classmethod
    def from_numpy(cls, data: np.ndarray) -> AnyVector:
        ...

    def to_numpy(self) -> np.ndarray:
        ...

    def to_list(self) -> list:
        ...


class ArrayVector(Vector):
    def __getitem__(self, index) -> Vector: ...
    def __setitem__(self, index, value) -> None: ...

    @classmethod
    def from_list(self, data: list, type: DataType = None) -> ArrayVector: ...
    @classmethod
    def from_tuple(self, data: tuple, type: DataType = None) -> ArrayVector: ...
    @classmethod
    def from_numpy(cls, data: np.ndarray, type: DataType = None) -> ArrayVector: ...


class Pair(Constant):
    def __getitem__(self, index) -> Scalar: ...
    def __setitem__(self, index, value) -> None: ...
    def __iter__(self) -> Iterator: ...

    def to_list(self) -> list: ...


class Matrix(Vector):
    def __getitem__(self, index) -> Constant: ...
    def __setitem__(self, index, value) -> None: ...

    @classmethod
    def from_numpy(cls, data: np.ndarray, type: DataType = None) -> Matrix: ...
    def to_numpy(self) -> np.ndarray: ...
    def to_list(self) -> list: ...


class Set(Constant):
    def __iter__(self) -> Iterator: ...

    @classmethod
    def from_set(cls, data: set, type: DataType = None) -> Set: ...
    def to_set(self) -> set: ...


class Dictionary(Constant):
    def __getitem__(self, index) -> Constant: ...
    def __setitem__(self, index, value) -> None: ...
    def __iter__(self) -> Iterator: ...

    @classmethod
    def from_dict(cls, data: dict, *, key_type: DataType = None, val_type: DataType = None) -> Dictionary: ...
    def to_dict(self) -> dict: ...
    def keys(self) -> Constant: ...
    def values(self) -> Constant: ...
    def items(self) -> DictionaryItems: ...


class DictionaryItems:
    def __iter__(self) -> DictionaryItemsIterator: ...


class DictionaryItemsIterator:
    def __next__(self) -> AnyVector: ...


class Table(Constant):
    def __getitem__(self, index) -> Constant: ...
    def __setitem__(self, index, value) -> None: ...
    def __iter__(self) -> Iterator: ...

    @classmethod
    def from_pandas(cls, data: pd.DataFrame, *, types: Dict[str, DataType] = None) -> Table: ...
    def to_pandas(self) -> pd.DataFrame: ...
    def types(self) -> Dict[str, DataType]: ...
    def schema(self) -> Dictionary: ...
    def head(self, n: Constant = DFLT) -> Constant: ...
    def tail(self, n: Constant = DFLT) -> Constant: ...
    def count(self) -> Constant: ...
    def keys(self) -> Constant: ...
    def values(self) -> Constant: ...


class Void(Scalar):
    VOID_VALUE: Void
    NULL_VALUE: Void
    DFLT_VALUE: Void
    def __init__(self) -> None: ...


class Bool(Scalar):
    NULL_VALUE: Bool
    @overload
    def __init__(self, data: bool) -> None: ...

    @overload
    def __init__(self) -> None: ...


class Char(Scalar):
    NULL_VALUE: Char
    @overload
    def __init__(self, data: str) -> None: ...

    @overload
    def __init__(self, data: int) -> None: ...

    @overload
    def __init__(self) -> None: ...


class Short(Scalar):
    NULL_VALUE: Short
    @overload
    def __init__(self, data: int) -> None: ...

    @overload
    def __init__(self) -> None: ...


class Int(Scalar):
    NULL_VALUE: Int
    @overload
    def __init__(self, data: int) -> None: ...

    @overload
    def __init__(self) -> None: ...


class Long(Scalar):
    NULL_VALUE: Long
    @overload
    def __init__(self, data: int) -> None: ...

    @overload
    def __init__(self) -> None: ...


class Float(Scalar):
    NULL_VALUE: Float
    @overload
    def __init__(self, data: float) -> None: ...

    @overload
    def __init__(self) -> None: ...


class Double(Scalar):
    NULL_VALUE: Double
    @overload
    def __init__(self, data: float) -> None: ...

    @overload
    def __init__(self) -> None: ...


class String(Scalar):
    NULL_VALUE: String
    @overload
    def __init__(self, data: str) -> None: ...

    @overload
    def __init__(self) -> None: ...


class Blob(Scalar):
    NULL_VALUE: Blob
    @overload
    def __init__(self, data: str) -> None: ...
    @overload
    def __init__(self) -> None: ...


class Date(Scalar):
    NULL_VALUE: Date
    @overload
    def __init__(self, data: int) -> None: ...
    @overload
    def __init__(self) -> None: ...


class Month(Scalar):
    NULL_VALUE: Month
    @overload
    def __init__(self, data: int) -> None: ...
    @overload
    def __init__(self) -> None: ...


class Time(Scalar):
    NULL_VALUE: Time
    @overload
    def __init__(self, data: int) -> None: ...
    @overload
    def __init__(self) -> None: ...


class Minute(Scalar):
    NULL_VALUE: Minute
    @overload
    def __init__(self, data: int) -> None: ...
    @overload
    def __init__(self) -> None: ...


class Second(Scalar):
    NULL_VALUE: Second
    @overload
    def __init__(self, data: int) -> None: ...
    @overload
    def __init__(self) -> None: ...


class DateTime(Scalar):
    NULL_VALUE: DateTime
    @overload
    def __init__(self, data: int) -> None: ...
    @overload
    def __init__(self) -> None: ...


class Timestamp(Scalar):
    NULL_VALUE: Timestamp
    @overload
    def __init__(self, data: int) -> None: ...
    @overload
    def __init__(self) -> None: ...


class NanoTime(Scalar):
    NULL_VALUE: NanoTime
    @overload
    def __init__(self, data: int) -> None: ...
    @overload
    def __init__(self) -> None: ...


class NanoTimestamp(Scalar):
    NULL_VALUE: "NanoTimestamp"
    @overload
    def __init__(self, data: int) -> None: ...
    @overload
    def __init__(self) -> None: ...


class DateHour(Scalar):
    NULL_VALUE: DateHour
    @overload
    def __init__(self, data: int) -> None: ...
    @overload
    def __init__(self) -> None: ...


class Uuid(Scalar):
    NULL_VALUE: Uuid


class Int128(Scalar):
    NULL_VALUE: Int128


class Ipaddr(Scalar):
    NULL_VALUE: Ipaddr


class Duration(Scalar):
    ...


class MetaCode(Scalar):
    ...


class Decimal32(Scalar):
    NULL_VALUE: Decimal32
    @overload
    def __init__(self, data: int, scale: int = EXPARAM_DEFAULT) -> None: ...
    @overload
    def __init__(self, data: Decimal, scale: int = EXPARAM_DEFAULT) -> None: ...


class Decimal64(Scalar):
    NULL_VALUE: Decimal64
    @overload
    def __init__(self, data: int, scale: int = EXPARAM_DEFAULT) -> None: ...
    @overload
    def __init__(self, data: Decimal, scale: int = EXPARAM_DEFAULT) -> None: ...


class Decimal128(Scalar):
    NULL_VALUE: Decimal128
    @overload
    def __init__(self, data: int, scale: int = EXPARAM_DEFAULT) -> None: ...
    @overload
    def __init__(self, data: Decimal, scale: int = EXPARAM_DEFAULT) -> None: ...
