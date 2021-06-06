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
        Inicialize a square object

        parametters:
        *size (int): Square's size
        *x (int): Square's x position
        *y (int): Square's y position
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter or Setter for Square's size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Method to setter private attribute.
        Args:
            value (int): New size of size.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return an informal printable string of a Square object."""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
            ))
