#!/usr/bin/python3
for char in range(122, 96, -1):
    upper = 32 if (char % 2 != 0) else 0
    print("{}".format(chr(char - upper)), end="")
