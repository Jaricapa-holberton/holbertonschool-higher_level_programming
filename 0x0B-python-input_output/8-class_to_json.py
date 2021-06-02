#!/usr/bin/python3
"""Define class_to_json function"""


def class_to_json(obj):
    """
    Returns a dict description with simple JSON data strcuture of an object

    parametters:
    *obj: a Python object to represent

    return:
    *returns the dictionary description
    """

    return obj.__dict__
