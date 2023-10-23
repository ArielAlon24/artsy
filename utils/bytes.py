BYTE_ORDER: str = "little"


def to_bytes(number: int, size: int = 4) -> bytes:
    return number.to_bytes(size, BYTE_ORDER)
