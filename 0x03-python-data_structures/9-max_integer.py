#!/usr/bin/python3


def max_integer(list=[]):

    if list:
        list.sort()
        return list[-1]
    else:
        return None
