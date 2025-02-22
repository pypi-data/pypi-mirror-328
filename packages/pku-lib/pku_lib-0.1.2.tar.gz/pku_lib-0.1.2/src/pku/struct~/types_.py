import abc
import pathlib
import typing as t
from typing import override

import construct_typed as cst


class BinaryStruct[T: cst.DataclassMixin](abc.ABC):
    struct: cst.DataclassStruct[T]
    _data: T

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


class StrictEnumBase(cst.EnumBase):
    """Modify `EnumBase` to disable automatic generation of missing values."""

    @override
    @classmethod
    def _missing_(cls, value: object) -> None:
        return None
