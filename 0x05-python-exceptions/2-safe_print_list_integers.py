#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    v = 0
    if(my_list):
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]),end='')
            except(ValueError,TypeError):
                v += 1
        print()
        return(i - v + 1)
