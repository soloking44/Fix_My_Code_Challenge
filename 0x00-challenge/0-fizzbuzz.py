#!/usr/bin/python3
""" This is FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    The FizzBuzz function displays serials of numbers from 1 to n, with each splited by a space.
    - However, for multiples of three, it displays "Fizz" instead of the number and for
      multiples of five displays "Buzz".
    - For numbers divisible by both three and five displays "FizzBuzz".
    """
    if n < 1:
        return

    tmp_result = []
    for m in range(1, n + 1):
        if (m % 3) == 0 and (m % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (m % 3) == 0:
            tmp_result.append("Fizz")
        elif (m % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(m))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
