#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Operator overiding  == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Method override != operator with == behavior."""
        return self.real == value
