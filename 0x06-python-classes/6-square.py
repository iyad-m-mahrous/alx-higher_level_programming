#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor of the Class

        Args:
            size (int): Size of the square
            position (tuple): a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

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
        for y_pos in range(self.position[1]):
            print()
        for i in range(self.size):
            for x_pos in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
        if not self.size:
            print()

    @property
    def position(self):
        """position Getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position Setter"""
        if (
                isinstance(value, tuple)
                and len(value) == 2
                and isinstance(value[0], int)
                and isinstance(value[1], int)
                and value[0] >= 0
                and value[1] >= 0
                ):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
