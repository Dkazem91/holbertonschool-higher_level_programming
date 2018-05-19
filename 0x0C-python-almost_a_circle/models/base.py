#!/usr/bin/python3
"""class base"""
import json


class Base:
    """this is inside the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inits the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string"""
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(json_string):
        """returns list of jsons"""
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        if list_objs is None:
            jsons = []
        else:
            jsons = [cls.to_json_string(x.to_dictionary()) for x in list_objs]
        with open(cls.__name__+'.json', 'w') as f:
            f.write(str(jsons))
