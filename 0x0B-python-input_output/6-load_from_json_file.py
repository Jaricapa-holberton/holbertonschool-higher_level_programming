#!/usr/bin/python3
"""Define load_from_json_file function"""
# import module
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

    parametters:
    *my_obj: a Python object to represent
    *filename: a string of the file name

    return:
    *the number of characters written
    """

    with open(filename, mode="r") as myfile:
        return (json.load(myfile))
