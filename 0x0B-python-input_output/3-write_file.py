#!/usr/bin/python3
"""
Writes a string to a text file (UTF8), returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    args: filename= name of the file, text = text to write in the file
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        numb_bites_written = myFile.write(text)
        return numb_bites_written
