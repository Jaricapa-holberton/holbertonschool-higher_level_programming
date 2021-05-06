#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    def evennum(n):
        if (n % 2 == 0):
            return True
        else:
            return False
    new_list = [evennum(i) for i in my_list]
    return (new_list)
