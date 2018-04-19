#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if(value):
        for key, val in list(a_dictionary.items()):
            if val is value:
                del a_dictionary[key]
        return(a_dictionary)
