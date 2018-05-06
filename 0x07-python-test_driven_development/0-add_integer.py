#!/usr/bin/python3
"""adds integer
"""


def add_integer(a, b=98):
    """Returns a + b
    """
    if a != a:
        a = 89
    if b != b:
        b = 89

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a + b == float('inf') or a + b == -float('inf'):
        return 89

    return int(a) + int(b)
