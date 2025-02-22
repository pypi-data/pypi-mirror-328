import enum
import typing as t
from typing import override

import construct as cs
import construct_typed as cst

import pku.struct.pkm as pkm
import pku.struct.types_ as types_


@enum.unique
class Language3(types_.StrictEnumBase):
    JPN = 1
    ENG = 2
    FRE = 3
    ITA = 4
    GER = 5
    SPA = 7

    @override
    def __str__(self) -> str:
        return self.name


@t.final
class Pk3(pkm.Pkm, pkm.TidSid):
    generation = 3
    struct = cs.Struct(
        "pid" / cs.Int32ul,
        "tidsid" / cs.Int32ul,
        # TODO: create encoding adapter.
        # https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_III)
        "nickname" / cs.Bytes(10),
        "language" / cst.TEnum(cs.Byte, Language3),
        "flags"
        / cs.BitStruct(
            "bad_egg" / cs.Flag,
            "has_species" / cs.Flag,
            "use_egg_name" / cs.Flag,
            "block_box_rs" / cs.Flag,
            cs.Padding(4),
        ),
        # TODO: create encoding adapter.
        "ot" / cs.Bytes(7),
        "markings"
        / cs.BitStruct(
            "circle" / cs.Flag,
            "square" / cs.Flag,
            "triangle" / cs.Flag,
            "heart" / cs.Flag,
            cs.Padding(4),
        ),
        "checksum" / cs.Int16ul,
        cs.Padding(2),
        # TODO: create encryption adapter.
        # # https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_substructures_(Generation_III)
        "data" / cs.Bytes(48),
        "party"
        / cs.Optional(
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
        ),
    )

    def in_party(self) -> bool:
        return self._data.party is not None

    @property
    def party(self) -> cs.Container[int]:
        if not self.in_party():
            raise AttributeError("party data is not available")

        return t.cast(cs.Container[int], self._data.party)

    @property
    def nickname(self) -> bytes:
        return types_.ensure(bytes, self._data.language)

    # TODO: nickname setter

    @property
    def language(self) -> int:
        return types_.ensure(Language3, self._data.language)

    @language.setter
    def language(self, language: int) -> None:
        self._data["language"] = Language3(language)

    @property
    def level(self) -> int:
        # There may be some complexities with stored level and stored EXP.
        return self.party.level

    # TODO: level setter
