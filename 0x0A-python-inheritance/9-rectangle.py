#!/usr/bin/python3
"""Define Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a object Rectangle"""

    def __init__(self, width, height):
        """
        Inicialize a Rectangle object

        parametters:
        *self: the class itself
        *width: the width of the rectangle
        *height: the height of the rectangle

        return:
        *none
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the Rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Return an informal representation of a rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
