from .color import Color


class Pixel:
    def __init__(self, color: Color) -> None:
        self.color = color

    def make(self) -> bytearray:
        return bytearray([self.color.blue, self.color.green, self.color.red])
