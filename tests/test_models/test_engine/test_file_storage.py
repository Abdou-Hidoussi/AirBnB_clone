#!/usr/bin/python3
import unittest
import json
import inspect
import datetime
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorageMethods(unittest.TestCase):

    def test_base_model_save(self):
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

if __name__ == '__main__':
    unittest.main()
