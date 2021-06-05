#!/usr/bin/python3
"""
Define unittests for Base class
"""
import os
import unittest
from models.base import Base


class TestBase_init(unittest.TestCase):
    """Test cases for init function in Base class"""

    def test_id_None(self):
        b1 = Base()
        _id = b1.id
        b2 = Base()
        b3 = Base(None)
        l_id = [b1.id, b2.id, b3.id]
        self.assertEqual([_id, _id + 1, _id + 2], l_id)

    def test_id_number(self):
        self.assertEqual(55, Base(55).id)

    def test_id_mix(self):
        b4 = Base()
        _id = b4.id
        b9 = Base(9)
        b5 = Base()
        l_id = [b4.id, b9.id, b5.id]
        self.assertEqual([_id, 9, _id + 1], l_id)
