/*
  Leslie Espino
  Assignment 5.2 - Projections
  assignment5.2.js
  MongoDB document manipulation and projection queries.
*/

/*
  Add a new user to the users collection.
*/
db.users.insertOne({
  firstName: "Leslie",
  lastName: "Espino",
  employeeId: "1998",
  email: "lespino@me.com",
  dateCreated: new Date(),
});

/*
  Update Mozart's email address.
*/
db.users.updateOne(
  { lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } },
);

/*
  Display all users showing only first name, last name, and email.
*/
db.users.find(
  {},
  {
    firstName: 1,
    lastName: 1,
    email: 1,
    _id: 0,
  },
);
