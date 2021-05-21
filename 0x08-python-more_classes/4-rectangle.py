#!/usr/bin/python3
'''
Define a class: Rectangle
'''


class Rectangle():
    '''A class to represent a rectangle.'''
    def __init__(self, width=0, height=0):
        """Construct all the necessary attributes for Rectangle object."""
        self.height = height
        self.width = width

    @property
    def width(self):
        '''Getter and setter of width.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter of width."""

        # Check if width is a correct input
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Getter and setter of height.'''
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter of size."""

        # Check if height is a correct input
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''
        returns the rectangle area.
        '''

        return (self.__height * self.__width)

    def perimeter(self):
        '''
        returns the rectangle perimeter.
        '''

        if (self.__height == 0) or (self.__width == 0):
            return (0)
        else:
            return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """
        Print an string of a Rectangle object.
        """

        if (self.__height == 0) or (self.__width == 0):
            return ("")
        else:
            string_of_sym = ""
            for i in range(self.__height):
                string_of_sym += ("#" * self.__width) + "\n"
            return (string_of_sym[:-1])

    def __repr__(self):
        """
        Return an official string representation of a
        Rectangle object.
        """
# "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        rep_rectangle = "Rectangle(" + str(self.__width)
        rep_rectangle += ", " + str(self.__height) + ")"
        return (rep_rectangle)
