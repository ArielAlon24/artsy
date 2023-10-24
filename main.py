from artwork import Artwork
from models.color import Color

import math


def main() -> None:
    width, height = 1000, 1000
    artwork = Artwork(width=width, height=height)

    x, y = width // 2, height // 2

    angle = 0
    length = 1
    max_length = (width + height) // 5
    increment = 1
    while length < max_length:
        dx = int(length * math.cos(angle))
        dy = int(length * math.sin(angle))

        artwork.line(
            (x, y),
            (x + dx, y + dy),
            Color(
                int(0.7 * length / max_length * 256),
                int(0.7 * length / max_length * 256),
                int(0.7 * length / max_length * 256),
            ),
        )

        x, y = x + dx, y + dy
        angle += increment
        length += 1

    artwork.export("spiral_artwork.bmp")


if __name__ == "__main__":
    main()
