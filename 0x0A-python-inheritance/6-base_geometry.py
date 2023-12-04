#!/usr/bin/python3


"""
Module: BaseGeometry

This module provides the definition for the BaseGeometry class,
 class for geometric calculations.

"""


class BaseGeometry:
    """
    defines the basic structure for geometric calculations.

    Methods:
    - area(): Raises an exception and should be implemented in derived classes.
    """

    @classmethod
    def area(self):
        """
        Calculates the area of the geometric shape.

        This method is intended to be overridden by derived classes to
        provide the specific implementaion.

        Raises:
        Exception: Always raises an exception when called.
        """
        raise Exception("area() is not implemented")
