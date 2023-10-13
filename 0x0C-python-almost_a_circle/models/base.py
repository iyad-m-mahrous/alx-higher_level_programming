#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """class Base:"""

    __nb_objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)
    
    @classmethod
    def save_to_file(cls, list_objs):
        with open(f'{cls.__name__}.json', 'w', encoding = 'UTF-8') as f:
            if list_objs is None:
                json.dump([], f)
            else:
                f.write(
                        cls.to_json_string(
                            [i.to_dictionary() for i in list_objs]
                        )
                )

    @classmethod
    def create(cls, **dictionary):
        pass

