#!/usr/bin/python3
"""an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        result = ""
        for h in range(self.height):
            for w in range(self.width):
                result += "#"
            if (w != 0):
                result += "\n"
        return result

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return (
                0 if (self.width == 0 or self.height == 0)
                else (2 * (self.height + self.width))
                )
