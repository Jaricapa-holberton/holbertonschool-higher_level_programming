#!/usr/bin/python3
"""Define function add_integer."""


def add_integer(a, b=98):
    """
    Add two numbers
    Parameters:
        a (int or float)
        b (int or float) for default = 98
    Return: Integer addition of a and b.
    Raises:
        TypeError: When a or b is a non-integer and non-float.
    """
    if ((type(a) is not int) and (type(a) is not float)):
        raise TypeError("a must be an integer")
    if ((type(b) is not int) and (type(b) is not float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
