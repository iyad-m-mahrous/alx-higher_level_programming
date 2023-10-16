#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square(Rectangle):"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """def __str__(self):"""

        return (f'[Square] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}')

    @property
    def size(self):
        """def size(self):"""

        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

        if args and len(args) != 0:
            no_args = len(args)
            if (no_args > 0):
                if args[0] is not None:
                    self.id = args[0]
            if(no_args > 1):
                self.size = args[1]
            if(no_args > 2):
                self.x = args[2]
            if(no_args > 3):
                self.y = args[3]

        elif kwargs and len(kwargs) != 0:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """def to_dictionary(self):"""

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
