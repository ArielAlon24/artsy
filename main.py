from artwork import Artwork
from models.color import Color


# ChatGPT generated function
def weird_tuple_generator(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Both input integers must be positive.")

    # Calculate a hash value of the sum of squares of a and b.
    hash_value = hash(a**2 + b**2)

    # Create a list of prime numbers up to the hash value.
    primes = [2]
    num = 3

    while len(primes) < 10:
        is_prime = True
        for divisor in range(3, int(num**0.5) + 1, 2):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2

    # Calculate the first value as the product of the first two prime numbers in the list.
    if len(primes) >= 2:
        value1 = primes[0] * primes[1]
    else:
        value1 = 0

    # Calculate the second value as the absolute difference between a and b.
    value2 = abs(a - b)

    # Calculate the third value as the hash value XORed with the sum of the first 10 prime numbers.
    sum_of_primes = sum(primes)
    value3 = hash_value ^ sum_of_primes

    return (value1 % 256, value2 % 256, value3 % 256)


def main() -> None:
    length = 1000
    artwork = Artwork(width=length, height=length)
    iteration = 0
    for x in range(length):
        for y in range(length):
            v1 = (7 * (x + y) % 1000, 7 * (x - y) % 1000)
            v2 = (3 * (x + y) % 1000, 3 * (x - y) % 1000)
            v3 = (9 * (x + y) % 1000, 9 * (x - y) % 1000)
            color = Color(iteration % 256, iteration % 256, iteration % 256)
            artwork.line(p0=v1, p1=v2, color=color)
            artwork.line(p0=v2, p1=v3, color=color)
            artwork.line(p0=v3, p1=v1, color=color)
            iteration += 1
    artwork.export("artwork.bmp")


if __name__ == "__main__":
    main()
