"""
Title: Espino_usersp1.py
Author: Leslie Espino
Date: 10 July 2026
Description: Exercise 6.3 - Python with MongoDB, Part I
"""

import os
from pymongo import MongoClient

# Keeping the password outside the source file prevents it from being exposed
# when the assignment is pushed to a public GitHub repository.
password = os.environ.get("MONGODB_PASSWORD")

# Stopping early provides a clear message instead of an unclear connection
# error when the required environment variable has not been set.
if not password:
    raise ValueError("MONGODB_PASSWORD environment variable is not set.")

# Reusing one client keeps all queries on the same database connection.
client = MongoClient(
    f"mongodb+srv://web335_user:{password}@cluster0.ff65rcy.mongodb.net/"
    "?retryWrites=true&w=majority"
)

# Saving the database reference reduces the chance of querying the wrong
# database in later statements.
db = client["web335DB"]

print("All users:")

# A loop is needed because find() returns several documents.
for user in db.users.find({}):
    print(user)

print("\nUser with employeeId 1011:")

# The employee ID provides a precise way to locate the assigned user.
print(db.users.find_one({"employeeId": "1011"}))

print("\nUser with lastName Mozart:")

# This separate query demonstrates finding a user when only a name is known.
print(db.users.find_one({"lastName": "Mozart"}))

# Closing the client releases the connection once it is no longer needed.
client.close()