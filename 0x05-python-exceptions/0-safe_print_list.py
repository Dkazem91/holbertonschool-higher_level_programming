#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if(my_list):
        printed = 0
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end='')
            except IndexError:
                print()
                return(printed)
            else:
                printed += 1
        print()
        return(printed)
