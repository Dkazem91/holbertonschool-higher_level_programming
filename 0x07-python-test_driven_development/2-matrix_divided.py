#!/usr/bin/python3
"""matrix divider module"""
def matrix_divided(matrix, div):
    """divides a matrix all elements by divider
    """
    if(not isinstance(matrix,list) or not len(matrix) or
       0 in [len(listx) if type(listx) is list else 0 for listx in matrix] or
       any(False in x for x in  [[isinstance(ele,(int,float)) for ele in row]
       for row in matrix])):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    if(len(set([len(listx) for listx in matrix])) > 1):
        raise TypeError(
            'Each row of the matrix must have the same size')
    if(not isinstance(div,(int,float))):
        raise TypeError('div must be a number')
    if(div is 0):
        raise ZeroDivisionError('division by zero')
    return [[round(ele / div, 2) for ele in row] for row in matrix]
