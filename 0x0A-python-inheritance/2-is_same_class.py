#!/usr/bin/python3
"""Define the is_same_class function"""


def is_same_class(obj, a_class):
    """
    show True or False about if the object is an instance

    parametters:
    *obj: an Python object to use
    *a_class: a class to use

    return:
    *True if instance or False if not
    """
    return type(obj) == a_class
