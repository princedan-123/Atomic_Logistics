"""Creates a super admin in the database."""
import sys
from werkzeug.security import generate_password_hash
from db import admin_collection
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('Usage: python create_super_admin.py <password>')
    sys.exit(1)
password = sys.argv[1]
if len(password) > 15:
    print('password should not be more than 15 characters')
    sys.exit(1)
hashed_pw = generate_password_hash(password)
updated = admin_collection.update_one({'firstName': 'Daniel'}, {'$set': {'password': hashed_pw}})
if updated and updated.modified_count > 0:
    print('super admin updated: password updated')