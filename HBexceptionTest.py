# -------------------------------------------------------------------------------------- #
# Title: exception testing
# Desc: Shows code to include for exceptions
# Change Log: (Who, When, What)
#   H.Breslauer, 11,08/2026. Start a file , copy from class notes-------------- #
#from mod05 notes page 20
# try:
#     value1: float = 3.0
#     value2: float = 0.0
#     print(value1 / value2)
# except Exception as e:
#     print("Error! Please check you are not dividing by zero.\n")
#     print("-- Technical Error Message -- ")
#     print(e) # Print the exception object (typically includes the error message)
#     print(type(e)) # Print the type of the exception object
#     print(e.__doc__) # Print the documentation string of the exception type
#     print(e.__str__()) # Print the string representation of the exception
 # mix up variable types
try:
    value1: float = 3.0
    value2: str = "Help"
    print(value1 / value2)
except Exception as e:
    print("Error! Please check you are have mismatched data types.\n")
    print("-- Technical Error Message -- ")
    print(e)  # Print the exception object (typically includes the error message)
    print(type(e))  # Print the type of the exception object
    print(e.__doc__)  # Print the documentation string of the exception type
    print(e.__str__())  # Print the string representation of the exception
# do some data validation



