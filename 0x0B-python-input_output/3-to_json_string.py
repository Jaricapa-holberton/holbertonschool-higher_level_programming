#!/usr/bin/python3
"""Define to_json_string function"""
# import module
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    parametters:
    *my_obj: the object to represent

    return:
    *a string as the JSON representation of an object
    """

    return (json.dumps(my_obj))
