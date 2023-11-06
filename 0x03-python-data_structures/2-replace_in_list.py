#!/usr/bin/python3


def replace_in_list(list, idex, element):

    if idex < 0 or idex > len(list) - 1:
        return list
    else:
        list[idex] = element
        return list
