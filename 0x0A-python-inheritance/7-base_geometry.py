#!/usr/bin/python3
"""Denfine BaseGeometry class"""


class BaseGeometry:
    """Create a empty class geometry"""

    def area(self):
        """
        Raise an Exception with the message area() is not implemented

        parametters:
        *self: the class itself

        return:
        *none
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a input value

        parametters:
        *self: the class itself
        *name: the data to check
        *value: the value of the data

        return:
        *none
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
