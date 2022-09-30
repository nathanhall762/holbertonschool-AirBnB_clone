#!/usr/bin/python3
"""Test module for base model class."""
import unittest
from unittest import mock
from models.base_model import BaseModel
from datetime import *


class BaseModelTest(unittest.TestCase):
    """Tests for base model."""

    def test_Constructor(self):
        """Test that object is created correctly."""
        test_instance = BaseModel()
        self.assertIsNotNone(test_instance)
        self.assertIsInstance(test_instance, BaseModel)
        test_instance.name = "name"
        test_instance.selfworth = 100
        attrs_dict = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "selfworth": int
        }
        for attr, typ in attrs_dict.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, test_instance.__dict__)
                self.assertIsInstance(test_instance.__dict__[attr], typ)
        self.assertEqual(test_instance.name, "name")
        self.assertEqual(test_instance.selfworth, 100)

    def test_datetime(self):
        """Test that created_at and updated_at are equal upon
        object creation, are not the same object, and that
        save method updates updated_at."""
        test_instance = BaseModel()
        self.assertEqual(test_instance.created_at, test_instance.updated_at)
        self.assertIsNot(test_instance.created_at, test_instance.updated_at)
        test_instance.save
        self.assertNotEqual(test_instance.created_at, test_instance.updated_at)

    def test_ToDict(self):
        """Test that to_dict returns dict with correct values and type."""
        test_instance = BaseModel()
        self.assertIsInstance(test_instance.to_dict(), dict)
        test_instance.name = "name"
        my_dict = test_instance.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "__class__",
                          "name"]
        self.assertCountEqual(my_dict, expected_attrs)
        self.assertEqual(my_dict['__class__'], 'BaseModel')
        self.assertEqual(my_dict['created_at'],
                         test_instance.created_at.strftime(
                             "%Y-%m-%dT%H:%M:%S.%f"))

    def test_strMethod(self):
        """Test that str method prints expected string."""
        test_instance = BaseModel()
        expected = "[BaseModel] ({}) {}".format(test_instance.id,
                                                test_instance.__dict__)
        self.assertEqual(expected, str(test_instance))

    def test_Kwargs(self):
        """Test that BaseModel instantiation occurs with kwargs."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.id, my_model.id)

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method functions properly."""
        test_instance = BaseModel()
        test_instance.save()
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.saved.called)
