#!/usr/bin/python3
"""Define class MyList"""


class MyList(list):
    """
    An inherited list class

    methods:
    *print_sorted(): Print a sorted list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)

        parametters:
        *self: the class itself

        return:
        *none
        """
        print(sorted(self))
