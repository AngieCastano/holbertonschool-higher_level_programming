#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    args: filename = where the object string is written
    """
    with open(filename, encoding="utf-8") as File:
        return json.load(File)
