#!/usr/bin/python3
for a in range(122, 96, -1):
    uppercase = 0
    if(a % 2 != 0):
        uppercase = 32
    print("{}".format(chr(a - uppercase)), end='')
