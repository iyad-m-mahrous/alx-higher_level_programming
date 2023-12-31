#!/usr/bin/python3
"""a class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            return (
                    {key: getattr(self, key) for key in self.__dict__
                        if key in attrs}
            )
        return self.__dict__
