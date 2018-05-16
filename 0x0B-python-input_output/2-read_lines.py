#!/usr/bin/python3
"""reads lines"""


def read_lines(filename="", nb_lines=0):
    lines = 0
    with open(filename, mode='r', encoding="utf-8") as f:
        for line in f:
            lines += 1
            print(line, end="")
            if lines == nb_lines:
                break
