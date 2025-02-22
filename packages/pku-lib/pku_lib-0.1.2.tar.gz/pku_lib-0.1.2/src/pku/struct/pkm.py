import abc
import typing as t

import pku.struct.ints as ints
import pku.struct.types_ as types_

G7TID_MAX = 10**6
G7SID_MAX = ints.UINT32_MAX // G7TID_MAX


class Pkm(types_.BinaryStruct, abc.ABC):
    generation: t.Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]


class TidSid(types_.BinaryStruct):
    @property
    def tidsid(self) -> int:
        return types_.ensure(int, self._data.tidsid)

    @tidsid.setter
    def tidsid(self, tidsid: int) -> None:
        self._data["tidsid"] = ints.uint32(tidsid)

    @property
    def tid16(self) -> int:
        return self.tidsid & 0xFFFF

    @tid16.setter
    def tid16(self, tid: int) -> None:
        tid = ints.uint16(tid)
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
        sid = ints.uint16(sid)
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
