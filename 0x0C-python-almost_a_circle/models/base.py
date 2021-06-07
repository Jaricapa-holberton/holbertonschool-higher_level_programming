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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation
        of list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                list_convert = [list_.to_dictionary() for list_ in list_objs]
                json_list = cls.to_json_string(list_convert)
                myfile.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of the JSON string
        representation json_string.
        """
        if json_string is None or json_string == []:
            return ("[]")
        else:
            return (json.loads(json_string))
