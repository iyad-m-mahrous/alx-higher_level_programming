#!/usr/bin/python3
"""Square Class"""
from .rectangle import Rectangle


class Square(Rectangle):
    """class Square(Rectangle):"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f'[Square] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}')

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
            if (kwargs.get('id')):
                if kwargs['id'] is not None:
                    self.id = kwargs['id']
            if (kwargs.get('size')):
                self.size = kwargs['size']
            if (kwargs.get('x')):
                self.x = kwargs['x']
            if (kwargs.get('y')):
                self.y = kwargs['y']
