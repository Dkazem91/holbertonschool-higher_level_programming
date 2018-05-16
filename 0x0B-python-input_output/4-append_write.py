#!/usr/bin/python3
"""appends to a file or creates it"""


def append_write(filename="", text=""):
    """appends to file or creates it"""
    with open(filename, mode="a+", encoding='utf-8') as f:
        return(f.write(text))
