from typing import TypeVar, Generic, get_args


T = TypeVar('T')


class _ParamAlias:
    name: str


class Alias(Generic[T]):
    def __class_getitem__(cls, item):
        name = get_args(item)[0]
        return type(name, (_ParamAlias,), {'name': name})
