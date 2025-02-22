from pku.struct import pkm


class PkmParty1(pkm.PkmParty):
    """Party-specific gen I attributes."""

    special: int


class PkmProtocol1(pkm.PkmProtocol[PkmParty1]):
    """Attributes of generation I PKMN."""

    level: int
    hp_current: int
