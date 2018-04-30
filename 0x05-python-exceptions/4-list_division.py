#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for x in range(list_length):
        result = 0
        try:
            result = my_list_1[x] / my_list_2[x]
        except IndexError:
            result = 0
            print("{}".format("Out of range"))
        except (ValueError, TypeError):
            result = 0
            print("{}".format("Wrong type"))
        except ZeroDivisionError:
            result = 0
            print("{}".format("division by 0"))
        finally:
            if(result):
                newList.append(result)
            else:
                newList.append(0)
    return(newList)
