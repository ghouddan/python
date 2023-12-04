#!/usr/bin/python3


"""
Module for is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of an
    enherited class

    Args:
        obj (any): object to check
        a_class (any): class to check against

    Returns:
        bool: True if the object is an instance of, or of an inherited class
    """
    return isinstance(obj, a_class)
