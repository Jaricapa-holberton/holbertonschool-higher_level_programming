#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """
    Creates a class Rectangle for do some operations


    atributes:
    *none
    """

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Inicialize a rectangle object

        parametters:
        *width (int): Rectangle's width
        *height (int): Rectangle's height
        *x (int): Rectangle's x position
        *y (int): Rectangle's y position
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter or Setter for Rectangle's width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter or Setter for Rectangle's height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter or Setter for Rectangle's x position"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter or Setter for Rectangle's y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.height * self.width)
