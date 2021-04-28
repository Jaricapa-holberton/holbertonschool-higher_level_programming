#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    i = 1
    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc > 0:
        print("{:d} arguments.".format(argc))
        while i <= argc:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
        