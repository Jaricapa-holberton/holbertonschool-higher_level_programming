#!/usr/bin/python3
"""
Unittest for Almost is a circle project.
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Class to add Unittests for a function."""
    def test_id_None(self):
        """Test for prove id None"""
        b1 = Base()
        self.assertTrue(b1.id, 1)

    def test_id_assignment(self):
        """Test for prove id increment"""
        b2 = Base(22)
        self.assertTrue(b2.id, 22)
        b3 = Base()
        self.assertTrue(b3.id, 2)

if __name__ == '__main__':
    unittest.main()