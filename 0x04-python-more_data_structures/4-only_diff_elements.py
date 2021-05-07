#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1_setted = set(set_1)
    not_intersection = set1_setted.symmetric_difference(set_2)
    XOR_set = list(not_intersection)
    return XOR_set
