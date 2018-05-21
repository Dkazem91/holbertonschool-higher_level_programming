#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
class TestSquare(unittest.TestCase):

    def test_square(self):
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
