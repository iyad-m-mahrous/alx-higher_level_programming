#!/usr/bin/python3
"""A class that represents a magic circle."""


class MagicClass:

    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a specified radius.

        Args:
            radius (float): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
