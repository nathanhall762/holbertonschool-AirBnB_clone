#!/usr/bin/python3
"""init file for bnb project"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
