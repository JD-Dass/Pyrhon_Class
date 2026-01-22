"""
# Exception handling in python 
# whate is exception?
An exception is an error that occurs during program execution, which stop the normal flow of the program
# example
a = 10
b = 0
print(a/b)
# ZeroDivisionError: division by zero

# why exception handling is important?
it prevent for a program crash
Run the program smoothly when error occurs
it hepls send a user friendly messages

# Types of errors:
=> Syntax Error - Code wrong formate
=> Runtime error - if you run the program teh errors occur
=> Logic Error - Output wrong but no error

# common built in exceptions:
=> ZeroDivisionError
=> ValueError
=> TypeError
=> IndexError
=> KeyError
=> FileNotFoundError
=> AttributeError
=> importError / ModuleNotFoundError
=> OverflowError

"""


"""
# try - except 
what is try-except?
#try-except block is used to runtime errors (exceptions) so that the program does not crash.
=> risky code inside the try block
=> errors inside the except block

# basic syntax:
try:
    risky Code 
except:
    runs if error occurs

# simple Example:
try:
    a = int(input("Enter a number: "))
    print(10 / a)
except:
    print("Some error occurred")

# Catching Specific Exceptions
try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter numbers only")

# Using Exception as e
try:
    x = int("abc")
except Exception as e:
    print("Error:", e)

# try - except - else
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Division by zero not allowed")
except ValueError:
    print("Invalid input")
else:
    print("No error, program success")

# try - except - finally
"""




