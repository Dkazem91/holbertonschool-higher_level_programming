#!/usr/bin/python3
import pep8
import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO
"""tests rectangle"""


class TestRectangle(unittest.TestCase):

    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/rectangle.py','models/base.py','models/square.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_ids(self):
        """tests ids"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        r3.id = "a"
        self.assertEqual(r3.id, "a")

    def test_attr_errors(self):
        """tests errors"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r1 = Rectangle(10, "2")
        with self.assertRaises(ValueError, msg="height must be  > 0"):
            r1 = Rectangle(-2, 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r1 = Rectangle({1: 2}, 2)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r2 = Rectangle(10, 2)
            r2.width = -10
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r3 = Rectangle(10, 2)
            r3.x = {}
        with self.assertRaises(ValueError, msg="y must be >=0"):
            r4 = Rectangle(10, 2, 3, -1)

    def test_areas(self):
        """tests areas"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r1 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)

        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)

    def test_display(self):
        """tests display"""
        Base._Base__nb_objects = 0
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        r1 = Rectangle(4, 2)
        r1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "####\n####\n")
        sys.stdout = mystdout = StringIO()
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n  ##\n")
        sys.stdout = old_stdout

    def test_str(self):
        """tests strings"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 0/0 - 1/1")

    def test_update(self):
        """tests update"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1_dictionary = r1.to_dictionary()
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        with self.assertRaises(ValueError, msg="x must be >=0"):
            r1.update(y=1, width=2, x=-3, id=89)
        r2 = Rectangle(2, 2)
        r2.update(**r1_dictionary)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 10/10 - 10/10")

    def test_dictionary(self):
        """tests dictionary"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {
            'x': 1, 'y': 9, 'width': 10, 'height': 2, 'id': 1})
        r1 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {
            'x': 0, 'y': 0, 'width': 1, 'height': 1, 'id': 2})

    def test_RectCreate(self):
        """tests create"""
        Base._Base__nb_objects = 0
        s1 = Rectangle(10, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Rectangle.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)


if __name__ == '__main__':
    unittest.main()
