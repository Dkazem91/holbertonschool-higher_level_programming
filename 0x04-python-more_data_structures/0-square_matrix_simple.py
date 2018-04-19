#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if(matrix):
        return ([[y*y for y in x] for x in matrix])
