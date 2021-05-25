#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """Class to add Unittests for a function."""

    def test_max_int(self):
        """Unittest for succes Cases in function
            max_integer.
        Test for:
            list with integers given.
            list with floats given.
            list with negative floats and integer given.
            Empty list.
        """

        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([5, 4, 3, 1]), 5)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-5.0, -50, 0]), 0)
        self.assertEqual(max_integer([0.9, 0.995, 0.0995]), 0.995)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()