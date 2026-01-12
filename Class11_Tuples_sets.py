"""
# Tuples in python
# What is Tuple?
Tuple is a collection of data types in python that is:
Ordered (items have fixed positions)
immuteble (cannot be changed after created)
allows duplicate values
can store multiple data types
# tuple looks similar to a list, but is uses round brackets () inside of square brackets []

# example:
tuples = (10, 20, 30)
print(tuples)

# Accessing tuple values
names = ("esu", "dass")
print(names[1])

# tuple with different datatypes 
datas = (12, "esu", 12.34,True)
print(datas)

# Tuple is immutable (very important)
# you cannot change a tuple item
nums = (2, 3, 4,5)
nums[2] = 5    #Error
# This will give TypeError, because tuple is immutable.

# Tuple with single Element (important Syntax)
a = (10)   # not a tuple (int)
b = (10,)  #tuple

# Tuple Unpacking
person = ("Esudass", 22, "Coimbatore")
name, age, place = person
print(name)
print(age)
print(place)

"""

"""
# Sets
# What is a set?
A set is a collection data type in python that is:
Unordered
muteble
no duplicates, only unique values
Writtern using curly braces{}

# Example
my_set = {10, 20, 30, 40}
print(my_set)
# order may change every time you print(because set is unordered)

# duplicate values automatically removed 
nums = {1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8}
print(nums)

# Accessing set element
# you cannot use index in sets
# youe can use loop:
colors = {"red", "green", "blue", "yellow"}
for c in colors:
    print(c)

# Adding element to set
s = {1, 2, 3}
s.add(4)
print(s)

# add multiple values
# update([])
s = {1,2,3,4}
s.update([5,6,7,8,9])
print(s)

# remove Element
s = {1, 2, 3, 4}
s.remove(2)       #remove specified value only
print(s)
s.discard(5)         # incase not found specified value when no erroe
print(s)
s.pop()           #remove random number
print(s)
s.clear()         # clear all values
print(s)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1,2,3,4,5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1,2}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

c = {} #dictionary
d = set() #empty set

"""