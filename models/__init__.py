#!/usr/bin/python
"""
    Make necessary imports.
"""
from os import getenv
from models.engine import *

# if storage is db.
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = db_storage.DBStorage()
    storage.reload()
else:
    storage = file_storage.FileStorage()
    storage.reload()

__all__ = ["user", "amenity", "city", "place", "review", "state"]
