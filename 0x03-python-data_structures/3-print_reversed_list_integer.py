#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for x in range(len(my_list)-1, -1, -1):
        print("{:d}".format(my_list[x]))
