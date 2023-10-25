from artwork import Artwork
from models.color import Color
import math


def main() -> None:
    length = 1000
    artwork = Artwork(width=length, height=length)

    x0, y0 = length // 2, length // 2

    radius = 4 * (length // 2 // 5)
    color_factor = 90
    power = -0.5
    for angle in range(360):
        print(f"Angle: {angle}")
        x1 = int(radius * max(math.cos(math.radians(angle)), 0.1) ** power)
        y1 = int(radius * max(math.sin(math.radians(angle)), 0.1) ** power)
        artwork.line(
            p0=(x0, y0),
            p1=((x0 + x1) % length, (y0 + y1) % length),
            color=Color(
                red=int((angle % color_factor / color_factor) * 256),
                blue=int((angle % color_factor / color_factor) * 256),
                green=int((angle % color_factor / color_factor) * 256),
            ),
        )

    artwork.export("artwork.bmp")


if __name__ == "__main__":
    main()
