"""
Condition statements (python)

Why we need conditional statements?
=> to make decision in program
=> to handle different situations
=> to control the flow of execution

1. if statement
2. if - else statement
3. if - elif - else statement
4. Nested if

if statement syntax:
if condition:
    # code block 

# Example
mark = int(input("Enter your mark: "))

if mark >= 50:
    print("pass")

num = int(input("Enter number: "))
if num % 5 == 0:
    print("Divisible by 5")

# id eles:

Syntax:

if condition:
    code if true
else:
    code if false

# Example
# eligible for vot
age = int(input("Enter a age: "))
if age >= 18:
    print("your aligible to vote")
else:
    print("Your not eligible to vote")

# divisible by 5
number = int(input("Enter a number: "))
if number % 5 == 0:
    print("Divisible by 5")
else:
    print("not Divisible by 5")

# positive or negative
number = int(input("Enter a number: "))
if number > 0:
    print("positive number")
else:
    print("negative or zero")

# Odd or Even
num = int(input("enter the number: "))
if num % 2 == 0:
    print("Even")
else:
    print("odd")


# if elif else
syntax

if condition:
    code
elif condition:
    code
elif condition:
    code
else:
    code

# grading system
mark = int(input("Enter mark: "))
if mark >= 90:
    print("A grade")
elif mark >= 80:
    print("B grade")
elif mark >= 70:
    print("C grade")
else:
    print("fail")

# positive and negative and zero
num = float(input("Enter a number: "))
if num > 0:
    print("positive")
elif num == 0:
    print("zero")
else:
    print("nagative")

# Nested if

syntax

if condition:
    if condition:
        if condition:
             code
        else:
            code
    else:
        code
else:
    code
"""

# Age + id check
age =int(input("enter age: "))
has_id = input("doyou have id? (y/n): ")

if age >= 18:
    if has_id == "y":
        print("Entry allowed")
    else:
        print("entry not allowed")
else:
    print("Under age")




