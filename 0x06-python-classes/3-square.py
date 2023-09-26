#!/usr/bin/python3
"""Area of a square"""


class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """
        Constructor of the Class

        Args:
            size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Public  instance method to calculate the area

        Returns:
            The current square area.
        """
        return (self.__size ** 2)
