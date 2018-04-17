#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    myList = []
    for x in my_list:
        if x % 2 is 0:
            myList.append(True)
        else:
            myList.append(False)
    return(myList)
