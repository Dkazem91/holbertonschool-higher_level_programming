#!/usr/bin/python3
"""writes to a file"""


def write_file(filename="", text=""):
    """writes to file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return(f.write(text))
