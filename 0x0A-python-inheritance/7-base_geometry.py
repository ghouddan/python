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
    @classmethod
    def integer_validator(self, name, value):
        """
        Validates the value passed to the method.

        Args:
        - name (str): The name of the variable to validate.
        - value (int): The value to validate.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
