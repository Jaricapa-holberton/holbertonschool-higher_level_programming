#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = ord(c)
        if 97 <= c <= 122:
            c = c - 32
        print("{:c}".format(c), end="")
    print()
