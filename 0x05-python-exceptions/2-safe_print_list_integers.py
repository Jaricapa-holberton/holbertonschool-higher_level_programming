#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    list_len = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            list_len += 1
        except (TypeError, ValueError):
            pass
    print("")
    return list_len
