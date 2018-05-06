#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):

    def test_one(self):
        matrix1 = [1,2,3,4]
        self.assertEqual(max_integer(matrix1),4)

    def test_two(self):
        matrix2 = []
        self.assertEqual(max_integer(matrix2),None)

    def test_three(self):
        self.assertRaises(TypeError, max_integer,0)

    def test_four(self):
        matrix4 = {5:'a',4:'b',3:'c'}
        self.assertRaises(KeyError, max_integer,matrix4)

    def test_five(self):
        matrix = ['a','b','c']
        self.assertEqual(max_integer(matrix),'c')

    def test_six(self):
        matrix = 'hello'
        self.assertEqual(max_integer(matrix),'o')

    def test_seven(self):
        matrix = [-500,1,2,3]
        self.assertEqual(max_integer(matrix),3)

    def test_eight(self):
        matrix1 = [4]
        self.assertEqual(max_integer(matrix1),4)

    def test_nine(self):
        matrix1 = [4,1,2,3]
        self.assertEqual(max_integer(matrix1),4)

    def test_ten(self):
        matrix1 = [1,2,6,5,4]
        self.assertEqual(max_integer(matrix1),6)

if __name__ == '__main__':
    unittest.main()
