#!/usr/bin/python3
def common_elements(set_1, set_2):
    set1_setted = set(set_1)
    intersection = set1_setted.intersection(set_2)
    set_intersection = list(intersection)
    return set_intersection
