#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    args: filename =  name of the file to read
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
