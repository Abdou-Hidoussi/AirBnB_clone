#!/usr/bin/python3
import unittest
import json
import inspect
import datetime
import os
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
import unittest


class TestUserMethods(unittest.TestCase):

    def test_id(self):
        new = User()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        new = User()
        self.assertEqual(type(new.created_at),
                         datetime.datetime)

    def test_updated_at(self):
        new = User()
        self.assertEqual(type(new.updated_at),
                         datetime.datetime)

    def test_str(self):
        new = User()
        self.assertEqual(str(new), "[{:s}] ({:s}) {}".format(
            new.__class__.__name__, new.id, new.__dict__))

    def test_email(self):
        new = User()
        self.assertEqual(new.email, "")

    def test_password(self):
        new = User()
        self.assertEqual(new.password, "")

    def test_first_name(self):
        new = User()
        self.assertEqual(new.first_name, "")

    def test_last_name(self):
        new = User()
        self.assertEqual(new.last_name, "")

if __name__ == '__main__':
    unittest.main()
