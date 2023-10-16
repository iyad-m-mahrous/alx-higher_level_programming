#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle(Base):"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """def width(self):"""

        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError('width must be an integer')
        if (value <= 0):
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """def height(self):"""

        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError('height must be an integer')
        if (value <= 0):
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """def x(self):"""

        return self.__x

    @x.setter
    def x(self, value):
        if (type(value) != int):
            raise TypeError('x must be an integer')
        if (value < 0):
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """def y(self):"""

        return self.__y

    @y.setter
    def y(self, value):
        if (type(value) != int):
            raise TypeError('y must be an integer')
        if (value < 0):
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""

        return (self.width * self.height)

    def display(self):
        """Print the Rectangle using the `#` character."""

        print('\n'*self.y, end='')
        for row in range(self.height):
            print(' '*self.x, end='')
            for col in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

        if args and len(args) != 0:
            no_args = len(args)
            if (no_args > 0):
                if args[0] is not None:
                    self.id = args[0]
            if(no_args > 1):
                self.width = args[1]
            if(no_args > 2):
                self.height = args[2]
            if(no_args > 3):
                self.x = args[3]
            if(no_args > 4):
                self.y = args[4]

        elif kwargs and len(kwargs) != 0:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """def __str__(self):"""

        return (f'[Rectangle] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}/{self.height}')
