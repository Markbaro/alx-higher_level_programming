#!/usr/bin/python3
"""Unittests for max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_ordinary(self):
        """Test an ordinary list"""
        l = [1, 2, 3, 4]
        self.assertEqual(max_integer(l), 4)

    def test_notInt(self):
        """Test with a list of non-ints and ints:"""
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty_list(self):
        """Test an empty list."""
        l = []
        self.assertEqual(max_integer(l), None)

    def test_negative(self):
        """Test with a list of negative values to return the max"""
        l = [-8, -6, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_one_element_list(self):
        """Test a list with a single element."""
        l = [3]
        self.assertEqual(max_integer(l), 3)

    def test_floats(self):
        """Test a list of floats."""
        l = [7.90, 16.85, -20.23, 0.07, 5.0]
        self.assertEqual(max_integer(l), 16.85)

    def test_intsfloats(self):
        """Test a list of ints and floats."""
        intsfloats = [1.00, 5.5, -10, 20, 13.0]
        self.assertEqual(max_integer(intsfloats), 20)

    def test_similar(self):
        """Test with a list of identical values: should return the value"""
        l = [1, 1, 1, 1]
        result = max_integer(l)
        self.assertEqual(result, 1)

    def test_blank(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [9, 8, 7, 6]
        self.assertEqual(max_integer(max_at_beginning), 4)

if __name__ == '__main__':
    unittest.main()
