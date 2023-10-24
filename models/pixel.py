from .color import Color
from typing import Tuple, Self
import struct


class Pixel:
    def __init__(self, color: Color) -> None:
        self.color = color

    def make(self) -> Tuple[int, int, int]:
        return bytearray([self.color.blue, self.color.green, self.color.red])

    @classmethod
    def from_bytes(self, data: bytes) -> Self:
        red, green, blue = struct.unpack("BBB", data)
        return Pixel(Color(red=red, green=green, blue=blue))
