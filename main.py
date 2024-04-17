import math
from artsy import Artwork, Color


def draw_mandala(artwork, center, radius, num_rings, num_divisions, color):
    angle_step = 2 * math.pi / num_divisions
    for ring in range(1, num_rings + 1):
        # Calculate the radius for this ring
        current_radius = (radius / num_rings) * ring
        # Generate points around the circle
        points = [
            (
                int(center[0] + math.cos(angle_step * i) * current_radius),
                int(center[1] + math.sin(angle_step * i) * current_radius),
            )
            for i in range(num_divisions + 1)
        ]
        # Draw the circle using lines between points
        for i in range(num_divisions):
            artwork.line(points[i], points[i + 1], color)  # Black color for the lines
            # Connect each point to several points ahead, creating a pattern
            for skip in range(1, num_rings):
                connect_point = (i + skip) % num_divisions
                artwork.line(points[i], points[connect_point], color)


def main():
    width, height = 1920, 1080
    artwork = Artwork(width=width, height=height)
    center = (width // 2, height // 2)
    radius = min(center) // 4 * 3
    num_rings = 30
    num_divisions = 24

    artwork.triangle((0, 0), (width, height), (width, 0), Color.hex("#D4F1F4"))
    artwork.triangle((0, 0), (width, height), (0, height), Color.hex("#D4F1F4"))

    draw_mandala(
        artwork, center, radius, num_rings + 4, num_divisions, Color.hex("#1e2d47")
    )

    draw_mandala(
        artwork, center, radius // 5, num_rings, num_divisions, Color.hex("#283c5f")
    )

    artwork.export("artwork.bmp")


if __name__ == "__main__":
    main()
