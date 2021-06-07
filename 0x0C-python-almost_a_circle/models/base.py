#!/usr/bin/python3
import json

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

    def to_json_string(list_dictionaries):
        return (json.dumps(list_dictionaries))

    def save_to_file(cls, list_objs):
        return (json.loads(list_objs))
