from components.bmp_header import _BmpHeader
from components.dib_header import _DibHeader
from components.pixel_table import _PixelTable

from models.color import Color
from typing import Tuple


class Artwork:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._bmp_header = _BmpHeader(width=self.width, height=self.height)
        self._dib_header = _DibHeader(width=self.width, height=self.height)
        self._pixel_table = _PixelTable(width=self.width, height=self.height)

    def export(self, path: str) -> None:
        with open(path, "wb") as file:
            file.write(self._bmp_header.make())
            file.write(self._dib_header.make())
            file.write(self._pixel_table.make())

    def __getitem__(self, key: Tuple[int, int]):
        if not isinstance(key, tuple) or not len(key) == 2:
            raise TypeError("Invalid index format. Use (x, y).")

        x, y = key
        try:
            return self._pixel_table.table[self.height - y - 1][x]
        except IndexError:
            raise IndexError(f"Index out of range: ({x}, {y}).")

    def __setitem__(self, key: Tuple[int, int], value: Color):
        if not isinstance(key, tuple) or not len(key) == 2:
            raise TypeError("Invalid index format. Use (x, y).")

        x, y = key
        try:
            self._pixel_table.table[self.height - y - 1][x].color = value
        except IndexError:
            raise IndexError(f"Index out of range: ({x}, {y}).")

    def box(
        self,
        p0: Tuple[int, int],
        p1: Tuple[int, int],
        color: Color,
        is_filled: bool = True,
    ) -> None:
        x0, y0 = p0
        x1, y1 = p1
        x0 = max(0, x0)
        x1 = min(self.width - 1, x1)
        y0 = max(0, y0)
        y1 = min(self.height - 1, y1)

        if is_filled:
            for x in range(x0, x1):
                for y in range(y0, y1):
                    self[x, y] = color
        else:
            for x in range(x0 + 1, x1 - 1):
                self[x, y0] = color
                self[x, y1 - 1] = color
            for y in range(y0, y1):
                self[x0, y] = color
                self[x1 - 1, y] = color

    def line(self, p0: Tuple[int, int], p1: Tuple[int, int], color: Color) -> None:
        x0, y0 = p0
        x1, y1 = p1

        # Check if we should loop over y values instead of x
        steep = abs(y1 - y0) > abs(x1 - x0)

        if steep:
            # Swap x and y for both points
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        # Ensure first point is to the left/top of the second
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        # Check for a vertical line
        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                if steep:
                    # print(f"(x, y) = ({y}, {x0})")
                    self[y, x0] = color
                else:
                    # print(f"(x, y) = ({x0}, {y})")
                    self[x0, y] = color
            return

        m = (y0 - y1) / (x0 - x1)
        b = y0 - m * x0

        for x in range(
            x0, x1 + 1
        ):  # Note: I've also added "+ 1" to make sure x1 is included.
            y = round(m * x + b)
            if steep:
                # If steep, set y, x instead of x, y
                # print(f"(x, y) = ({y}, {x})")
                self[y, x] = color
            else:
                # print(f"(x, y) = ({x}, {y})")
                self[x, y] = color
