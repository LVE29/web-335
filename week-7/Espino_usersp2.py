"""
Title: Espino_usersp2.py
Author: Leslie Espino
Date: 19 July 2026
Description: Exercise 7.3 - Python with MongoDB, Part II
"""

from pymongo import MongoClient
import datetime
import getpass
from urllib.parse import quote_plus

# Requesting the password when the program runs prevents a database password
# from being stored in the file and exposed when the project is pushed to GitHub.
password = quote_plus(getpass.getpass("Enter your MongoDB password: "))

# quote_plus safely formats special characters that may appear in a password
# so they do not interfere with the structure of the connection string.
connection_string = (
    f"mongodb+srv://web335_user:{password}"
    "@cluster0.ff65rcy.mongodb.net/"
    "?retryWrites=true&w=majority"
)

client = MongoClient(connection_string)
db = client["web335DB"]

# A unique employee ID makes it possible to locate the same document during
# each operation without accidentally changing another user in the collection.
leslie = {
    "firstName": "Leslie",
    "lastName": "Espino",
    "employeeId": "LE2026",
    "email": "leslie.espino@example.com",
    "dateCreated": datetime.datetime.now(datetime.timezone.utc)
}

db.users.insert_one(leslie)

# Searching by the unique employee ID confirms that MongoDB saved the document
# instead of relying only on the insert operation completing without an error.
print("User created:")
print(db.users.find_one({"employeeId": "LE2026"}))

# $set is used because only the email should change; replacing the entire
# document could accidentally remove fields that are not included in the update.
db.users.update_one(
    {"employeeId": "LE2026"},
    {
        "$set": {
            "email": "leslie.espino@web335.com"
        }
    }
)

# Retrieving the document again provides evidence that the new email address
# was stored in the database rather than changed only inside the Python program.
print("\nUser updated:")
print(db.users.find_one({"employeeId": "LE2026"}))

# The same employee ID is used for deletion to ensure that only the document
# created for this exercise is removed from the users collection.
delete_result = db.users.delete_one({"employeeId": "LE2026"})

print("\nDelete result:")
print(delete_result)

# MongoDB should return None because a deleted document should no longer match
# the search, which verifies that the delete operation was successful.
print("\nUser after deletion:")
print(db.users.find_one({"employeeId": "LE2026"}))

client.close()