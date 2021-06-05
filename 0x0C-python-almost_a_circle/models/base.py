#!/usr/bin/python3
class Base:
    """
    Creates a class Base for do some operations

    atributes:
    *__nb_objects (int): The number of instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Inicialize a Base object

        parametters:
        *self: the class itself
        *id: the identification of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
