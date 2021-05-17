#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("Inside result: {:d}".format(result))
    except ZeroDivisionError:
        result = None
        print("Inside result: {:s}".format(result))
    finally:
        return (result)
