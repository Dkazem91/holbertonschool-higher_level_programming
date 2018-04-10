#!/usr/bin/python3
def uppercase(str):
    uppercase = 0
    for i in str:
        if(ord(i) >= 97 and ord(i) <= 122):
            uppercase = 32
        else:
            uppercase = 0
        print("{}".format(chr(ord(i) - uppercase)), end='')
    print()
