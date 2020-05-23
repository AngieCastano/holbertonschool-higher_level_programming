#!/usr/bin/python3
"""Function that prints
   a text with 2 new lines after
   each of these characters: ., ? and :

"""


def text_indentation(text):
    """
    text = text to indent
    """
    types = [str]
    check = ['.', '?', ':']
    if type(text) not in types:
        raise TypeError("text must be a string")
    new = []
    for i, char in enumerate(text):
        if i != len(text) - 1:
            if char == " ":
                if text[i + 1] not in check:
                    new.append(char)
            else:
                new.append(char)
            if char in check:
                new.append("\n\n")
    print("".join(new))
