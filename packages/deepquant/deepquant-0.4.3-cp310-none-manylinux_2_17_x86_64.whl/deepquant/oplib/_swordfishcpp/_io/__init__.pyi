from io import TextIOWrapper
from swordfish.data import Constant


def dump(obj: Constant, file: TextIOWrapper) -> None:
    """Serialize `Constant` object and writes the serialized data to
    writable file-like object (`TextIOWrapper`).

    Args:
        obj (Constant): The object to be serialized. Must be a `Constant` instance.
        file (TextIOWrapper): A writable file-like object.
    """
    ...


def load(file: TextIOWrapper) -> Constant:
    """Reads from a readable file-like object and
    deserializes the content to reconstruct a Constant object.

    Args:
        file (TextIOWrapper): A readable file-like object.

    Returns:
        Constant: The deserialized object.
    """
    ...


def dumps(obj: Constant) -> bytes:
    """serialize `Constant` object and writes the serialized data to
    `bytes`.

    Args:
        obj (Constant): The object to be serialized. Must be a `Constant` instance.

    Returns:
        bytes: representing the serialized form of `obj`.
    """
    ...


def loads(data: bytes) -> Constant:
    """Reads from a `bytes` object and deserializes the content
    to reconstruct a `Constant` object.

    Args:
        data (bytes): _description_

    Returns:
        Constant: _description_
    """
    ...
