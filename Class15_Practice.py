"""
# Revition and Practice:

# Class 1 - Variables:
# Store and print the Name, age, city variables
name = "Esudass"
age = 21
city = "coimbatore"
print(name)
print(age)
print(city)

# Create and Sum tow numbers
num1 = 10
num2 = 20
print(num1 + num2)

# a = 10, b = 20 → swap the value (use temporary variables)
a = 10
b = 20
a,b = b, a
print(a, b)



# Class 2 - Data Types
# Create Example int, float, string, boolean
integer = 10
float = 10.5
str = "dass" 
boolean = True 

# Print the datatype using type() function
print(type(integer))
print(type(float))
print(type(str))
print(type(boolean))

# get the input from the user and then print the datatype
a = input("Enter input: ")
print(type(a))


# Class 3 – Input & Output
# get the user name from the user and peint "Hello, <name>"
name = input("Enter your name: ")
print(f"Hello, {name}")

# get two numbers from the user and the print sum and difference
num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
sum = num1 + num2
difference = num1 - num2
print(f"sum: {sum}\ndifference: {difference}")


# Class 4 – Type Casting
# convert string "100" into int 100
num = "100"
num = int(num)
print(num)
print(type(num))

# convert float into int
a = 100.232
a = int(a)
print(a)

# get number from user and then multiply
num1 = float(input("Enter the number: "))
num1 *= num1
print(num1)


# Class 5 – Operators
# create calculater using arithmatic operators
num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
print(f"{num1 + num2}")
print(f"{num1 - num2}")
print(f"{num1 * num2}")
print(f"{num1 / num2}")
print(f"{num1 % num2}")
print(f"{num1 ** num2}")
print(f"{num1 // num2}")

# odd/even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an Even number")
else:
    print(num, "is an Odd number")

# get two numbers and compare print greater number
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a > b:
    print(a)
else:
    print(b)


# Class 6 - Conditional Statements
# Number positive / negative / zero check
a = int(input("enter number: "))
if a > 0:
    print("positive")
elif a < 0:
    print("negative")
else:
    print("zero")

# Marks input → grade print (A, B, C, Fail)
mark = int(input("Enter a mark: "))
if mark <= 90:
    print("grade A")
elif mark <= 80:
    print("grade B")
elif mark <= 60:
    print("grade C")
else:
    print("File")

# Divisible by 3 & 5 check
a = int(input("Enter a number: "))
if a % 3 == 0:
    print("Divisible by 3")
elif a % 5 == 0:
    print("Divisible by 5")
else:
    print("not Divisible")

# Nested if use panni biggest of 3 numbers
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a > b:
    if a > c:
        print("A is a big number")
    else:
        print("C is a big number")
else:
    if b > c:
        print("B is a big number")
    else:
        print("C is a big number")


# Class 7 - Mini Programs
# Simple calculator (add, sub, mul, div)
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print('''
      addition    => "+"
      subtraction => "-"
      multiply    => "*"
      divid       => "/"
      ''')
choice = input("chose the operator(Symbole only): ")
if choice == "+":
    print(a + b)
elif choice == "-":
    print(a - b)
elif choice == "*":
    print(a * b)
elif choice == "/":
    print(a / b)
else:
    print("invalid input")

# Vowel or consonant check
a = input("Enter a Letter: ")

if a in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    print(f"{a} is Vowel")
else:
    print(f"{a} in consonant")


# Class 8 - Loops
# Print 1 to 10
for x in range(1, 11):
    print(x)

a = 1
while a <= 10:
    print(a)
    a += 1

# Print 10 to 1
for x in range(10, 0, -1):
    print(x)

a = 10
while a >= 1:
    print(a)
    a -= 1

# Even numbers from 1 to 50
for x in range(0, 51, 2):
    print(x)

for x in range(50, 0, -2):
    print(x)

# polindrom check
num = int(input("Enter number: "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")


# Class 9 - String
# find string length
string = "Hello"
print(len(string))

# reverse the string
string = "Hello"
string = string[::-1]
print(string)

text = "hello"
rev = ""
for ch in text:
    rev = ch + rev
print(rev)

# count vowels
text = input("Enter text: ")
vowels = "aeiouAEIOU"
total = 0
for ch in text:
    if ch in vowels:
        total += 1
print(total)

# polindrom
text = input("Enter text: ").lower().strip()
sample = text
rev = text[::-1]
if sample == rev:
    print("polindrom")
else:
    print("not polindrom")


# Class 10 -list
# create 5 number list
number = [1, 2, 3, 4, 5]

# find large and smallest number
number = [1, 2, 3, 4, 5]
print(max(number))
print(min(number))

# sum and avarage
number = [1, 2, 3, 4, 5]
sum = sum(number)
avarage = sum / len(number)
print(sum)
print(avarage)
    
# remove duplicats
nums = [11,22,33,44,5,56,33,44,22,11,88]
result = []
for num in nums:
    if num not in result:
        result.append(num)
print(result)

# reversed list
num = [1, 2, 3, 4, 5, 6]
num = num[::-1]
print(num)

num = [1, 2, 3, 4, 5, 6]
num.reverse()
print(num)

num = [1, 2, 3 , 4, 5, 6]
result =[]
for i in range(len(num)-1, -1, -1):
    result.append(num[i])
print(result)


# Class 11 -Tuple and sets
# create tuple and access the element
num = (1, 2, 3, 4, 5, 6)
print(num[1])

# use count and index for tuple
num = (1, 2, 2, 3, 4, 5, 5, 6, 7, 6)
print(num.count(5))
print(num.index(4))

# set
# crete set
num = {1, 2, 3, 4,5, 5, 5, 6, 7, 8,8 ,8 }
print(num)

a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a | b)
print(a & b)
print(a ^ b)

"""

