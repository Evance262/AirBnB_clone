#!/usr/bin/python3
import unittest
import pep8
import json
import inspect
import datetime
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_pep8_conformance(self):
        """Comforming tests with pep8"""
        pep8style  = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_id(self):
        pass

    def test_created_at(self):
        pass

    def test_updated_at(self):
        pass

    def test_save(self):
        pass

        def to_dict(self):
            pass

if __name__ == '__main__':
    unittest.main()