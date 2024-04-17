from .handlers.logging_handler import LoggingHandler
from .components import _BmpHeader, _DibHeader, _PixelTable
from .color import Color
from typing import Tuple
import time

logger = LoggingHandler.create_logger(__name__)

Point = Tuple[int, int]


class Artwork:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._pixel_table = _PixelTable(width=self.width, height=self.height)
        self.components = [
            _BmpHeader(width=self.width, height=self.height),
            _DibHeader(width=self.width, height=self.height),
            self._pixel_table,
        ]
        self._creation_time = time.perf_counter()

    def export(self, path: str) -> None:
        start = time.perf_counter()
        with open(path, "wb") as file:
            for component in self.components:
                file.write(bytes(component))

        end = time.perf_counter()
        logger.debug(f"Finished exporting '{path}'.")
        logger.info(f"Drawing took:  \t {end - self._creation_time: .4f} sec.")
        logger.info(f"Exporting took:\t {end - start: .4f} sec.")

    def __getitem__(self, key: Point):
        if not isinstance(key, tuple) or not len(key) == 2:
            raise TypeError("Invalid index format. Use (x, y).")

        x, y = key
        try:
            return self._pixel_table.get(x=x - 1, y=y - 1)
        except IndexError:
            raise IndexError(f"Index out of range: ({x}, {y}).")

    def __setitem__(self, key: Point, value: Color):
        if not isinstance(key, tuple) or not len(key) == 2:
            raise TypeError("Invalid index format. Use (x, y).")

        x, y = key
        try:
            self._pixel_table.set(x=x - 1, y=y - 1, color=value)
        except IndexError:
            raise IndexError(f"Index out of range: ({x}, {y}).")

    def border(self, color: Color = Color.white()) -> None:
        self.line((1, 1), (self.width, 1), color)
        self.line((self.width, 1), (self.width, self.height), color)
        self.line((self.width, self.height), (1, self.height), color)
        self.line((1, self.height), (1, 1), color)

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

    def polygon(self, *points: Point, color: Color) -> None:
        if len(points) < 3:
            raise ValueError("A polygon must have at least 3 points.")

        x_min = min(x for x, _ in points)
        x_max = max(x for x, _ in points)
        y_min = min(y for _, y in points)
        y_max = max(y for _, y in points)

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                inside = False
                j = len(points) - 1
                for i in range(len(points)):
                    x0, y0 = points[i]
                    x1, y1 = points[j]
                    if (y0 < y <= y1 or y1 < y <= y0) and (x <= max(x0, x1)):
                        cross = (x1 - x0) * (y - y0) / (y1 - y0) + x0
                        if x < cross:
                            inside = not inside
                    j = i

                if inside:
                    self[x, y] = color

    def fill(self, color: Color) -> None:
        for x in range(1, self.width + 1):
            for y in range(1, self.height + 1):
                self[x, y] = color

    def boundary(self, *points: Point, color: Color) -> None:
        if len(points) < 3:
            raise ValueError("A boundary must have at least 3 points.")

        for i, point in enumerate(points):
            self.line(point, points[(i + 1) % len(points)], color=color)

    def triangle(
        self,
        p0: Point,
        p1: Point,
        p2: Point,
        color: Color,
        is_filled: bool = True,
        fill: Color | None = None,
    ) -> None:
        if is_filled:
            self.polygon(p0, p1, p2, color=fill if fill is not None else color)

        self.boundary(p0, p1, p2, color=color)

    def rectangle(
        self, p0: Point, p1: Point, p2: Point, p3: Point, color: Color
    ) -> None:
        self.polygon(p0, p1, p2, p3, color=color)
