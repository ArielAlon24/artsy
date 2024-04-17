import struct
from ..handlers.logging_handler import LoggingHandler

logger = LoggingHandler.create_logger(__name__)


class _DibHeader:
    HEADER_SIZE: int = 40
    COLOR_PLANES: int = 1
    COMPRESSION_METHOD: int = 0
    PALETTE_COLORS: int = 0
    IMPORTANT_COLORS: int = 0
    FORMAT: str = "<IiiHHIiiIIi"

    def __init__(
        self, width: int, height: int, resolution: int = 2835, bit: int = 24
    ) -> None:
        self._size = self.HEADER_SIZE
        self._width = width
        self._height = height
        self._color_planes = self.COLOR_PLANES
        self._bit = bit
        self._compression_method = self.COMPRESSION_METHOD
        self._image_size = 3 * width * height
        self._horizontal_resolution = resolution
        self._vertical_resolution = resolution
        self._palette_colors = self.PALETTE_COLORS
        self._important_colors = self.IMPORTANT_COLORS

    def make(self) -> bytes:
        result = struct.pack(
            self.FORMAT,
            self._size,
            self._width,
            self._height,
            self._color_planes,
            self._bit,
            self._compression_method,
            self._image_size,
            self._horizontal_resolution,
            self._vertical_resolution,
            self._palette_colors,
            self._important_colors,
        )
        logger.debug(f"{self.__class__.__name__} has completed packing.")
        return result
