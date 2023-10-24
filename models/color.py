class Color:
    MAX: int = 255

    def __init__(self, red: int, green: int, blue: int) -> None:
        if (
            not 0 <= red <= self.MAX
            and not 0 <= green <= self.MAX
            and 0 <= blue <= self.MAX
        ):
            raise ValueError(
                f"Color value must be positive and less than 256. Provided: ({red=}, {green=}, {blue=})."
            )
        self.red = red
        self.green = green
        self.blue = blue

    def __neg__(self):
        return Color(
            red=self.MAX - self.red,
            green=self.MAX - self.green,
            blue=self.MAX - self.blue,
        )


RED: Color = Color(255, 0, 0)
GREEN: Color = Color(0, 255, 0)
BLUE: Color = Color(0, 0, 255)
BLACK: Color = Color(0, 0, 0)
WHITE: Color = Color(255, 255, 255)
