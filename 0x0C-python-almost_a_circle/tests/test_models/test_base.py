#!/usr/bin/python3
"""Test class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base(self):
        """
        Test base
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(3)
        b5 = Base()
        b6 = Base(1000000)
        b6.id = 9999999
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5, 0)
        self.assertEqual(b6.id, 9999999)
