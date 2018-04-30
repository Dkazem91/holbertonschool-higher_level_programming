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

my_list = ["hello"]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
