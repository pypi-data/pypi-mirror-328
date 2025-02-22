import abc
import pathlib
import typing as t

import construct as cs
import construct_typed as cst


def ensure[T](type_: type[T], value: object, /) -> T:
    """
    Assert that an object is the type you expect it to be.

    Useful when working with objects with overly permissive types.
    Raises `TypeError` if `value` is not the expected type.
    """
    if not isinstance(value, type_):
        raise TypeError(f"expected type {type_}, but got {type(value)}")

    return value


class StrictEnumBase(cst.EnumBase):
    """Modify `EnumBase` to disable automatic generation of missing values."""

    @t.override
    @classmethod
    def _missing_(cls, value: object) -> None:
        return None


class BinaryStruct(abc.ABC):
    struct: cs.Struct
    _data: cs.Container[object]

    def __init__(self, data: bytearray | bytes) -> None:
        self._data = self.struct.parse(data)

    def __bytes__(self) -> bytes:
        return self.struct.build(self._data)

    @classmethod
    def read_file(cls, file: str | pathlib.Path) -> t.Self:
        with open(file, mode="rb") as f:
            data = f.read()

        return cls(data)

    def write_file(self, file: str | pathlib.Path) -> int:
        data = bytes(self)

        with open(file, mode="wb") as f:
            return f.write(data)
