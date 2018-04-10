#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = int(str(number)[-1])
if(lastDigit > 5):
    print("{} and is greater than 5".format(lastDigit))
elif(lastDigit == 0):
    print("{} and is 0".format(lastDigit))
else:
    print("{} and is less than 6 and not 0".format(lastDigit))
