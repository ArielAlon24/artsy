from components.bmp_header import _BmpHeader
from components.dib_header import _DibHeader
from components.pixel_table import _PixelTable
from models.color import Color
from typing import Tuple
import time
from logging import Logger
from handlers.logging_handler import LoggingHandler

logger: Logger = LoggingHandler.create_logger(__name__)

Point = Tuple[int, int]


class Artwork:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._bmp_header = _BmpHeader(width=self.width, height=self.height)
        self._dib_header = _DibHeader(width=self.width, height=self.height)
        self._pixel_table = _PixelTable(width=self.width, height=self.height)

    def export(self, path: str) -> None:
        start = time.perf_counter()
        with open(path, "wb") as file:
            file.write(self._bmp_header.make())
            file.write(self._dib_header.make())
            file.write(self._pixel_table.make())
        end = time.perf_counter()
        logger.debug(f"Finished exporting {path}. Took: {end - start} sec.")

    def __getitem__(self, key: Point):
        if not isinstance(key, tuple) or not len(key) == 2:
            raise TypeError("Invalid index format. Use (x, y).")

        x, y = key
        try:
            return self._pixel_table.get_pixel(x=x - 1, y=y - 1)
        except IndexError:
            raise IndexError(f"Index out of range: ({x}, {y}).")

    def __setitem__(self, key: Point, value: Color):
        if not isinstance(key, tuple) or not len(key) == 2:
            raise TypeError("Invalid index format. Use (x, y).")

        x, y = key
        try:
            self._pixel_table.set_pixel(x=x - 1, y=y - 1, color=value)
        except IndexError:
            raise IndexError(f"Index out of range: ({x}, {y}).")

    def border(self, color: Color) -> None:
        self.line((1, 1), (self.width, 1), Color.red())
        self.line((self.width, 1), (self.width, self.height), Color.red())
        self.line((self.width, self.height), (1, self.height), Color.red())
        self.line((1, self.height), (1, 1), Color.red())

    def line(self, p0: Point, p1: Point, color: Color) -> None:
        x0, y0 = p0
        x1, y1 = p1

        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                self[x0, y] = color
            return

        if y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                self[x, y0] = color
            return

        steep = abs(y1 - y0) > abs(x1 - x0)

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = x1 - x0
        dy = abs(y1 - y0)

        ystep = 1 if y0 < y1 else -1

        error = dx // 2
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                self[y, x] = color
            else:
                self[x, y] = color

            error -= dy
            if error < 0:
                y += ystep
                error += dx

    def triangle(self, p0: Point, p1: Point, p2: Point, color: Color) -> None:
        x0, y0 = p0
        x1, y1 = p1
        x2, y2 = p2

        x_min = min(x0, x1, x2)
        x_max = max(x0, x1, x2)
        y_min = min(y0, y1, y2)
        y_max = max(y0, y1, y2)

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                o0 = (x0 - x) * (y1 - y) - (x1 - x) * (y0 - y)
                o1 = (x1 - x) * (y2 - y) - (x2 - x) * (y1 - y)
                o2 = (x2 - x) * (y0 - y) - (x0 - x) * (y2 - y)

                if (o0 >= 0 and o1 >= 0 and o2 >= 0) or (
                    o0 <= 0 and o1 <= 0 and o2 <= 0
                ):
                    self[x, y] = color
