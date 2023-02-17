#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base(self):
        base1 = Base(10)
        self.assertEqual(base1.id, 10)
        self.assertEqual(Base._Base__nb_objects, 0)

        base2 = Base()
        self.assertEqual(base2.id, 1)
        self.assertEqual(base2.id, Base._Base__nb_objects)

        base3 = Base()
        self.assertEqual(base3.id, 2)
        self.assertEqual(base3.id, Base._Base__nb_objects)

        base4 = Base(7)
        self.assertEqual(base4.id, 7)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_base_alxtests(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == "__main__":
    unittest.main()