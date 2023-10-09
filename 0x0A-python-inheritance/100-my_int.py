#!/usr/bin/python3
""" a class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt(int):"""

    def __ne__(self, other):
        return (super.__eq__(other))

    def __eq__(self, other):
        return (super.__ne__(other))
