#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if(idx < 0 or idx >= len(my_list)):
        copyList = my_list.copy()
        return(copyList)
    del my_list[idx]
    copyList = my_list.copy()
    return(copyList)
