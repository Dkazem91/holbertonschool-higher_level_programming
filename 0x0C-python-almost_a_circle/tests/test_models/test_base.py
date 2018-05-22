#!/usr/bin/python3
import unittest
import os.path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""tests the Base"""


class TestBase(unittest.TestCase):

    def test_id(self):
        """tests the ids"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_dictionary(self):
        """tests the dictionary"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertDictEqual(dictionary,
                             {'x': 2, 'width': 10,
                              'id': 1, 'height': 7, 'y': 8})
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, json_dictionary)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_saveFile(self):
        """tests the savefile"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Square(4)
        Rectangle.save_to_file([r1])
        Square.save_to_file([r2])
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) > 1)
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) > 1)

        Rectangle.save_to_file(None)
        Square.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(f.read() == "[]")
        with open("Square.json", 'r') as f:
            self.assertTrue(f.read() == "[]")

    def test_fromJson(self):
        """tests the fromjson"""
        r_input = [{'id': 89, 'width': 10, 'height': 4}]
        s_input = [{'id': 89, 'size': 4}]
        json_list_input = Rectangle.to_json_string(r_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_output) is list)
        list_output = Rectangle.from_json_string([])
        self.assertTrue(list_output == [])
        list_output = Rectangle.from_json_string(None)
        self.assertTrue(list_output == [])
        json_list_input = Square.to_json_string(s_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertTrue(type(list_output) is list)
        list_output = Square.from_json_string([])
        self.assertTrue(list_output == [])
        list_output = Square.from_json_string(None)
        self.assertTrue(list_output == [])

    def test_load(self):
        """tests load"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for thing in list_rectangles_output:
            self.assertTrue(type(thing) is Rectangle)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for thing in list_squares_output:
            self.assertTrue(type(thing) is Square)


if __name__ == '__main__':
    unittest.main()
