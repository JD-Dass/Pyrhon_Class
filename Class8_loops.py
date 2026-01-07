# loops

"""
in this Python loops topics

=> for loop
=> while loop
=> Nested Loop
=> Break
=> Continue
=> Pass
=> Else

# for loops
# syntax
for variable in sequence:
     code block

# Range

for i in range(5):
    print(i +1)

# start to end
for i in range(2, 9):
    print(i)

# step value
for i in range(1, 10, 2):
    print(i)

# for loop with list
names = ["esu", "dass", "nelson", "joseph"]
for name in names:
    print(name)

# str with for loop
word = "python"
for letter in word:
    print(letter)

for i in "python":
    print(i)

# for + if
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

for i in range(11):
    if i == 5:
        break
    print(i)

for i in range(11):
    if i % 3 == 0:
        continue
    print(i)

for i in range(11):
    if i % 3 == 0:
        print(i)

# nested for loop
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)

# for + else 
for i in range(3):
    print(i)
else:
    print("loop completed")

# for loop is used to iterate over sequences like list, string, tuple and range in Python

for i in range(1, 11):
    print(i)

for i in range(1, 50):
    if i % 2 == 0:
        print(i)

names = ["name1", "name2", "name3", "name4", "name5"]
for name in names:
    print(name)

text = "Python"
for ch in text[::-1]:
    print(ch, end="")

for i in range (1, 11):
    print(f"{i} * 2 = {i*2}")

"""



"""
# While loop

# syntax

while condition:
    code block

# first print
i = 1

while i <= 5:
    print(i)
    i += 1

# even number
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# user input until correct password
password = "DASS"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")

print("Login Success")

# infinite loop
while True:
    print("Hello")

# breck
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)

# continue
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)

# reverse number using while
num = 24343
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(rev)

# while loop is used when the number of iteration is not known in advance and depends on a condition

# Input number use panni reverse pannu
num = int(input("Enter number: "))
rev = 0

while num > 0 :
    digit = num % 10
    rev = rev * 10 + digit 
    num //= 10

print(rev)

# polindrom check
num = int(input("Enter number: "))
original = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(f"Reversed number: {rev}")

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# negative revers
num = int(input("Enter number: "))
is_nagative = False
if num < 0:
    is_nagative = True
    num = -num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if is_nagative:
    rev = -rev

print(rev)

"""