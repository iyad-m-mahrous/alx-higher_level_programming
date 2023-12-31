#!/usr/bin/python3


"""A class that represents a magic circle."""


import math


class MagicClass:
    """Circle Class"""

    def __init__(self, radius=0):
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
