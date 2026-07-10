/*
  Title: Espino-assignment6.2.js
  Author: Leslie Espino
  Date: July 10, 2026
  Description: MongoDB queries for Assignment 6.2 - Aggregate Queries
 */

// Query A
// Viewing the existing students first provides a baseline before the
// collection is changed by the insert, update, and delete operations.
db.students.find({});

// Query B
// The new document uses the same four fields as the existing student
// documents so it follows the collection's established structure.
// A new studentId is used because it uniquely identifies this student.
db.students.insertOne({
  firstName: "Leslie",
  lastName: "Espino",
  studentId: "s1019",
  houseId: "h1009",
});

// Searching by the unique studentId confirms that the correct document
// was added without returning unrelated student records.
db.students.findOne({ studentId: "s1019" });

// Query C
// $set is used because only the student's house needs to change.
// This preserves the student's name and ID instead of replacing the
// entire document.
db.students.updateOne({ studentId: "s1019" }, { $set: { houseId: "h1007" } });

// Using the same studentId verifies that the intended document now
// contains the new houseId.
db.students.findOne({ studentId: "s1019" });

// Query D
// The studentId targets only the student created for this assignment,
// preventing another student with a similar name from being deleted.
db.students.deleteOne({ studentId: "s1019" });

// Returning null confirms that no document with this studentId remains
// after the delete operation.
db.students.findOne({ studentId: "s1019" });

// Query E
// Houses and students are stored separately but share houseId.
// $lookup uses that shared value to group each house with its students
// without permanently duplicating student data inside the house documents.
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students",
    },
  },
]);

// Query F
// Gryffindor is filtered before the collections are joined so MongoDB
// only performs the lookup for the house needed in this query.
db.houses.aggregate([
  {
    $match: {
      houseId: "h1007",
    },
  },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students",
    },
  },
]);

// Query G
// The house is filtered by mascot because the question identifies it
// by "Eagle" rather than by its houseId or founder.
db.houses.aggregate([
  {
    $match: {
      mascot: "Eagle",
    },
  },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students",
    },
  },
]);
