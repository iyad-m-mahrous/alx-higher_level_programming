#!/usr/bin/python3
"""Compare 2 squares"""


class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """
        Constructor of the Class

        Args:
            size (int): Size of the square
        """
        self.size = size

    @property
    def size(self):
        """size Getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public  instance method to calculate the area"""

        return (self.size ** 2)

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __nq__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()
        return False

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
