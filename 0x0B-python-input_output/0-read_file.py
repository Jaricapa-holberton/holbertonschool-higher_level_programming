#!/usr/bin/python3
"""Define read_file function"""

def read_file(filename=""):
    """Read a text file with UTF-8 encoding and print out"""

    with open(filename, mode="r", encoding="utf-8") as myfile:
        print(myfile.read(), end="")
