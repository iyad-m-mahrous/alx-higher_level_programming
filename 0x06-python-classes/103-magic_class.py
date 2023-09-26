#!/usr/bin/python3
"""A class that represents a magic circle.

Attributes:
    radius: The radius of the circle.

Methods:
    area(): Calculates the area of the circle.
    circumference(): Calculates the circumference of the circle.
"""

import math


class MagicClass:
    def __init__(self, radius=0):
        """Initializes a new MagicClass object.

        Args:
            radius: The radius of the circle.
        """

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle.

        Returns:
            The area of the circle.
        """

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle.

        Returns:
            The circumference of the circle.
        """

        return 2 * math.pi * self.__radius
