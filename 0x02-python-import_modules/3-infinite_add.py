#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    sum = 0
    i = 1
    if argc <= 1:
        print(sum)
    else:
        while i <= argc:
            sum = sum + int(argv[i])
            i = i + 1
        print(sum)
