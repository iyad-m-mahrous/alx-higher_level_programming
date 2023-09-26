#!/usr/bin/python3


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
        """Public  instance method to calculate the area

        Returns:
            The current square area.
        """
        return (self.size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
        if not self.size:
            print()
