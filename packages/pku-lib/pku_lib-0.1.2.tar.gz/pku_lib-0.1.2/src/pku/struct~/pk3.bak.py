__all__ = ["Box", "Party"]
from typing import Self, cast, final

from construct import (
    Byte,
    Bytes,
    Container,
    Int16ul,
    Int32ul,
    PaddedString,
    Struct,
)


class PkBox3:
    # https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_substructures_(Generation_III)
    # https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_III)
    # https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_III)

    # TODO: Add encrypted data structure.
    encrypted: Struct = Struct("encrypted" / Bytes(48))
    binary: Struct = Struct(
        "pid" / Int32ul,
        "tid" / Int16ul,
        "sid" / Int16ul,
        "nickname" / Bytes(10),
        "language" / Byte,
        "flags" / Byte,
        "ot" / PaddedString(7, "utf-8"),
        "markings" / Byte,
        "checksum" / Int16ul,
        "_padding" / Int16ul,
        encrypted,
    )

    def __init__(self, data: bytes) -> None:
        self.data: bytes = data
        self._container: Container[object] = self.binary.parse(self.data)

    @classmethod
    def from_file(cls, file: str) -> Self:
        with open(file, mode="rb") as f:
            data = f.read()

        return cls(data)

    @property
    def pid(self) -> int:
        return cast(int, self._container.pid)

    @property
    def tid(self) -> int:
        return cast(int, self._container.tid)

    @property
    def sid(self) -> int:
        return cast(int, self._container.sid)

    @property
    def ot(self) -> bytes:
        return cast(bytes, self._container.ot)


@final
class PkParty3(PkBox3):
    binary = Struct(
        PkBox3.binary,
        "status" / Int32ul,
        "level" / Byte,
        "mailid" / Byte,
        "hp" / Int16ul,
        "hp_total" / Int16ul,
        "attack" / Int16ul,
        "defense" / Int16ul,
        "speed" / Int16ul,
        "special_attack" / Int16ul,
        "special_defense" / Int16ul,
    )


@final
class Box:
    Pk3 = PkBox3


@final
class Party:
    Pk3 = PkParty3
