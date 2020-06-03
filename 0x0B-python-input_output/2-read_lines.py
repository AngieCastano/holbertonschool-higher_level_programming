#!/usr/bin/python3
"""
 function that reads n lines of a text file (UTF8) and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """
    args: filename = name of the file, nb_lines =  number of lines to read
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        counter = 0
        for counter, line in enumerate(myFile, 1):
            pass
        myFile.seek(0)
        if nb_lines < 1 or nb_lines >= counter:
            print(myFile.read(), end="")
        else:
            for counter, line in enumerate(myFile, 1):
                if counter > nb_lines:
                    break
                print(line, end="")
