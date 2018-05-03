#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    matrix1 = [1,2,3,4]
    matrix2 = []
    matrix3 = [1,'a','b','c']
    matrix4 = {5:'a',4:'b',3:'c'}

    def test_one(self):
        self.assertEqual(max_integer(TestMaxInteger.matrix1),4)

    def test_two(self):
        self.assertEqual(max_integer(TestMaxInteger.matrix2),None)

    def test_three(self):
        self.assertRaises(TypeError, lambda: max_integer(0))

    def test_four(self):
        self.assertRaises(KeyError, lambda:max_integer(TestMaxInteger.matrix4))

if __name__ == '__main__':
    unittest.main()
