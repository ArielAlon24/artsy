import struct


class _BmpHeader:
    HEADER_SIZE: int = 54
    FORMAT: str = "<2sI2I"

    def __init__(self, width: int, height: int) -> None:
        self._type: bytes = b"BM"
        self._file_size: int = self.HEADER_SIZE + 3 * width * height
        self._reserved: int = 0
        self._offset: int = self.HEADER_SIZE

    def make(self) -> bytes:
        return struct.pack(
            self.FORMAT, self._type, self._file_size, self._reserved, self._offset
        )
