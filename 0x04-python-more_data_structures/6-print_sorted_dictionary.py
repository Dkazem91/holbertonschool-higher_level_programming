#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if(a_dictionary):
        for x, val in sorted(a_dictionary.items()):
            print("{}: {}".format(x, val))
