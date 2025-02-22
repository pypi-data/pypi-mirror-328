from __future__ import annotations

import dataclasses
import enum
import typing as t
from typing import override

import construct as cs
import construct_typed as cst

import pku.struct.pkm as pkm
from pku.struct.types_ import StrictEnumBase


@enum.unique
class Language3(StrictEnumBase):
    JPN = 1
    ENG = 2
    FREE = 3
    ITA = 4
    GER = 5
    SPA = 7

    @override
    def __str__(self) -> str:
        return self.name


@dataclasses.dataclass
class Pk3Markings(cst.DataclassMixin):
    circle: bool = cst.csfield(cs.Flag)
    square: bool = cst.csfield(cs.Flag)
    triangle: bool = cst.csfield(cs.Flag)
    heart: bool = cst.csfield(cs.Flag)
    cst.csfield(cs.Padding(4))


@dataclasses.dataclass
class Pk3Struct(cst.DataclassMixin):
    pid: int = cst.csfield(cs.Int32ul)
    tidsid: int = cst.csfield(cs.Int32ul)
    nickname: bytes = cst.csfield(cs.Bytes(10))
    language: Language3 = cst.csfield(cst.TEnum(cs.Byte, Language3))
    flags: cs.Container[bool] = cst.csfield(
        cs.BitStruct(
            "bad_egg" / cs.Flag,
            "has_species" / cs.Flag,
            "use_egg_name" / cs.Flag,
            "block_box_rs" / cs.Flag,
            cs.Padding(4),
        )
    )
    ot: bytes = cst.csfield(cs.Bytes(7))
    # markings: Pk3Markings = cst.csfield(cst.DataclassBitStruct(Pk3Markings))
    markings: cs.Container[bool] = cst.csfield(
        cs.BitStruct(
            "circle" / cs.Flag,
            "square" / cs.Flag,
            "triangle" / cs.Flag,
            "heart" / cs.Flag,
            cs.Padding(4),
        )
    )
    checksum: int = cst.csfield(cs.Int16ul)
    _: None = cst.csfield(cs.Padding(2))
    data: bytes = cst.csfield(cs.Bytes(48))
    party: cs.Container[int] | None = cst.csfield(
        cs.Optional(
            cs.Struct(
                "status" / cs.Int32ul,
                "level" / cs.Byte,
                "mailid" / cs.Byte,
                "hp" / cs.Int16ul,
                "hp_total" / cs.Int16ul,
                "attack" / cs.Int16ul,
                "defense" / cs.Int16ul,
                "speed" / cs.Int16ul,
                "special_attack" / cs.Int16ul,
                "special_defense" / cs.Int16ul,
            )
        )
    )


print(Pk3Struct)


@t.final
class Pk3(pkm.Pkm[Pk3Struct]):
    """
    Handle Pokémon data in mainline generation III titles.

    Source:
    https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_III)
    """

    generation = 3
    struct = cst.DataclassStruct(Pk3Struct)
    # struct = cs.Struct(
    #     "pid" / cs.Int32ul,
    #     "tidsid" / cs.Int32ul,
    #     # TODO: create encoding adapter.
    #     # https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_III)
    #     "nickname" / cs.Bytes(10),
    #     # "language" / Language3Adapter(construct.Byte),
    #     "language" / cs_t.TEnum(cs.Byte, Language3),
    #     "flags"
    #     / cs.BitStruct(
    #         "bad_egg" / cs.Flag,
    #         "has_species" / cs.Flag,
    #         "use_egg_name" / cs.Flag,
    #         "block_box_rs" / cs.Flag,
    #         cs.Padding(4),
    #     ),
    #     # TODO: create encoding adapter.
    #     "ot" / cs.Bytes(7),
    #     "markings"
    #     / cs.BitStruct(
    #         "circle" / cs.Flag,
    #         "square" / cs.Flag,
    #         "triangle" / cs.Flag,
    #         "heart" / cs.Flag,
    #         cs.Padding(4),
    #     ),
    #     "checksum" / cs.Int16ul,
    #     cs.Padding(2),
    #     # TODO: create encryption adapter.
    #     # # https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_substructures_(Generation_III)
    #     "data" / cs.Bytes(48),
    #     "party"
    #     / cs.Optional(
    #         cs.Struct(
    #             "status" / cs.Int32ul,
    #             "level" / cs.Byte,
    #             "mailid" / cs.Byte,
    #             "hp" / cs.Int16ul,
    #             "hp_total" / cs.Int16ul,
    #             "attack" / cs.Int16ul,
    #             "defense" / cs.Int16ul,
    #             "speed" / cs.Int16ul,
    #             "special_attack" / cs.Int16ul,
    #             "special_defense" / cs.Int16ul,
    #         )
    #     ),
    # )

    @property
    def language(self) -> int:
        return self._data.language

    @language.setter
    def language(self, language: int) -> None:
        self._data.language = Language3(language)
