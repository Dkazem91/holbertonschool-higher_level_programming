#!/usr/bin/python3
# finds peak


def search(lo, h, ints):
    mid = (lo + h) // 2
    if lo == h:
        return ints[h]
    if ints[mid] < ints[mid + 1]:
        return(search(mid + 1, h, ints))
    return(search(lo, mid, ints))


def find_peak(list_of_integers):
    if not list_of_integers:
        return
    return(search(0, len(list_of_integers) - 1, list_of_integers))
