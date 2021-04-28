#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    i = 1
    if argc == 1:
        print("{:d} arguments.".format(argc - 1))
    elif argc > 1:
        print("{:d} arguments.".format(argc - 1))
        while i <= argc - 1:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
   