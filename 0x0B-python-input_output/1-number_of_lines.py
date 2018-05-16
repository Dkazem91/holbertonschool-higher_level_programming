#!/usr/bin/python3
"""returns number of lines"""


def number_of_lines(filename=""):
    """number of lines"""
    lines = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines
