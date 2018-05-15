#!/usr/bin/python3
"""class mylist"""


class MyList(list):
    """prints sorted list of class"""
    def print_sorted(self):
        print(sorted(self))
