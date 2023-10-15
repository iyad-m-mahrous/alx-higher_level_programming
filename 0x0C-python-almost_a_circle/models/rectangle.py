#!/usr/bin/python3
"""Rectangle Class"""
from .base import Base


class Rectangle(Base):
    """class Rectangle(Base):"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return (f'[Rectangle] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}/{self.height}')

    @property
    def width(self):
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
        return self.__y

    @y.setter
    def y(self, value):
        if (type(value) != int):
            raise TypeError('y must be an integer')
        if (value < 0):
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return (self.width * self.height)

    def display(self):
        print('\n'*self.y, end='')
        for row in range(self.height):
            print(' '*self.x, end='')
            for col in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
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
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
