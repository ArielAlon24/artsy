from typing import Self
import struct


class Color:
    MAX: int = 255

    def __init__(self, red: int, green: int, blue: int) -> None:
        if (
            not 0 <= red <= self.MAX
            and not 0 <= green <= self.MAX
            and 0 <= blue <= self.MAX
        ):
            raise ValueError(
                f"Color value must be positive and less than 256. Provided: ({red=}, {green=}, {blue=})."
            )
        self.red = red
        self.green = green
        self.blue = blue

    def __neg__(self):
        return Color(
            red=self.MAX - self.red,
            green=self.MAX - self.green,
            blue=self.MAX - self.blue,
        )

    def make(self) -> bytes:
        return bytearray([self.blue, self.green, self.red])

    @classmethod
    def from_bytes(self, data: bytes) -> Self:
        red, green, blue = struct.unpack("BBB", data)
        return Color(red=red, green=green, blue=blue)

    def __repr__(self) -> str:
        return f"Color({self.red}, {self.blue}, {self.green})"

    @classmethod
    def white(self) -> Self:
        return Color(255, 255, 255)

    @classmethod
    def black(self) -> Self:
        return Color(0, 0, 0)

    @classmethod
    def red(self) -> Self:
        return Color(255, 0, 0)

    @classmethod
    def green(self) -> Self:
        return Color(0, 255, 0)

    @classmethod
    def blue(self) -> Self:
        return Color(0, 0, 255)
