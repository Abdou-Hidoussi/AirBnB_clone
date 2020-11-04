#!/usr/bin/python3
import unittest
import json
import inspect
import datetime
import os
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
import unittest


class TestReviewMethods(unittest.TestCase):

    def test_id(self):
        new = Review()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        new = Review()
        self.assertEqual(type(new.created_at),
                         datetime.datetime)

    def test_updated_at(self):
        new = Review()
        self.assertEqual(type(new.updated_at),
                         datetime.datetime)

    def test_str(self):
        new = Review()
        self.assertEqual(str(new), "[{:s}] ({:s}) {}".format(
            new.__class__.__name__, new.id, new.__dict__))

    def test_text(self):
        new = Review()
        self.assertEqual(new.text, "")

    def test_user_id(self):
        new = Review()
        self.assertEqual(new.user_id, "")

    def test_place_id(self):
        new = Review()
        self.assertEqual(new.place_id, "")

if __name__ == '__main__':
    unittest.main()
