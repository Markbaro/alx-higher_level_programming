#!/usr/bin/python3
"""
This module defines `text_indentation`
The function prints a text with 2 new lines after each of characters
"""


def text_indentation(text):
    """
    splits a text after each of these characters "?", ":", "."
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
