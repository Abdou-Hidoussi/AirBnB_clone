#!/usr/bin/python3
import unittest
import json
import inspect
import datetime
import os
from models.base_model import BaseModel
import unittest


class TestStringMethods(unittest.TestCase):

    def test_id(self):
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        new = BaseModel()
        self.assertEqual(type(new.created_at),
                         datetime.datetime)

    def test_updated_at(self):
        new = BaseModel()
        self.assertEqual(type(new.updated_at),
                         datetime.datetime)

    def test_str(self):
        new = BaseModel()
        self.assertEqual(str(new), "[{:s}] ({:s}) {}".format(
            new.__class__.__name__, new.id, new.__dict__))

if __name__ == '__main__':
    unittest.main()
