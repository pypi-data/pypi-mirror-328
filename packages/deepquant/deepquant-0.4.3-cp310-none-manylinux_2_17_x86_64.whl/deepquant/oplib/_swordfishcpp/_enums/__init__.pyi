from swordfish._swordfishcpp import EnumInt
from swordfish._swordfishcpp import DataType, DataForm, ObjectType, LogLevel


def create_type_enum(type: int, exparam: int) -> DataType: ...


def create_array_type_enum(sub_type: DataType) -> DataType: ...


def create_form_enum(form: int) -> DataForm: ...


ALL: EnumInt
FIRST: EnumInt
LAST: EnumInt
NONE: EnumInt

VOID: DataType
BOOL: DataType
CHAR: DataType
SHORT: DataType
INT: DataType
LONG: DataType
DATE: DataType
MONTH: DataType
TIME: DataType
MINUTE: DataType
SECOND: DataType
DATETIME: DataType
TIMESTAMP: DataType
NANOTIME: DataType
NANOTIMESTAMP: DataType
FLOAT: DataType
DOUBLE: DataType
SYMBOL: DataType
STRING: DataType
UUID: DataType
FUNCTIONDEF: DataType
HANDLE: DataType
CODE: DataType
DATASOURCE: DataType
RESOURCE: DataType
ANY: DataType
DICTIONARY: DataType
DATEHOUR: DataType
IPADDR: DataType
INT128: DataType
BLOB: DataType
COMPLEX: DataType
POINT: DataType
DURATION: DataType
OBJECT: DataType

SCALAR: DataForm
VECTOR: DataForm
PAIR: DataForm
MATRIX: DataForm
SET: DataForm
DICT: DataForm
TABLE: DataForm

VAR: ObjectType
SHARED: ObjectType
DEF: ObjectType

DEBUG: LogLevel
INFO: LogLevel
ERROR: LogLevel
WARNING: LogLevel
