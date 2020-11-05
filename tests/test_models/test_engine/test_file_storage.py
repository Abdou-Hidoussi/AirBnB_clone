#!/usr/bin/python3
import unittest
import pep8
import json
import inspect
import datetime
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorageMethods(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_base_model_save(self):
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

if __name__ == '__main__':
    unittest.main()
