#!/usr/bin/python3
"""
Unittest for Almost is a circle project.
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class Testsquare(unittest.TestCase):
    """Class for test square class"""

    def setUp(self):
        """setUp"""
        Base._Base__nb_objects = 0
        self.a = Square(1)
        self.b = Square(5, 0, 0, 98)
        self.c = Square(4)
        self.d = Square(2)

    def test_1_Square(self):
        """Test_1_Square"""
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.a.size, 1)
        self.assertEqual(self.b.id, 98)
        self.assertEqual(self.b.size, 5)
        self.assertEqual(self.c.size, 4)
        self.assertEqual(self.d.id, 3)

    def test_2_Update(self):
        """test_2_Square"""
        self.a.update(id=99)
        self.a.update(99, 10)
        self.assertEqual(self.a.id, 99)
        self.assertEqual(self.a.size, 10)
        with self.assertRaises(TypeError):
            self.a.update(size="Holberton")
            self.a.update("unknowk")

    def test_3_to_dictionary(self):
        """test_3_Square"""
        my_dict = self.a.to_dictionary()
        my_dict2 = self.b.to_dictionary()
        self.assertIsInstance(my_dict, dict)
        self.assertIsInstance(my_dict2, dict)

if __name__ == "__main__":
    unittest.main()