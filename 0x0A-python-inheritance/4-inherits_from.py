#!/usr/bin/python3
"""subclass checker"""


def inherits_from(obj, a_class):
    """returns subclass yes"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
