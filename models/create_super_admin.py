"""Creates a super admin in the database."""
import sys
from werkzeug.security import generate_password_hash
from models.db import admin_collection
password = sys.argv[0]
if len(password) > 15:
    print('password should not be more than 15 characters')
    sys.exit(1)
hashed_pw = generate_password_hash(password)
updated = admin_collection.updateOne({'firstName': 'Daniel'}, {'password': 'hashed_pw'})
if (updated and)
