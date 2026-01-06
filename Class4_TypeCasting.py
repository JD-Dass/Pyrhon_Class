# type cansting
# type casting means convert one data type into another data type 
# example: converting a string to an integere, an integer to a float, etc

# python support two type of type casting

# 1. implicit type casting (automatic)

# 2. explicit type casting (manual)



# Impicit Type casting(Automatic)

# python automatically converts one data type to anouther when needed

# for example
# a = 10.5
# b = 10.5

# c= a + b
# print(type(a))   # "a" is int
# print(type(b))   # "b" is float   int + float = float
# print(type(c))   # "c" is float   float + float = float

# explanation
# when an int and a float are added
# python automatically convert the int into a float
# the result will be a float

#  2. Explicit casting (manual)
# explicit type casting is done manually by the programmer using built in functions.

# common type casting functions:
# int(), float(), str(), bool()

# a = "10"
# b = "100"
# c = a + b
# print(type(a))
# print(type(b))
# print(type(c))
# print(c)
# print(type(c))
# c = int(a) + int(b)
# print(c)
# print(type(c))

# converts str "10" and str "100" to int "10" and "100"

# a = "100.100"
# print(type(a))
# b = float(a)
# print(b)
# print(type(b))

# a = "100"
# b = bool(a)
# print(b)

# age = int(input("Enter your age: "))
# print(f"your age after 10 years will be: {age + 10}")

# price = int(input("Enter the price: "))
# quantity = int(input("Enter the quantity: "))
# total = price * quantity
# print(f"total amount is: {total}")
