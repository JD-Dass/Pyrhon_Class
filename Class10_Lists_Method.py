"""
Lists and lists methods


What is a list?
A list in python is a colloction used to store multiple values in a single variables

list are:
# Ordered (items have a fixed position)
# Changeable (mutable)
# Allow Duplicate values

How to create list?
number = [1, 2, 3, 4, 5 ,6 ]
string = ["esu", "dass", "ram", "som"]
mixed = [1, 1.4, "python", True]

# Accessing list items (indexing)
names = ["esu","dass","ganesh","elakiya"]
access = names[2]
print(access)

# change the list values
names = ["esu","dass","ganesh","elakiya"]
names[2] = "JD"
print(names)

# List methods
# in python , list methods are builed in functions used to add, remove, modify and manage elaments in a list

# append()
# add element to the end of the list
names = ["esu","dass","ganesh","elakiya"]
names.append("Jd")
print(names)

# insert()
# add element at a specific position
names = ["esu","dass","ganesh","elakiya"]
names.insert(1, "JD")
print(names)

# remove()
# remove the first occurrene of a specified value
names = ["esu","dass","ganesh","elakiya"]
names.remove("dass")
print(names)

# pop()
# remove and returnan element by index
# default removes the last element
names = ["esu","dass","ganesh","elakiya"]
names.pop()
print(names)
names.pop(0)
print(names)

# clear()
# remove all elements from the list
names = ["esu","dass","ganesh","elakiya"]
names.clear()
print(names)

# index()
# returns the index of the first occurrence of a value
names = ["esu","dass","ganesh","elakiya"]
index = names.index("dass")
print(index)

# count()
# counts how many times a value appears in the list
num = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 7, 7]
count = num.count(3)
print(count)

# sort()
# sort the list in ascending order
num = [12,4,6,77,7,34,343,545,56,5,76,86]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

# reverse()
# revers the order of the elements
num = [1,2,3]
num.reverse()
print(num)

# copy()
# create the copy of the list
num1 = [1,2,3]
num2 = num1.copy()
print(num2)
num2.append(4)
print(num2)

# extend()
# adds all elements of another list
num1 = [1,2,3,4]
num2 = [5,6,7,8]
num1.extend(num2)
print(num1)

"""
