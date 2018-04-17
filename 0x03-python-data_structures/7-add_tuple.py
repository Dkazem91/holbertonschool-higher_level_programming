#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = tuple_a or (0, 0)
    b = tuple_b or (0, 0)
    if(len(a) is 1):
        a = (tuple_a[0], 0)
    if(len(b) is 1):
        b = (tuple_b[0], 0)
    return((a[0] + b[0], a[1] + b[1]))
