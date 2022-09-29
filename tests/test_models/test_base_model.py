#!/usr/bin/python3
""" test module for base model """
import unittest
from models.base_model import BaseModel
from datetime import *


class BaseModelTest(unittest.TestCase):
    """ tests for base model """

    def test_Constructor(self):
        test_instance = BaseModel()
        self.assertIsInstance(test_instance, BaseModel)

    def test_CreatedAt(self):
        test_instance = BaseModel()
        self.assertIsInstance(test_instance.created_at, datetime)

    def test_UpdatedAt(self):
        test_instance = BaseModel()
        self.assertIsInstance(test_instance.updated_at, datetime)

    def test_IDIsString(self):
        test_instance = BaseModel()
        self.assertIsInstance(test_instance.id, str)

    def test_ExtraAttr(self):
        test_instance = BaseModel()
        test_instance.number = 69
        self.assertIsInstance(test_instance.number, int)

    def test_Save(self):
        test_instance = BaseModel()
        test_instance.save()
        self.assertNotEqual(test_instance.created_at, test_instance.updated_at)

    def test_ToDict(self):
        test_instance = BaseModel()
        self.assertIsInstance(test_instance.to_dict(), dict)
