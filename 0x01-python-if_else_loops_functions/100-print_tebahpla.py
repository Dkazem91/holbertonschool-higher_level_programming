#!/usr/bin/python3
for a in range(122, 96, -1):
    if(a % 2 != 0):
        a -= 32
    print("{:s}".format(chr(a)), end="")
