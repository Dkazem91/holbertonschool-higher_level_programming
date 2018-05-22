#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
class TestSquare(unittest.TestCase):

    def test_Squarearea(self):
        Base._Base__nb_objects = 0
        s1 = Square(2, 2)
        s2 = Square(size=4, x=2, y=3)
        self.assertEqual(s1.area(), 4)
        self.assertEqual(s2.area(), 16)

    def test_squareFail(self):
        Base._Base__nb_objects = 0
        s1 = Square(2, 2)
        s2 = Square(size=4, x=2, y=3)
        with self.assertRaises(TypeError):
            Square('A')
            Square([])
            Square({1: 2})
            Square(1, 1, 'a')
            Square(1, 'a', 1)
        with self.assertRaises(ValueError):
            Square(-4)
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, -1)
            Square(1, 1, -1)
