#!/usr/bin/python3
"""Define the Student class"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Inicialize a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance"""

        if type(attrs) == list and all(type(i) == str for i in attrs):
            dic1 = [[k, getattr(self, k)] for k in attrs if hasattr(self, k)]
            return dict(dic1)
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""

        for key, value in json.items():
            setattr(self, key, value)
