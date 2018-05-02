#!/usr/bin/python3
def matrix_divided(matrix, div):
    if(not isinstance(matrix,list) or
       any(False in x for x in  [[isinstance(ele,(int,float)) for ele in row]
                                   for row in matrix]) or
        0 in [len(listx) for listx in matrix]):
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
