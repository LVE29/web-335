/*
  Leslie Espino
  Assignment 4.3 - MongoDB Shell
  MongoDB Shell Queries
*/

/*
  Query 1:
  Display all users in the users collection.
*/
db.users.find();

/*
  Query 2:
  Display the user with the email address jbach@me.com.
*/
db.users.findOne({ email: "jbach@me.com" });

/*
  Query 3:
  Display the user with the last name Mozart.
*/
db.users.findOne({ lastName: "Mozart" });

/*
  Query 4:
  Display the user with the first name Richard.
*/
db.users.findOne({ firstName: "Richard" });

/*
  Query 5:
  Display the user with employeeId 1010.
*/
db.users.findOne({ employeeId: "1010" });
