#!/usr/bin/python3
"""
Given an array, find the peak
"""


def find_peak(list_of_integers):
    """
    Function returns the peak of a list
    """
    if (list_of_integers != []):
        list_of_integers.sort()
        return (list_of_integers[-1])
