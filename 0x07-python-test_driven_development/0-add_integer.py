#!/usr/bin/python3
"""A function that adds 2 integers."""


def add_integer(a, b=98):
    """Add Two Integers

    Returns:
        the addition of a and b casted to int

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """

    if (not isinstance(a, float) and not isinstance(a, int)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, float) and not isinstance(b, int)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
