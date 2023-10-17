#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    @classmethod
    def tearDownClass(self):
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_init(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(12, Base(12).id)
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)
        with self.assertRaises(AttributeError):
            print(Base(12).__test)
        self.assertEqual("hello", Base("hello").id)
        self.assertEqual(5.5, Base(5.5).id)
        self.assertEqual(complex(5), Base(complex(5)).id)
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)
        self.assertEqual(True, Base(True).id)
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)
        self.assertEqual((1, 2), Base((1, 2)).id)
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)
        self.assertEqual(range(5), Base(range(5)).id)
        self.assertEqual(b'Python', Base(b'Python').id)
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)
        self.assertEqual(float('inf'), Base(float('inf')).id)
        self.assertNotEqual(float('nan'), Base(float('nan')).id)
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)
        self.assertEqual("[]", Base.to_json_string([]))
        self.assertEqual("[]", Base.to_json_string(None))
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_save_to_file(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_from_json_string(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
        self.assertEqual([], Base.from_json_string(None))
        self.assertEqual([], Base.from_json_string("[]"))
        with self.assertRaises(TypeError):
            Base.from_json_string()
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    def test_load_from_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_save_to_file_csv(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

    def test_load_from_file_csv(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))


if __name__ == "__main__":
    unittest.main()
