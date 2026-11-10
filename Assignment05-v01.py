# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   HeidiBreslauer, 11/08/2026
# ------------------------------------------------------------------------------------------ #

#  Import the json module
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data as dictionary
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
# HB add structured error handling for file open,
try:
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        # Transform the data from the file
        student_data = row.split(',')
        student_data = {"FirstName": student_data[0], \
                        "LastName": student_data[1], "CourseName": student_data[2].strip()}
        # Load it into our collection (list of lists)
        students.append(student_data)
    # print(students)
except FileNotFoundError as e:
    print("No file found.")
    print("--Technical Error Message--")
    print(e, e.__doc__, type(e), sep='\n')

# Check if a file object exists and is still open
if file is not None and file.closed == False:
    file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data and check that name does not incule numbers
    if menu_choice == "1":  # This will not work if it is an integer!
        while True:
            try:
                student_first_name = input("Enter the student's first name: ")
                if not student_first_name.isalpha():
                    raise ValueError("The first name should not contain numbers.")
                break
            except ValueError as e:
                print(e)
                print("--Technical Error Message --")
                print(e.__doc__)
                print(e.__str__())

            # except Exception as e:
            # print(e)
            # print("There was an error.")
        while True:
            try:
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError("The last name should not contain numbers.")
                break
            except ValueError as e:
                print(e)
                print("--Technical Error Message --")
                print(e.__doc__)
                print(e.__str__())

        course_name = input("Please enter the name of the course: ")

        # HB: structured error handling
# Version .1 working to here
        print(student_first_name, student_last_name,course_name)
        student_data = {"FirstName": student_data[0], \
                        "LastName": student_data[1], "CourseName": student_data[2].strip()}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} "
              f"for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        # HB:structured error handling here
        file = open(FILE_NAME, "w")
        for student in students:
            file.write(f"{student[0]},{student[1]},{student[2]}\n")

        # Check if a file object exists and is still open
        if file is not None and file.closed == False:
            file.close()

        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

    # HB : Do we want a finally clean up here?

print("Program Ended")
