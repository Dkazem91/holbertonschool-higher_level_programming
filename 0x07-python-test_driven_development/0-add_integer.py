#!/usr/bin/python3
"""adds integer
"""


def add_integer(a, b=98):
    """Returns a + b
    """
    if(a == float('+inf') or a == float('-inf') or a != a
       or not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")

    if(b == float('+inf') or b == float('-inf') or b != b
       or not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
print(add_integer(0))
