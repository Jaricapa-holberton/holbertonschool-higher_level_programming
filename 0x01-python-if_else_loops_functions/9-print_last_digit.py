#!/usr/bin/python3
def print_last_digit(number):
    last_num = abs(number) % 10
    print(last_num, end="")
    return (last_num)
