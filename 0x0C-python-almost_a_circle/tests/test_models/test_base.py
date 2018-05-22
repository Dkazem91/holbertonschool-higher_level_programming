#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
class TestBase(unittest.TestCase):

    def test_id(self):
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
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertDictEqual(dictionary,
                          {'x': 2, 'width': 10,
                           'id': 1, 'height': 7, 'y': 8})
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, json_dictionary)

if __name__ == '__main__':
    unittest.main()
