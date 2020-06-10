#!/usr/bin/python3
"""Class Base"""
import json
import csv


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
            return "[]"
        ret = json.dumps(list_dictionaries)
        return ret

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            dictionaries = [_list.to_dictionary() for _list in list_objs]
            string = cls.to_json_string(dictionaries)
        else:
            string = "[]"
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
        if cls.__name__ == "Square":
            new_instance = cls(1)
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """load from file"""
        try:
            with open(cls.__name__+".json", mode="r", encoding="utf-8") as F:
                data = F.read()
                data2 = Base.from_json_string(data)
                return [cls.create(**_list) for _list in data2]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializesin CSV"""
        with open(cls.__name__+".csv", mode="w") as CSV:
            dictionaries = [_list.to_dictionary() for _list in list_objs]
            fieldnames = ['x', 'y', 'id', 'height', 'width']
            writer = csv.DictWriter(CSV, fieldnames=fieldnames)
            for row in dictionaries:
                writer.writerow(row)
