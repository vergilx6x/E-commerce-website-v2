#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import app.models
from app.models.engine import db_storage
from app.models.user import User
from app.models.base_model import BaseModel
from app.models.product import Product
from app.models.cart import Cart
from app.models.cart_item import Cart_item
from app.models.order import Order
from app.models.order_item import Order_item
from app.models.category import Category
from app.models.favorite import Favorite
import json
import os
# import pep8
import unittest
from app.models import storage
DBStorage = db_storage.DBStorage

classes = {"User": User, "Category": Category, "Product": Product, "Cart": Cart, "Cart_item": Cart_item, "Order": Order, "Order_item": Order_item, "Favorite": Favorite}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    # def test_pep8_conformance_db_storage(self):
    #     """Test that models/engine/db_storage.py conforms to PEP8."""
    #     pep8s = pep8.StyleGuide(quiet=True)
    #     result = pep8s.check_files(['models/engine/db_storage.py'])
    #     self.assertEqual(result.total_errors, 0,
    #                      "Found code style errors (and warnings).")

#     def test_pep8_conformance_test_db_storage(self):
#         """Test tests/test_models/test_db_storage.py conforms to PEP8."""
#         pep8s = pep8.StyleGuide(quiet=True)
#         result = pep8s.check_files(['tests/test_models/test_engine/\
# test_db_storage.py'])
#         self.assertEqual(result.total_errors, 0,
#                          "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(app.models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(app.models.storage.all()), dict)

    @unittest.skipIf(app.models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(app.models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(app.models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    def test_get_db(self):
        """ Tests method for obtaining an instance db storage"""
        dic = {"name": "Cundinamarca"}
        instance = State(**dic)
        storage.new(instance)
        storage.save()
        get_instance = storage.get(State, instance.id)
        self.assertEqual(get_instance, instance)

    def test_count(self):
        """ Tests count method db storage """
        dic = {"name": "Vecindad"}
        state = State(**dic)
        storage.new(state)
        dic = {"name": "Mexico", "state_id": state.id}
        city = City(**dic)
        storage.new(city)
        storage.save()
        c = storage.count()
        self.assertEqual(len(storage.all()), c)