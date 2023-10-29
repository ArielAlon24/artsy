from artwork import Artwork
from models.color import Color


def main() -> None:
    width = 2000
    quarter = width // 4
    artwork = Artwork(width=width, height=width)
    for x in range(width):
        for y in range(width):
            if x + y % 29 == 3:
                artwork.triangle(
                    (x, y),
                    (x + quarter, y + 3 * quarter),
                    (x + 2 * quarter, y + 2 * quarter),
                    Color(x % 256, y % 256, 20),
                )

    artwork.export("artwork.bmp")


if __name__ == "__main__":
    main()
