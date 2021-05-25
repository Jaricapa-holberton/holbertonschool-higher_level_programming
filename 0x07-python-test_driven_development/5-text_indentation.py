#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    else:
        buffer = ""
        for c in text:
            buffer += c
            if ((c == '.') or (c == ':') or (c == '?')):
                buffer.strip()
                print(buffer + '\n')
                buffer = ""
