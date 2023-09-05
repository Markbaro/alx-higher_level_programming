#!/usr/bin/python3
"""
This module defines `print_square`
The function prints a square with the character #
"""


def print_square(size):
    """Prints a square where size is
    the length and width of the square.
    """

    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for x in range(size):
        print('#' * size)
