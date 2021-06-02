#!/usr/bin/python3
"""Define fuction lookup"""


def lookup(obj):
    """
    write the list of available attributes and methods of an object

    parametters:
    *obj: a object of python

    return:
    *a list object
    """
    return(dir(obj))
