# PKU - PKMN Utility Library.
# Copyright (C) 2025  Taylor Rodríguez
#
# PKU is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# PKU is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PKU.  If not, see <https://www.gnu.org/licenses/>.

"""API for interacting with PKM files without worrying about the details."""

import enum
import typing as t

import construct as cs
import construct_typed as cst


@t.final
class SizedOptional(cs.Select):
    """Accurately report the size of optional structs."""

    def __init__(self, struct: cs.Struct) -> None:
        """
        Initialise a new SizedOptional.

        Args:
            struct (cs.Struct): The structure to treat as optional.
        """
        self.struct = struct
        super().__init__(self.struct, cs.Pass)

    def _sizeof(self, *_: object) -> int:
        return self.struct.sizeof()


class StrictEnumBase(cst.EnumBase):
    """
    Stricter extension of `cst.EnumBase`.

    Disables the automatic generation of missing values. This behaviour was not
    ideal because it prevented using `cst.TEnum` for data validation.
    """

    @t.override
    @classmethod
    def _missing_(cls, value: object) -> None:
        return None


@enum.unique
class Language3(StrictEnumBase):
    """
    The language of origin determines which text encoding is used.

    Note: ID 6 is unused.
    """

    JPN = 1
    ENG = 2
    FRE = 3
    ITA = 4
    GER = 5
    SPA = 7

    @t.override
    def __str__(self) -> str:
        return self.name


pk3_party = cs.Struct(
    "status"
    / cs.BitsSwapped(
        cs.BitStruct(
            "sleep_turns" / cs.BitsInteger(3),
            "poison" / cs.Flag,
            "burn" / cs.Flag,
            "freeze" / cs.Flag,
            "paralysis" / cs.Flag,
            "bad_poison" / cs.Flag,
        )
    ),
    cs.Padding(3),
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

# https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_structure_(Generation_III)
pk3 = cs.Struct(
    "pid" / cs.Int32ul,
    "tidsid" / cs.Int32ul,
    # TODO: create encoding adapter.
    # https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_III)
    "nickname" / cs.Bytes(10),
    "language" / cst.TEnum(cs.Byte, Language3),
    "flags"
    / cs.BitsSwapped(
        cs.BitStruct(
            "bad_egg" / cs.Flag,
            "has_species" / cs.Flag,
            "use_egg_name" / cs.Flag,
            "block_box_rs" / cs.Flag,
            cs.Padding(4),
        )
    ),
    # TODO: create encoding adapter.
    "ot" / cs.Bytes(7),
    "markings"
    / cs.BitsSwapped(
        cs.BitStruct(
            "circle" / cs.Flag,
            "square" / cs.Flag,
            "triangle" / cs.Flag,
            "heart" / cs.Flag,
            cs.Padding(4),
        )
    ),
    "checksum" / cs.Int16ul,
    cs.Padding(2),
    # TODO: create encryption adapter.
    # https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_substructures_(Generation_III)
    "data" / cs.Bytes(48),
    "party" / SizedOptional(pk3_party),
)

PK3_PARTY_SIZE = pk3.sizeof()
PK3_SIZE = PK3_PARTY_SIZE - pk3_party.sizeof()
