"""
Author: Leslie Espino
Date: July 5, 2026
File Name: leslieEspino_lemonadeStandSchedule.py
Description: This program demonstrates the use of Python conditionals, lists, and loops by creating a weekly schedule for a lemonade stand.
"""

# Store the tasks that need to be completed to operate the lemonade stand.
tasks = [
    "Buy lemons",
    "Make lemonade",
    "Set up the stand",
    "Serve customers",
    "Count earnings"
]

# Display each task by looping through the list one item at a time.
print("Lemonade Stand Tasks:")

for task in tasks:
    print(task)

# Create a list containing every day of the week for the schedule.
days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

print("\nWeekly Schedule:")

# Keep track of which task should be assigned to each weekday.
taskIndex = 0

# Check each day of the week and determine whether it is a workday or a rest day.
for day in days:

    if day == "Saturday" or day == "Sunday":
        print(day + ": Rest day! Enjoy your weekend.")
    else:
        print(day + ": " + tasks[taskIndex])
        taskIndex += 1