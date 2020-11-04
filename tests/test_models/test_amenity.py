#!/usr/bin/python3
import unittest
import json
import inspect
import datetime
import os
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
import unittest


class TestAmenityMethods(unittest.TestCase):

    def test_id(self):
        new = Amenity()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        new = Amenity()
        self.assertEqual(type(new.created_at),
                         datetime.datetime)

    def test_updated_at(self):
        new = Amenity()
        self.assertEqual(type(new.updated_at),
                         datetime.datetime)

    def test_str(self):
        new = Amenity()
        self.assertEqual(str(new), "[{:s}] ({:s}) {}".format(
            new.__class__.__name__, new.id, new.__dict__))

    def test_name(self):
        new = Amenity()
        self.assertEqual(new.name, "")

if __name__ == '__main__':
    unittest.main()
