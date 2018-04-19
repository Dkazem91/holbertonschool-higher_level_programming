#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    if(roman_string and isinstance(roman_string, str)):
        iT = {'D': 500, 'C': 100, 'M': 1000, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        aList = [iT.get(x) for x in roman_string]
        for idx, char in enumerate(aList):
            if(idx < len(aList) - 1):
                if aList[idx + 1] > char:
                    sum -= char
                else:
                    sum += char
            else:
                sum += char
    return(sum)
