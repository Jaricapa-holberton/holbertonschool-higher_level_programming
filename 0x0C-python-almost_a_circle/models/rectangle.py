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
        Initialize a rectangle object

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
        """
        Method to return (getter) the value of private attribute.
        Returns:
            Value of width.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Method to setter private attribute.
        Args:
            value (int): New size of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Method to return (getter) the value of private attribute.
        Returns:
            Value of heigth.
        """
        return s
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Method to setter private attribute.
        Args:
            value (int): New size of Height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Method to return (getter) the value of private attribute.
        Returns:
                Value of x.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Method to setter private attribute.
        Args:
            value : New value of x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Method to return (getter) the value of private attribute.
        Returns:
                Value of y.
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Method to setter private attribute.
        Args:
            value : New value of y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method that returns the area value of the Rectangle instance.
        Returns:
            Area of the Rectangle object (width * height).
        """
        return (self.height * self.width)

    def display(self):
        """
        public method that prints in stdout the Rectangle instance
        with the character #. (W * H)
        """
        for i in range(self.__y):
            print()
        for j in range(self.height):
            for k in range(self.__x):
                print(' ', end='')
            row = ""
            for l in range(self.width):
                row += "#"
            print(row)

    def __str__(self):
        """
        Return an informal printable string of a Rectangle object.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}". format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        ))

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by adding the public method that
        assigns an argument to each attribute.
        
        1st argument should be the id attribute.
        2nd argument should be the size attribute.
        3rd argument should be the x attribute.
        4th argument should be the y attribute.
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            super().__init__(args[0])
            for position, value in enumerate(args[1:], 1):
                setattr(self, attributes[position], value)
        else:
            for key in kwargs.keys():
                if key in attributes:
                    if key == "id":
                        super().__init__(kwargs.get(key))
                    else:
                        setattr(self, key, kwargs.get(key))

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation
        of a Rectangle.
        """
        keys_dict = ["id", "width", "height", "x", "y"]
        dict_rect = {}
        for keys in keys_dict:
            dict_rect.update({keys: getattr(self, keys)})
        return (dict_rect)
