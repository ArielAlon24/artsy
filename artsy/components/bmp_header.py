import struct
from .component import Component
from ..handlers.logging_handler import LoggingHandler

logger = LoggingHandler.create_logger(__name__)


class _BmpHeader(Component):
    HEADER_SIZE: int = 54
    FORMAT: str = "<2sI2I"

    def __init__(self, width: int, height: int) -> None:
        self._type: bytes = b"BM"
        self._file_size: int = self.HEADER_SIZE + 3 * width * height
        self._reserved: int = 0
        self._offset: int = self.HEADER_SIZE

    def __bytes__(self) -> bytes:
        result = struct.pack(
            self.FORMAT, self._type, self._file_size, self._reserved, self._offset
        )
        logger.debug(f"{self.__class__.__name__} has completed packing.")
        return result
