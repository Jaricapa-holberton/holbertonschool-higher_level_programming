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
