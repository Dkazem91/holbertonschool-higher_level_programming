#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if(my_list):
        printed = 0
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end='')
                printed += 1
            except IndexError:
                print()
                return(printed)
        print()
        return(printed)
