#!/usr/bin/python3
def print_square(size):
    """prints a square using #

    Args:
        size (int): length of square

    Raises:
        TypeError: if size is not an integer, or if size is a float
            and is less than 0
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)sr/bin/python3    
"""class called Rectangle"""


class Rectangle:
    """defines a rectangle """

    def __init__(self, width=0, height=0):
        """initializes the instance

        Args:
            width: rectangle width
            height: rectangle height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the value of the width

        Returns:
            rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
