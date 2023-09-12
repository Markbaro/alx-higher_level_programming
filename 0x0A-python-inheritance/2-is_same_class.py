#!/usr/bin/python3
"""class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj : The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True - If obj is exactly an instance of a_class -
        Otherwise - False.

    if type(obj) == a_class:
        return True
    return False
    """
    return type(obj) is a_class
