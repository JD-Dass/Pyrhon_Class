# Input & Output

# input

# Input Syntax:
# variable_name = input("Enter Address: ")
# if you get the input data from user , the data is defalt string

name = input("Enter your name: ")
print("Hello! ",name)

# integer input
age = int(input("Enter your age: "))
print(age)
print(type(age))

# Float input
balance = float(input("Enter Elakiya bank balance: "))
print(balance)
print(type(balance))

# multiple input
name = input("What is your name? ")
age = int(input("What is your age? "))
Phone = int(input("Enter your Number: "))
bf_name = input("Enter your alagu boy name: ")

print("Hello! ",name, ".are you ",age," years old!",bf_name," soo cute! your number is ",Phone)
print(f"Hello! {name} . Are you {age} years old, {bf_name} is soo cute boy , your number is {Phone}")

# multiple inputs in sigle line
a,b,c = input("Enter your number: ").split("-")
print(a)
print(b)
print(c)

# Output

# syntax
# print(Value)

print("hello world")

name = "esu"
age = 21
price = 99.44444444444
print(f"Price: {price:.4f}")
print("Hello! ",name)
print("Hello! "+name)
print(12, 232, 34 ,sep="+")
print(f"Hello! {name} your age is {age}")