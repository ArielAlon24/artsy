from typing import Self
import struct


class Color:
    MAX: int = 255

    def __init__(self, red: int, green: int, blue: int) -> None:
        if (
            not (0 <= red <= self.MAX)
            or not (0 <= green <= self.MAX)
            or not (0 <= blue <= self.MAX)
        ):
            raise ValueError(
                f"Color value must be positive and less than 256. Provided: ({red=}, {green=}, {blue=})."
            )
        self.red = red
        self.green = green
        self.blue = blue

    def __add__(self, other: "Color"):
        return Color(
            min(self.MAX, self.red + other.red),
            min(self.MAX, self.green + other.green),
            min(self.MAX, self.blue + other.blue),
        )

    def __sub__(self, other: "Color"):
        return Color(
            max(0, self.red - other.red),
            max(0, self.green - other.green),
            max(0, self.blue - other.blue),
        )

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Can only multiply RGBColor by a scalar.")
        return Color(
            min(self.MAX, int(self.red * scalar)),
            min(self.MAX, int(self.green * scalar)),
            min(self.MAX, int(self.blue * scalar)),
        )

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __neg__(self):
        return Color(
            red=self.MAX - self.red,
            green=self.MAX - self.green,
            blue=self.MAX - self.blue,
        )

    def __repr__(self):
        return f"Color({self.red}, {self.green}, {self.blue})"

    def make(self) -> bytes:
        return bytearray([self.blue, self.green, self.red])

    @classmethod
    def from_bytes(self, data: bytes) -> Self:
        red, green, blue = struct.unpack("BBB", data)
        return Color(red=red, green=green, blue=blue)

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
