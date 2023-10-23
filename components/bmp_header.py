from utils.bytes import to_bytes


class _BmpHeader:
    HEADER_SIZE: int = 54

    def __init__(self, width: int, height: int) -> None:
        self._type: bytearray = bytearray(b"BM")
        self._file_size = to_bytes(self.HEADER_SIZE * 3 * width * height)
        self._reserved = to_bytes(0)
        self._offset = to_bytes(self.HEADER_SIZE)

    def make(self) -> bytes:
        return self._type + self._file_size + self._reserved + self._offset
