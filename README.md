# Artsy

The idea behind *Artsy* is creating art using python scripts. It uses the [bmp](https://en.wikipedia.org/wiki/BMP_file_format) file format to create pixelated (rasty) images.


## Examples

### Cubes

![cubes](./artworks/cubes.bmp)

```Python
from artwork import Artwork
from models.pixel import Pixel


def main() -> None:
    length = 1000
    artwork = Artwork(width=length, height=length)
    for x in range(length):
        for y in range(length):
            artwork[x, y] = Pixel(red=x % 255, blue=y % 255, green=0)

    artwork.export("artwork.bmp")


if __name__ == "__main__":
    main()
```

## Lines

![lines](./artworks/lines.bmp)

```Python
from artwork import Artwork
from models.pixel import Pixel


def main() -> None:
    length = 1000
    artwork = Artwork(width=length, height=length)

    count = 0
    for x in range(length):
        for y in range(length):
            artwork[x, y] = Pixel(
	            red=count % 255, 
	            green=count % 255, 
	            blue=count % 255
	        )
            if (x + y) % 7 == 0:
                count += 1

    artwork.export("artwork.bmp")


if __name__ == "__main__":
    main()
```
