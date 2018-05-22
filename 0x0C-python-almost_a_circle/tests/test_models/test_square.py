#!/usr/bin/python3
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO
"""tests square"""


class TestSquare(unittest.TestCase):

    def test_docstrings(self):
        """tests docstrings"""
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Square.__doc__) > 0)
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)
        for func in dir(Square):
            self.assertTrue(len(func.__doc__) > 0)

    def test_ids(self):
        """tests ids"""
        Base._Base__nb_objects = 0
        r1 = Square(10)
        r2 = Square(2)
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        r3.id = "a"
        self.assertEqual(r3.id, "a")

    def test_attr_errors(self):
        """tests errors"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError, msg="size must be an integer"):
            r1 = Square("2")
        with self.assertRaises(ValueError, msg="size must be  > 0"):
            r1 = Square(-2)
        with self.assertRaises(TypeError, msg="size must be an integer"):
            r1 = Square({1: 2})
        with self.assertRaises(ValueError, msg="size must be > 0"):
            r2 = Square(10)
            r2.size = -10
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r3 = Square(10, 2)
            r3.x = {}
        with self.assertRaises(ValueError, msg="y must be >=0"):
            r4 = Square(10, 2, -1)

    def test_areas(self):
        """tests areas"""
        Base._Base__nb_objects = 0
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

        r1 = Square(2)
        self.assertEqual(r1.area(), 4)

        r1 = Square(8, 0, 0, 12)
        self.assertEqual(r1.area(), 64)

    def test_display(self):
        """tests displays"""
        Base._Base__nb_objects = 0
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        r1 = Square(2)
        r1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "##\n##\n")
        sys.stdout = mystdout = StringIO()
        r1 = Square(2, 2, 2)
        r1.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n")
        sys.stdout = old_stdout

    def test_str(self):
        """tests strings"""
        Base._Base__nb_objects = 0
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Square] (12) 2/1 - 4")
        r2 = Square(5, 1)
        self.assertEqual(r2.__str__(), "[Square] (1) 1/0 - 5")
        r1 = Square(1)
        self.assertEqual(r1.__str__(), "[Square] (2) 0/0 - 1")

    def test_update(self):
        """tests update"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10, 10)
        r1_dictionary = r1.to_dictionary()
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Square] (89) 10/10 - 10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Square] (89) 10/10 - 2")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Square] (89) 3/10 - 2")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Square] (89) 1/3 - 4")
        with self.assertRaises(ValueError, msg="x must be >=0"):
            r1.update(y=1, width=2, x=-3, id=89)
        r2 = Square(2, 2)
        r2.update(**r1_dictionary)
        self.assertEqual(r2.__str__(), "[Square] (10) 10/10 - 10")

    def test_dictionary(self):
        """tests dictionary"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {
            'x': 2, 'y': 1, 'size': 10, 'id': 9})
        r1 = Square(1)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {
            'x': 0, 'y': 0, 'size': 1, 'id': 1})

    def test_SquareCreate(self):
        """tests create"""
        Base._Base__nb_objects = 0
        s1 = Square(10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)


if __name__ == '__main__':
    unittest.main()
