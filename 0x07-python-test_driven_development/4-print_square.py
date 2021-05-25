#!/usr/bin/python3
"""Function that prints a square maked with only "#" character"""


def print_square(size):
    """
    Function that prints a square maked with only "#" character.
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for rows in range(size):
        for columns in range(size):
            print("{}".format('#'), end='')
        print()
