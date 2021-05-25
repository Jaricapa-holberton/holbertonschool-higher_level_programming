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
    if ((type(a) != int) and (type(a) != float)):
        raise TypeError("a must be an integer")
    if ((type(b) != int) and (type(b) != float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
