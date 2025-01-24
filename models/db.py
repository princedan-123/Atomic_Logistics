"""A module that creates a database client for database operations."""
from pymongo import MongoClient

client = MongoClient()
admin_collection = client['atomic_logistics']['admins']
