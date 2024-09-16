#!/usr/bin/python

from app import models
from app.models.base_model import BaseModel, Base
from app.models.user import User
from app.models.category import Category
from app.models.product import Product
from app.models.cart import Cart
from app.models.cart_item import Cart_item
from app.models.order import Order
from app.models.order_item import Order_item
from sqlalchemy import create_engine
from app.models.favorite import Favorite
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


classes = {"User": User, "Category": Category, "Product": Product, "Cart": Cart, "Cart_item": Cart_item, "Order": Order, "Order_item": Order_item, "Favorite": Favorite}

class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        WEB_MYSQL_USER = getenv('WEB_MYSQL_USER')
        WEB_MYSQL_PWD = getenv('WEB_MYSQL_PWD')
        WEB_MYSQL_HOST = getenv('WEB_MYSQL_HOST')
        WEB_MYSQL_DB = getenv('WEB_MYSQL_DB')
        WEB_ENV = getenv('WEB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(WEB_MYSQL_USER,
                                             WEB_MYSQL_PWD,
                                             WEB_MYSQL_HOST,
                                             WEB_MYSQL_DB))
        if WEB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
    
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def rollback(self):
        """Rolls back the previous state"""

        self.__session.rollback()

    def get_user(self, username):
        """Gets user by username"""
        users = self.all(User)
        for value in users.values():
            if (value.username == username):
                return value
            

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count