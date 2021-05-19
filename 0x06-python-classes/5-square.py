#!/usr/bin/python3
'''
Define a class: Square
'''


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

    @property
    def size(self):
        '''Getter and setter of size.'''
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter of size."""

        # Check if size is a correct input
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def area(self):
        '''
        returns the current square area.
        '''

        return (self._Square__size ** 2)

    def my_print(self):
        '''Print a square.'''

        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__size):
                print("{}".format("#" * self.__size))
