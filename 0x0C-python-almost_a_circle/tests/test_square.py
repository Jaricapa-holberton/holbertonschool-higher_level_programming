#!/usr/bin/python3
"""
Define unittests for Rectanagle class
"""
import unittest
from unittest.mock import patch
from models.square import Square


class TestSquare_init(unittest.TestCase):
    """Test cases for init methods in Square class"""

    def test_correct_args(self):
        s1 = Square(10)
        s2 = Square(1, 11)
        s3 = Square(10, 2, 1, 12)
        s4 = Square(10, id=13, y=1, x=2)

        ts = (s1, s2, s3, s4)
        id1 = s1.id
        l_real = [[ar.width, ar.height, ar.x, ar.y, ar.id] for ar in ts]
        l_exp = [
            [10, 10, 0, 0, id1],
            [1, 1, 11, 0, id1 + 1],
            [10, 10, 2, 1, 12],
            [10, 10, 2, 1, 13]]
        self.assertEqual(l_exp, l_real)

    def test_set_size(self):
        s = Square(1)

        s.size = 2
        l_real = [s.width, s.height, s.x, s.y]
        self.assertEqual([2, 2, 0, 0], l_real)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "-20"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -20

    def test_Incorrect_size(self):
        tTypeError = (1.2, "1", True, None)
        for case in tTypeError:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Square(case)

        tValueError = (-1, 0)
        for case in tValueError:
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Square(case)

    def test_Incorrect_x(self):
        tTypeError = ((1, 1.2), (1, "1"), (1, True), (1, None))
        for case in tTypeError:
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Square(case[0], case[1])

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -3)

    def test_Incorrect_y(self):
        tTypeError = (
            (1, 2, 1.2),
            (1, 2, "1"),
            (1, 2, True),
            (1, 2, None))
        for case in tTypeError:
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Square(case[0], case[1], case[2])

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, y=-3)