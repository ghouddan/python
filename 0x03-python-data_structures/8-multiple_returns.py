#!/usr/bin/python3


def multiple_returns(sentence):

    lent = len(sentence)
    if sentence:
        first = sentence[0]
    else:
        first = None
    return (lent, first)
