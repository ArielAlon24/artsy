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
