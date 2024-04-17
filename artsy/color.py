from __future__ import annotations
import struct
from dataclasses import dataclass
from functools import lru_cache


@dataclass(slots=True)
class Color:
    r: int
    g: int
    b: int
    MAX: int = 255

    def __post_init__(self) -> None:
        if (
            not (0 <= self.r <= self.MAX)
            or not (0 <= self.g <= self.MAX)
            or not (0 <= self.b <= self.MAX)
        ):
            raise ValueError(
                f"Color value must be positive and less than 256. Provided: ({self.r=}, {self.g=}, {self.b=})."
            )

    def __add__(self, other: Color) -> Color:
        return Color(
            min(self.MAX, self.r + other.r),
            min(self.MAX, self.g + other.g),
            min(self.MAX, self.b + other.b),
        )

    def __sub__(self, other: Color) -> Color:
        return Color(
            max(0, self.r - other.r),
            max(0, self.g - other.g),
            max(0, self.b - other.b),
        )

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Can only multiply Color by a scalar.")
        return Color(
            r=min(self.MAX, int(self.r * scalar)),
            g=min(self.MAX, int(self.g * scalar)),
            b=min(self.MAX, int(self.b * scalar)),
        )

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __neg__(self):
        return Color(
            r=self.MAX - self.r,
            g=self.MAX - self.g,
            b=self.MAX - self.b,
        )

    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

    def __bytes__(self) -> bytes:
        return struct.pack("BBB", self.b, self.g, self.r)
        # return bytes((self.b, self.g, self.r))

    @classmethod
    def from_bytes(cls, data: bytes) -> Color:
        r, g, b = struct.unpack("BBB", data)
        return Color(r=r, g=g, b=b)

    @classmethod
    def hex(cls, data: str) -> Color:
        r, g, b = bytes.fromhex(data.lstrip("#"))
        return cls(r=r, g=g, b=b)

    @classmethod
    def white(cls) -> Color:
        return Color(255, 255, 255)

    @classmethod
    def black(cls) -> Color:
        return Color(0, 0, 0)

    @classmethod
    def red(cls) -> Color:
        return Color(255, 0, 0)

    @classmethod
    def green(cls) -> Color:
        return Color(0, 255, 0)

    @classmethod
    def blue(cls) -> Color:
        return Color(0, 0, 255)
