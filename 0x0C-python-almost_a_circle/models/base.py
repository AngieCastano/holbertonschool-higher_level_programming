#!/usr/bin/python3
import json
"""Class Base"""


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ args: id = object's id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            empty_list = []
            return empty_list
        ret = json.dumps(list_dictionaries)
        return ret

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        string = ""
        dictionaries = [cls.to_json_string([_list.to_dictionary()])
                        for _list in list_objs]
        for elem in dictionaries:
            string += elem
        with open(cls.__name__+".json", mode="w", encoding="utf-8") as File:
            File.write(string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string:"""
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set"""
        new_instance = cls(1, 1, 1, 1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """load from file"""
        with open(cls.__name__+".json", mode="r", encoding="utf-8") as File:
            data = File.read()
            print(data)
            data2 = Base.from_json_string(data)
            print(len(data2))
            print(type(data2))
