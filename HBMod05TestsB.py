# ------------------------------------------------------------------------------------------ #
# Title: HBMod05Tests from Working With Dictionaries And Files
# Desc: Shows how work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
#   H.Breslauer, 11,07/2026. Start a file from scratch
# ------------------------------------------------------------------------------------------ #
# Define variables and CONSTANTS
student_first_name: str = ""  # Holds the first name of a student read from file
student_last_name: str = ""  # Holds the last name of a student read from file
course_name: str ="" # Holds the course name read from file
student_gpa: float = 0.0  # Holds the GPA of a student read from file.
# student_paid: bool = ""Bool not declared!
student_bday: str="" # Holds the students birthday read from file

message: str = ''  # Holds a custom message string
menu_choice: str = ''   # Hold the choice made by the user.
student: dict = {}  # one row of student data
students: list = []  # a table of student data
fileorig_data: str = ''  # Holds combined string data separated by a comma.
file1 = None  # Not using type hint helps PyCharm, so we won't use it going forward

FILE_NAME: str = "studentsTest1.csv"
#  Read in test data from csv
# student_paid: bool = True
# print(type(student_paid))

# Read in a giant string from CSV file
file1=open(FILE_NAME, "r")
fileorig_data = file1.read()
file1.close()
print(len(fileorig_data))
print("data from file")
print(fileorig_data)

# # read using readline, need to do this for every line in the file.
# file1datareadline=""
# file1=open(FILE_NAME, "r")
#
# file1datareadline=file1.readline()
# print(len(file1datareadline))
# file1datareadline+= file1.readline()
# print(len(file1datareadline))
# file1.close()
file = open(FILE_NAME, "r")
# for row in file.readlines():
#     # Transform the data from the file
#     student = row.split(',')
#     student = {"FirstName": student[0],
#                     "LastName": student[1],
#                     "GPA": float(student[2].strip())}
#     # Load it into our collection (list of lists)
#     students.append(student)
# file.close()
# Reads all rows in file with file.readlines()

# """
# file1=open(FILE_NAME, "r")
# # file1datareadlines=file1.readlines()
# for row in file1.readlines():
#     #Transform the data from file
#     student= row.split(",")
#     student={"FirstName":student[0],
#           "LastName":student[1],
#              "CourseName":student[2],
#              "GPA":float(student[3]),
#              "StudentPaid":student[4],
#              "Birthday":student[5].strip()
#              }
# """


   # student=[student[0],student[1],student[2], float(student[3]),student[4],student[5]].strip()]
    students=append.(student)
file1.close()
print(file1datareadlines)
print(len(file1datareadlines))

#





#tell me it's finished
print("All Done")


