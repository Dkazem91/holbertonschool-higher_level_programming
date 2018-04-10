#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if(i is 8 and j is 9):
            print(str(i) + str(j))
        elif(j > i):
            print(str(i) + str(j) + ", ", end="")
