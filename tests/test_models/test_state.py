#!/usr/bin/python3
import unittest
import json
import inspect
import datetime
import os
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
import unittest


class TestStateMethods(unittest.TestCase):

    def test_id(self):
        new = State()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        new = State()
        self.assertEqual(type(new.created_at),
                         datetime.datetime)

    def test_updated_at(self):
        new = State()
        self.assertEqual(type(new.updated_at),
                         datetime.datetime)

    def test_str(self):
        new = State()
        self.assertEqual(str(new), "[{:s}] ({:s}) {}".format(
            new.__class__.__name__, new.id, new.__dict__))

    def test_name(self):
        new = State()
        self.assertEqual(new.name, "")

if __name__ == '__main__':
    unittest.main()
