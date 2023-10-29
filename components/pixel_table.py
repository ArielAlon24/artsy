from models.color import Color
from logging import Logger
from handlers.logging_handler import LoggingHandler

logger: Logger = LoggingHandler.create_logger(__name__)


class _PixelTable:
    def __init__(
        self, width: int, height: int, alignment: int = 4, color: Color = Color.black()
    ) -> None:
        self.width = width
        self.height = height
        self.row_size = (
            alignment - (3 * self.width) % alignment
        ) % alignment + 3 * self.width
        self.image_data = bytearray(self.height * self.row_size)
        for y in range(self.height):
            for x in range(self.width):
                self.set_pixel(x, y, color)

    def set_pixel(self, x: int, y: int, color: Color) -> None:
        offset = y * self.row_size + x * 3
        self.image_data[offset : offset + 3] = color.make()

    def get_pixel(self, x: int, y: int) -> Color:
        offset = y * self.row_size + x * 3
        return Color.from_bytes(self.image_data[offset : offset + 3])

    def make(self) -> bytearray:
        logger.debug(f"{self.__class__.__name__} has completed packing.")
        return self.image_data
