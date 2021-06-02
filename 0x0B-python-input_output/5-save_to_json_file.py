#!/usr/bin/python3
"""Define save_to_json_file function"""
# import module
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    parametters:
    *my_obj: a Python object to represent
    *filename: a string of the file name

    return:
    *the number of characters written
    """

    with open(filename, mode="w") as myfile:
        json.dump(my_obj, myfile)
