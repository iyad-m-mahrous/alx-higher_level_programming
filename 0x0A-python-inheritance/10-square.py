#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """"class Square(Rectangle):"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)
