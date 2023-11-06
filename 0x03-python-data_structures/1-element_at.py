#!/usr/bin/python3


def element_at(list, idex):
    if idex < 0 or idex > len(list) - 1:
        return None
    else:
        return list[idex]
