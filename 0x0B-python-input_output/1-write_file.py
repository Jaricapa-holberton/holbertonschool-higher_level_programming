#!/usr/bin/python3
"""Define write_file function"""


def write_file(filename="", text=""):
    """
    Read a text file (UTF8) and prints it to stdout

    parametters:
    *filename: a string of the file name
    *text: a string with the text to write

    return:
    *the number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as myfile:
        return (myfile.write(text))
