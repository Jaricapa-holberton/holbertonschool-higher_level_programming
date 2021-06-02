#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""

# import module
import sys


if __name__ == "__main__":

    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        list_from_json = load("add_item.json")
    except FileNotFoundError:
        list_from_json = []

    list_from_json.extend(sys.argv[1:])
    save(list_from_json, "add_item.json")
