#!/usr/bin/python3


def new_in_list(list, idex, element):

    if idex < 0 or idex > len(my_list) - 1:
        return list[:]
    else:
        new_list = list[:]
        new_list[idx] = element
        return new_list
