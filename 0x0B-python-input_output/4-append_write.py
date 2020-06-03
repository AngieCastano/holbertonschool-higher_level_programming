#!/usr/bin/python3
"""
appends a string at a text file(UTF8),ret the number of characters added
"""


def append_write(filename="", text=""):
    """
    args: filename= name of the file, text = text to write in the file
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        numb_bites_written = myFile.write(text)
        return numb_bites_written
