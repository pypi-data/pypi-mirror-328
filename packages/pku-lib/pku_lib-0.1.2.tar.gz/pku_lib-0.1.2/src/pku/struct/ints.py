UINT8_MAX = 0xFF
UINT16_MAX = 0xFFFF
UINT32_MAX = 0xFFFF_FFFF


def uint8(x: int, /, strict: bool = True) -> int:
    value = x & UINT8_MAX

    if strict and value != x:
        raise ValueError(f"uint8 requires 0 <= number <= {UINT8_MAX}")

    return value


def uint16(x: int, /, strict: bool = True) -> int:
    value = x & UINT16_MAX

    if strict and value != x:
        raise ValueError(f"uint16 requires 0 <= number <= {UINT16_MAX}")

    return value


def uint32(x: int, /, strict: bool = True) -> int:
    value = x & UINT32_MAX

    if strict and value != x:
        raise ValueError(f"uint32 requires 0 <= number <= {UINT32_MAX}")

    return value
