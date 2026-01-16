"""
# Type convertion in python

Typr convertion means changeing the value one data type to another.
In python, this is uesful when you want to perform operations on different type of data

There are two types of type convertion in python:
1. Implicit Type Convertion (Automatic)
2. Explicit Type Convertion (Type casting)


1. Implicit Type Convertion (Automatic)
Implicit Type Convertion means Python Automatically convert one datatype into another,
without the programer writing any convertion code.

This happens internally when Python feels convertion is needed to avoid data loss.

# key points:
=> Done automatically by python 
=> Programmer does not write any convertion code
=> Uesally happens between int, float, and complex
=> Safer datatype is chosen

# Example 1: int to float
a = 10          #int
b = 10.5        #float
c = a + b
print(c)
print(type(c))  #float
# Python converts int into float and then adds

# Example 2: int to complex
a = 5       #int
b = 2 + 3j  #complex
c = a + b
print(c)
print(type(c))
Python converts int into complex automatically

# Example 3: int + str (Error)
a  = 5  #int 
b = "esu" # string
c = a + b
print(c) 
#TypeError: unsupported operand type(s)
# Python cannot implicitly convert string to number

# Convertion order priority
int => float => complex
# Python converts lower priority type to higher priority type

# Why python use implicit convertion?
=>prevents data loss
=>Keeps calculation accurate
=>Macks code similar

# important notes :
=>string never implicit convertion
=>Implicit convertion happens only for compatible types
=>Mostly used in arithmatic operations

""" 

"""
# Explicit Type convertion (Type casting)
Explicit type convertion also calling type casting means
Programmer manually converts one data type into another using built-in function
Python will not convert automatically here - we must tell python what to do.

# key points
=> Done manually by the progammer
=> Uses build in functions
=> Needed when working with user input
=> Helps avoid TypeError

# commen type casting functions
=> int()   integer
=> float() float
=> str()   sting
=> bool()  boolean
=> complex() complex number

# int() - convert to integer
strnum = "10"      #string
num = int(strnum)  #int
print(num)
print(type(num))

a = "10.5"
b = float(a)
print(b)
print(type(b))

num = 100
text = str(num)
print(text)
print(type(text))

print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("Hi"))   # True

x = 5
y = complex(x)
print(y)
print(type(y))

# real time example
age = input("Enter your age: ")
age = int(age)
print("Next year age:", age + 1)

"""