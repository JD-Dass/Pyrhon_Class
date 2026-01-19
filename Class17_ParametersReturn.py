"""
# Parameters & return in python
# What is a Function?
A function is a block of reusable code that performs a specific task

# Example:
def func_name():
    # block of code
    pass


# What are parameters?
# parameters are variables used in a function definition to receive values
# => They act like inputs to a function.
def greet(name):
    print("Hello", name)
greet("Esu")

# Types of Parameters
# signle parameters
def square(num):
    print(num * num)
square(5)

# Multiple Parameters
def add(a, b):
    print(a+b)
add(10, 20)

# Default Parameters
# A default value is used if no argument is passed.
def greet(name = "Guast"):
    print("Hello ",name )
greet()
greet("Esu")

# Keyword Parameaters
# Arguments are passed using parameters names
# order is does not mater
def details(name, age, city):
    print(name, age, city)
details(name = "Esudass", age = 21, city = "Coimbatore")

# Variable-length Parameters (*args)1
# Used when you don't know how many values will be passed.
def total(*numbers):
    print(sum(numbers))
total(12,12,12,12,12,23,23)

# Keyword Variable-length Parameters (**kwargs)
# Used to pass Key-Value Paire
def details(**data):
    print(data)
details(name="Esudass", age=21, city="Coimbatore")

"""



"""
# Return in Python
# What is python?
return is a keyword used inside a function to:
1. Send a value back to the function caller
2. Stop the function execution immediately
simple meaning:
return = give output + exit function

# basic example
def add(a, b):
    return a+b
result = add(10, 20)
print(result)

"""


"""
# *Args in python2 (simple and clear Explanation)
# What is *args?
*args is uesd in Python function to accept a variable number of positional arguments.
The word args stands for arguments, and the *(asterisk) allows the function to tack any number of values.

# Why do use *args?
Normally, a function has a fixed number of parameters.
# Example:
def add(a, b):
    return a+b
# this works only two arguments.
but, what if you want to pass 2, 3, 4,5 or more numbers?
That's where *args is use full

# How does *args works?
*args collected all extra positional arguments
It stors them as a tuple
# Example:
def num(*args):
    print(args)
num(12,12,12,12,21)
output: (12,12,12,12,21)
# Here *args is a tuple

# Example:
# Sum of multiple numbers
def sum_num(*nums):
    print(sum(nums))
sum_num(12,23,34,56,67,89)

# Example2:
# mixing normal parameters and *args
def student_info(name, *marks):
    print(f"Name: {name}")
    print(f"Marks: {marks}")
student_info("Esudass", 50, 60, 70, 80, 20)
# Normal parameters must come before *args

"""


"""
# **kwargs in python
# What is **kwargs?
**kwargs used in python function to accept a variable number of keyword variable arguments
kwargs stands for keywors arguments
the **(double asterisk) allows the function to receive arguments in te form of key = value
inside the function kwargs is stored as a dictionary

# why do we use **kwargs?
Normally, a function accepts a fixed number of keyword parameters.
but when you don't know how many named arguments will be passed, **kwargs is useful.


# how does **kwargs work?
# Example:
def student_details(**details):
    print(details)
student_details(name = "Esudass", id = 101, age = 21, department = "computer science", city = "coimbatore")
# output:
{'name': 'Esudass', 'id': 101, 'age': 21, 'department': 'computer science', 'city': 'coimbatore'}
here, **kwargs is a dictionary

# Example 1: 
# accessing value from **kwargs
def student_details(**details):
    for key, value in details.items():
        print(f"{key} : {value}")
student_details(name = "Esudass", id = 101, age = 21, department = "computer science", city = "coimbatore")
# output:
name : Esudass
id : 101
age : 21
department : computer science
city : coimbatore

# Example 2:
# Mixing normal parameters and **kwargs:
def student_details(id, **details):
    print("id :", id)
    print("details :", details)
student_details(name = "Esudass",id = 101, city = "coimbatore") #or
student_details(101, name = "Esudass",city = "coimbatore") 

# Example 3:
# Using *args and **kwargs together
def demo(a, b, *nums, **dataset):
    print("a : " ,a)
    print("b : " ,b)
    print("nums : " ,nums)
    print("dataset : " ,dataset)
demo(12, 23,34, 34, 34,34, data = 1, data1 = 1)
# output:
a :  12
b :  23
nums :  (34, 34, 34, 34)
dataset :  {'data': 1, 'data1': 1}

"""