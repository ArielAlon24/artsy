from utils.bytes import to_bytes


class _DibHeader:
    HEADER_SIZE: int = 40
    COLOR_PLANES: int = 1
    COMPRESSION_METHOD: int = 0
    PALETTE_COLORS: int = 0
    IMPORTANT_COLORS: int = 0

    def __init__(
        self, width: int, height: int, resulotion: int = 2835, bit: int = 24
    ) -> None:
        self._size = to_bytes(self.HEADER_SIZE)
        self._width = to_bytes(width)
        self._height = to_bytes(height)
        self._color_planes = to_bytes(self.COLOR_PLANES, size=2)
        self._bit = to_bytes(bit, size=2)
        self._compression_method = to_bytes(self.COMPRESSION_METHOD)
        self._image_size = to_bytes(3 * width * height)
        self._horizontal_resolution = to_bytes(resulotion)
        self._vertical_resolution = to_bytes(resulotion)
        self._palette_colors = to_bytes(self.PALETTE_COLORS)
        self._important_colors = to_bytes(self.IMPORTANT_COLORS)

    def make(self) -> bytes:
        return (
            self._size
            + self._width
            + self._height
            + self._color_planes
            + self._bit
            + self._compression_method
            + self._image_size
            + self._horizontal_resolution
            + self._vertical_resolution
            + self._palette_colors
            + self._important_colors
        )
