#!/usr/bin/python3
"""
initialize the models package
"""


from app.models.engine.db_engine import DBStorage
    
storage = DBStorage()
storage.reload()
