#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a is 8 and b is 9:
            print("{:d}{:d}".format(a, b))
        elif a < b:
            print("{:d}{:d}".format(a, b), end=", ")
