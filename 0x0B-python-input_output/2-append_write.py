#!/usr/bin/python3
"""Define append_write function"""


def append_write(filename="", text=""):
    """
    overwrite a text file append text at the end with UTF-8 encoding

    parametters:
    *filename: a string of the file name
    *text: a string with the text to write

    return:
    *the number of characters written
    """

    with open(filename, mode="a", encoding="utf-8") as myfile:
        return (myfile.write(text))
