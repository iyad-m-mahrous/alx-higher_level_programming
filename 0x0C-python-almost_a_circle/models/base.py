#!/usr/bin/python3
"""Base Class"""
import json
import csv
import turtle


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
        with open(f'{cls.__name__}.json', 'w', encoding='UTF-8') as f:
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
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                obj = cls(1, 1)
            else:
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        try:
            with open(f'{cls.__name__}.json', 'r', encoding='UTF-8') as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**i) for i in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(f'{cls.__name__}.csv', 'w', newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open(f'{cls.__name__}.csv', 'r', newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(f, fieldnames=fieldnames)
                list_dict = [
                        dict((key, int(value)) for key, value in i.items())
                        for i in list_dict
                ]
                return [cls.create(**i) for i in list_dict]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        t = turtle.Turtle()
        t.screen.bgcolor("black")

        t.pensize(3)
        t.shape("classic")
        t.color("white")
        for rect in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rect.x, rect.y)
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.pensize(2)
        t.color("red")
        t.shape("turtle")
        for sq in list_squares:
            t.showturtle()
            t.up()
            t.goto(sq.x, sq.y)
            t.down()
            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            t.hideturtle()

        turtle.exitonclick()
