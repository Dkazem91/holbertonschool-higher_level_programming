#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """does it"""
    bullshit = []
    for i in range(n):
        if i is 0:
            bullshit.append([1])
            continue
        if i is 1:
            oldList = [1, 1]
            bullshit.append(oldList)
            continue
        adder = [1] + [sum(oldList[x:x + 2]) for x in range(len(oldList) - 1)]
        newList = adder + [1]
        bullshit.append(newList)
        oldList = newList
    return bullshit
