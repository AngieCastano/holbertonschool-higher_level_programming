#!/usr/bin/python3
"""
function that returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    """
    args: filename = name of the file
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        for counter, line in enumerate(myFile, 1):
            pass
        return counter
