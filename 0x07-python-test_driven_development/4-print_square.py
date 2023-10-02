#!/usr/bin/python3
"""a function that prints a square with the character #."""


def print_square(size):
    """print_square(size)

    Args:
        size is the size length of the square

    Raises:
        TypeError: if size not int
        ValueError: if size < 0
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
