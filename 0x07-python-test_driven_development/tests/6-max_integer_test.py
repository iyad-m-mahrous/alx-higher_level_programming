#!/usr/bin/python3
"""unittests for the function def max_integer(list=[]):."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_empty(self):
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_one(self):
        my_list = [4]
        self.assertEqual(max_integer(my_list), 4)

    def test_ordered(self):
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_unordered(self):
        my_list = [2, 1, 4, 3]
        self.assertEqual(max_integer(my_list), 4)

    def test_negative(self):
        my_list = [-1,-3,-4, -2, -6]
        self.assertEqual(max_integer(my_list), -1)

    def test_floats(self):
        my_list = [1.5, 2.43, 0.45, 6.66, -1.6, -99.8]
        self.assertEqual(max_integer(my_list), 6.66)

    def test_ints_and_floats(self):
        my_list = [3.9, 10.001, -1, 10, 2]
        self.assertEqual(max_integer(my_list), 10.001)

    def test_string(self):
        my_list = "Iyad"
        self.assertEqual(max_integer(my_list), 'y')

    def test_strings(self):
        my_list = ["Iyad", "Mahrous", "is", "here"]
        self.assertEqual(max_integer(my_list), "is")

    def test_empty_string(self):
        my_list = ""
        self.assertEqual(max_integer(my_list), None)

if __name__ == '__main__':
    unittest.main()
