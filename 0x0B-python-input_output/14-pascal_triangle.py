#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """does it"""
    bullshit = []
    start = []
    for i in range(n):
        adder = [1] + [sum(start[x:x + 2]) for x in range(len(start) - 1)]
        newList = adder
        if i > 0:
            newList = adder + [1]
        bullshit.append(newList)
        start = newList
    return bullshit
