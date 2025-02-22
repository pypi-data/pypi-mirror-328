__all__ = ["BinaryStruct", "PkmVC", "Pkm"]

import abc
import typing as t

import construct_typed as cst

from pku.struct.types_ import BinaryStruct

G7TID_MAX = 10**6
G7SID_MAX = 0xFFFF_FFFF // G7TID_MAX


class PkmParty(t.TypedDict):
    level: int
    hp_total: int
    attack: int
    defense: int
    speed: int


class PkmProtocol[T: PkmParty](abc.ABC, cst.DataclassMixin):
    """All Pokémon objects have the attributes of this class."""

    tid: int
    party: T | None


class PkmVcProtocol(PkmProtocol[PkmVcParty]):
    pass


class PkmnNewProtocol(PkmProtocol[PkmNewParty]):
    pid: int


PkmT = t.TypeVar("PkmT", bound=PkmProtocol[PkmParty])
PkmVcType = t.TypeVar("VcType", bound=PkmVcProtocol[PkmVcProtocol])
PkmNewType = t.TypeVar("PkmNewType", bound=Pkm)


class PkmBase(BinaryStruct[P]):
    pass


class PkmVc(PkmBase[Vc]):
    """
    Handle Pokémon data from the Virtual Console titles.
    """

    generation: t.Literal[1, 2]


class Pkm(BinaryStruct[P]):
    generation: t.Literal[3, 4, 5, 6, 7, 8, 9]

    @property
    def pid(self) -> int:
        return self._data.pid

    @pid.setter
    def pid(self, pid: int) -> None:
        # assert_uint32(pid)
        self._data.pid = pid

    @property
    def tidsid(self) -> int:
        return self._data.tidsid

    @tidsid.setter
    def tidsid(self, tidsid: int) -> None:
        # assert_uint32(tidsid)
        self._data.tidsid = tidsid

    @property
    def tid16(self) -> int:
        return self.tidsid & 0xFFFF

    @tid16.setter
    def tid16(self, tid: int) -> None:
        # assert_uint16(tid)
        self.tidsid = (self.sid16 << 16) | tid

    @property
    def tid(self) -> int:
        """Alias for `tid16`."""
        return self.tid16

    @tid.setter
    def tid(self, tid: int) -> None:
        self.tid16 = tid

    @property
    def sid16(self) -> int:
        return self.tidsid >> 16

    @sid16.setter
    def sid16(self, sid: int) -> None:
        # assert_uint16(sid)
        self.tidsid = (sid << 16) | self.tid16

    @property
    def sid(self) -> int:
        """Alias for `sid16`."""
        return self.sid16

    @sid.setter
    def sid(self, sid: int) -> None:
        self.sid16 = sid

    @property
    def g7tid(self) -> int:
        return self.tidsid % G7TID_MAX

    @g7tid.setter
    def g7tid(self, tid: int) -> None:
        if 0 <= tid < G7TID_MAX:
            self.tidsid = self.g7sid * G7TID_MAX + tid
            return

        raise ValueError(f"G7TID must be positive and less than {G7TID_MAX:,}")

    @property
    def g7sid(self) -> int:
        return self.tidsid // G7TID_MAX

    @g7sid.setter
    def g7sid(self, sid: int) -> None:
        if 0 <= sid < G7SID_MAX:
            self.tidsid = sid * G7TID_MAX + self.g7tid
            return

        raise ValueError(f"G7SID must be positive and less than {G7SID_MAX:,}")
