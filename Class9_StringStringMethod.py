# String and String Method
"""
string means letters , words, sentence and all text format to store in data type.
strings between quotes in python
# single quote ' '
# Double quote " "
# Triple Quote ''' '''/ """ """(multi line ku use pannauvaga
)

name = "python"
name1 = 'Python'

# string length
text = "Python"
print(len(text))  

# String Indexing
# string indexing start with 0 in python
great = "Python"
print(great[0])
print(great[1])
print(great[2])
print(great[3])
print(great[4])
print(great[5])

# string Slicing
name = "python"
print(name[0:7])
print(name[0:6])
print(name[0:5])
print(name[1:7])
print(name[2:7])
print(name[3:7])
print(name[2:])
print(name[:5])

# format:
# string[start: end]

# Strings are immutable
# strings la iruka character direct ta change panna mudiyadhu 
# example:
word = "pyhton"
# wors[0] = "j"  #error
word = "j" + word[1:]
print(word)

# String methods
# String methods are built in functions in python that help you modify, check or work with text(string) easily
# syntax:
# string_name.method()

# Most important string methods

# upper() => convert all characters to UPPERCASE.
# Example:
text = "pyhton"
text = text.upper()
print(text)

# lower() => convert all character to lowercase
# Example:
text = "PYTHON"
text = text.lower()
print(text)

# capitalize() => Makes only the first letter uppercase.
# example:
text = "i am a python developer"
text = text.capitalize()
print(text)

# title() => makes first letter of each word uppercase
# Example
text = "Python is easy"
text = text.title()
print(text)

# strip() => Removes extra spaces from the beginning and end
# example:
text = " Hai  "
text = text.strip()
print(text)
# lstrip() => remove left spaces
# rstrip() => remove right spaces

# replace(old, new) => replace one word or character eith another
# example
text = "i am a python developer"
text = text.replace("python", "java")
print(text)

# split() => splits a string into a list.
# example:
text = "Python in powerfull"
text = text.split()
print(text)

# join() => join elements of a list into single string.
# example:
text = ["python", "is", "powerfull"]
text = " ".join(text)
print(text)

# find() => returns the index position of a character or word
# example:
text = "python is very powerfull"
text = text.find("z")
print(text)
# if not found => returns -1

# count() => counts how many times a character or words appears.
# example:
text = "pyhton is powerfull"
counts = text.count("a")
print(counts)

# startswith() => Checks if the string starts with a specific value.
# example:
text = "python"
starts = text.startswith("p")
print(starts)  #True
starts = text.startswith("e")
print(starts)   #Fauls

# endswith() => chacks if the string ends with a specific value.
# example:
text = "python"
ends = text.endswith("p")
print(ends)  #Fauls
ends = text.endswith("n")
print(ends)   #True

# isdigit() => check if the string contain only numbers.
# example
text = "12345"
digit = text.isdigit()
print(digit)

# isalpha() => checks if the string containe only letters
# example.
text = "python"
alpha = text.isalpha()
print(alpha)

# isalnum() => check if the string contains letters and numbers
# example:
text = "123wewew"
alnum = text.isalnum()
print(alnum)








"""










