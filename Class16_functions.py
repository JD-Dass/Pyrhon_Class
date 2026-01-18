"""
# Funcrions in python
What is a Function?
Function is a block of code that runs only when we call it.
=> avoide repeaded code
=> Code neat & resuable 


# function syntax:
def func_name():
    # code block
    pass

# for Example => function without arguments:
def greet():
    print("Hello world")
# call the function
greet()

# function with arguments
def greet(name):
    print(f"Hello, {name}")
# call the function
greet("Esudess")

# Function With Multiple Arguments
def add(a, b):
    print(a + b)
# call the function
add(10, 20)

# Function With Return Statement
# return the value outside of the function
def square(num):
    return num *num
# result = square(5)
# print(result)

# Function With Default Arguments
def greet(name = "Guest"):
    print(f"Hello, {name}")
greet()
greet("Esu")

# Keyword Arguments
# order is not important
def details(name, age):
    print(name, age)
details(age = 22, name = "Esudass")

# Arbitrary Arguments (*args)
# pass multiple arguments
def total(*nums):
    print(sum(nums))
total(10, 10, 10, 20, 30, 40)

# Keyword Arbitrary Arguments (**kwargs)
# pass multiple key word with values arguments (like dictionary)
def data(**data):
    print(data)
data(name = "dass", age = 21, city = "coimbatore")

# Lambda Function (Short Function)
# one line function
add = lambda a, b: a+b
print(add(10, 30))

# Function Inside Function (Nested Function)
def outer():
    print("i am outer function , i will bw call inner function")
    def inner():
        print("i am inner function")
    inner()
outer()

"""