from ..color import Color
from .component import Component
from ..handlers.logging_handler import LoggingHandler

logger = LoggingHandler.create_logger(__name__)


class _PixelTable(Component):
    ALIGNMENT = 4

    def __init__(self, width: int, height: int, color: Color = Color.black()) -> None:
        self.width = width
        self.height = height
        self.row_size = (
            self.ALIGNMENT - (3 * self.width) % self.ALIGNMENT
        ) % self.ALIGNMENT + 3 * self.width
        self.image_data = bytearray(self.height * self.row_size)
        for y in range(self.height):
            for x in range(self.width):
                self.set(x, y, color)

    def set(self, x: int, y: int, color: Color) -> None:
        offset = y * self.row_size + x * 3
        self.image_data[offset : offset + 3] = bytes(color)

    def get(self, x: int, y: int) -> Color:
        offset = y * self.row_size + x * 3
        return Color.from_bytes(self.image_data[offset : offset + 3])

    def __bytes__(self) -> bytes:
        logger.debug(f"{self.__class__.__name__} has completed packing.")
        return bytes(self.image_data)
