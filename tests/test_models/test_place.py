#!/usr/bin/python3
import unittest
import json
import inspect
import datetime
import os
from models.base_model import BaseModel
from models.city import City
from models.place import Place
import unittest


class TestPlaceMethods(unittest.TestCase):

    def test_id(self):
        new = Place()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        new = Place()
        self.assertEqual(type(new.created_at),
                         datetime.datetime)

    def test_updated_at(self):
        new = Place()
        self.assertEqual(type(new.updated_at),
                         datetime.datetime)

    def test_str(self):
        new = Place()
        self.assertEqual(str(new), "[{:s}] ({:s}) {}".format(
            new.__class__.__name__, new.id, new.__dict__))

    def test_name(self):
        new = Place()
        self.assertEqual(new.name, "")

if __name__ == '__main__':
    unittest.main()
