#!/usr/bin/python3
def print_last_digit(number):
    lastDig = int(str(number)[-1])
    print("{}".format(lastDig), end='')
    return(lastDig)
