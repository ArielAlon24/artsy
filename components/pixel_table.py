from models.pixel import Pixel
from models import color


class _PixelTable:
    def __init__(self, width: int, height: int, alignment: int = 4) -> None:
        self.width = width
        self.height = height
        self.row_size = (alignment - (3 * width) % alignment) % alignment + 3 * width
        self.image_data = bytearray(self.height * self.row_size)
        for y in range(self.height):
            for x in range(self.width):
                self.set_pixel(x, y, Pixel(color=color.BLACK))

    def set_pixel(self, x: int, y: int, pixel: Pixel) -> None:
        offset = y * self.row_size + x * 3
        self.image_data[offset : offset + 3] = pixel.make()

    def get_pixel(self, x: int, y: int) -> Pixel:
        offset = y * self.row_size + x * 3
        return Pixel.from_bytes(self.image_data[offset : offset + 3])

    def make(self) -> bytearray:
        return self.image_data
