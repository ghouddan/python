#!/usr/bin/python3


def add_tuple(tupleB=(), tupleB=()):
    if len(tupleA) < 1:
        tupleA = (0, 0)
    elif len(tupleA) < 2:
        tupleA = (tupleA[0], 0)
    if len(tuple_B) < 1:
        tupleB = (0, 0)
    elif len(tupleB) < 2:
        tupleB = (tupleB[0], 0)
    rest = (tupleA[0] + tupleA[0], tupleA[1] + tupleB[1])
    return rest
