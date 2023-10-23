from models.pixel import Pixel
from models import color


class _PixelTable:
    def __init__(self, width: int, height: int, alingment: int = 4) -> None:
        self.table = [
            [Pixel(color=color.BLACK) for _ in range(width)] for _ in range(height)
        ]
        self.padding = (alingment - (3 * width) % 4) % 4

    def make(self) -> bytearray:
        image_data = bytearray()
        for row in self.table:
            for pixel in row:
                image_data += pixel.make()
            image_data += bytearray([0] * self.padding)
        return image_data
