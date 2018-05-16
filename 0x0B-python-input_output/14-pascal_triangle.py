#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """does it"""
    for i in range(n):
        if i is 0:
            print([1])
            continue
        if i is 1:
            oldList = [1, 1]
            print(oldList)
            continue
        adder = [1] + [sum(oldList[x:x + 2]) for x in range(len(oldList) - 1)]
        newList = adder + [1]
        print(newList)
        oldList = newList
