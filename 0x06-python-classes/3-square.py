#!/usr/bin/python3
'''
Define a class: Square
'''


from typing import Sized


class Square:
    '''A class to represent a square.'''
    def __init__(self, size=0):
        '''
        Construct all the necessary attributes for the square object.
        '''

        # Check if size is a correct input
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        '''
        returns the current square area.
        '''

        return (self._Square__size ** 2)
