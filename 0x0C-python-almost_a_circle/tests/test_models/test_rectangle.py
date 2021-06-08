#!/usr/bin/python3
"""
Unittest for Almost is a circle project.
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch


class TestRectangle_RaiseErrors(unittest.TestCase):
    """Class to add Unittests for a function."""

    def test_no_arguments(self):
        """Test to create an object without arguments"""
        with self.assertRaises(TypeError):
            test = Rectangle()
        with self.assertRaises(TypeError):
            test = Rectangle(4)

    def test_Type_Error_width(self):
        """Test to validate correct outputs messages error"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tst = Rectangle(None, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            tst = Rectangle(None, None)

    def test_Value_Error_width(self):
        """Test to validate correct outputs messages error"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            tst = Rectangle(0, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            tst = Rectangle(-2, 0)

    def test_Type_Error_height(self):
        """Test to validate correct outputs messages error"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            tst = Rectangle(2, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            tst = Rectangle(2, None)

    def test_Value_Error_height(self):
        """Test to validate correct outputs messages error"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -2)

    def test_Type_Error_x(self):
        """Test to validate correct outputs messages error"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tst = Rectangle(2, 2, "x", 3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            tst = Rectangle(2, 2, 0.9, 3)

    def test_Value_Error_x(self):
        """Test to validate correct outputs messages error"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            tst = Rectangle(2, 2, -1, 3)

    def test_Type_Error_y(self):
        """Test to validate correct outputs messages error"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tst = Rectangle(2, 2, 3, "y")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            tst = Rectangle(2, 2, 3, 1.5)

    def test_Value_Error_y(self):
        """Test to validate correct outputs messages error"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            tst = Rectangle(2, 2, 1, -2)


class TestRectangle_Succes_cases(unittest.TestCase):
    """Class to prove succes cases for Rectangle Class"""

    def test_Succes_Cases(self):
        """Test to probe the succes cases"""
        rec_0 = Rectangle(5, 3)
        rec_1 = Rectangle(2, 2, 2, 2, 3)
        rec_2 = Rectangle(4, 3)
        first_id = rec_0.id
        self.assertEqual(rec_0.id, first_id)
        self.assertEqual(rec_2.id, rec_0.id + 1)
        self.assertEqual(rec_0.width, 5)
        self.assertEqual(rec_0.height, 3)
        self.assertEqual(rec_0.x, 0)
        self.assertEqual(rec_0.y, 0)
        self.assertEqual(rec_1.width, 2)
        self.assertEqual(rec_1.height, 2)
        self.assertEqual(rec_1.x, 2)
        self.assertEqual(rec_1.y, 2)
        self.assertEqual(rec_1.id, 3)

    def test_is_instance(self):
        """Test to an object is instance of rectangle"""
        r1 = Rectangle(2, 2, 3, 4, 1)
        self.assertIsInstance(r1, Rectangle)

    def test_display_update_methods(self):
        """Test to prove few methods by rectangle class"""
        Base._Base__nb_objects = 0
        self.c = Rectangle(2, 2)
        b = Rectangle(5, 10, 2, 2, 24)
        self.assertEqual(b.x, 2)
        self.assertEqual(b.id, 24)
        self.assertIsInstance(b, Rectangle)
        b.height = 15
        self.assertEqual(b.height, 15)
        b.y = 10
        self.assertEqual(b.y, 10)
        self.assertIsNone(self.c.display())
        b.update(1, 2, 3, 4, 5)
        self.assertEqual(b.y, 5)
        b.update(width=20)
        self.assertEqual(b.width, 20)

    def test_Rectangle_to_dictionary(self):
        """Test to prove the instance of return value (should be dic)"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r1.to_dictionary(), dict)
        self.assertNotIsInstance(r1.to_dictionary(), list)

    def test_rectangle_area(self):
        """Test area method"""
        a = Rectangle(10, 20)
        self.assertEqual(a.area(), 200)
        self.assertIsInstance(a.area(), int)

    def test_rectangle_errors_update(self):
        """test_rectangle_errors_update"""
        self.c = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            self.c.update(1, "hi")
            self.c.update(1, [3])

        self.c.update(unknowk=20)
        with self.assertRaises(AttributeError):
            self.c.unknowk

if __name__ == '__main__':
    unittest.main()