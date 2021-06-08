#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Creates a class Square for do some operations


    atributes:
    *none
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a square object

        parametters:
        *size (int): Square's size
        *x (int): Square's x position
        *y (int): Square's y position
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Method to return (getter) the value of private attribute.
        Returns:
            Value of width.
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Method to setter private attribute.
        Args:
            value (int): New size of size.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return an informal printable string of a Square object.
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
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
        attributes = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            Base.__init__(self, args[0])
            for position, value in enumerate(args[1:], 1):
                setattr(self, attributes[position], value)
        else:
            for key in kwargs.keys():
                if key in attributes:
                    if key == "id":
                        Base.__init__(self, kwargs.get(key))
                    else:
                        setattr(self, key, kwargs.get(key))

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation
        of a Square.
        """
        keys_dict = ["id", "size", "x", "y"]
        dict_rect = {}
        for keys in keys_dict:
            dict_rect.update({keys: getattr(self, keys)})
        return (dict_rect)
