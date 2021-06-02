#!/usr/bin/python3
"""Define from_json_string function"""
# import module
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    parametters:
    *my_str: the string represented

    return:
    *a Python object
    """

    return (json.loads(my_str))
