#!/usr/bin/python3
'''
Define a class: Square
'''


class Square:
    '''A class to represent a square.'''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Construct all the necessary attributes for the square object.
        '''

        # Check if size is a correct input
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
            self.position = position

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

    @property
    def position(self):
        "Get and stter of size"
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter of position."""

        # Validate position
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(i) is int for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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

        sep = " " if self.__position[0] > 0 else ""
        top = "\n" * self.__position[1] if self.__position[1] > 0 else ""

        print("{}".format(top), end="")

        for i in range(self.__size):
            print("{}{}".format(sep * self.__position[0], "#" * self.__size))
