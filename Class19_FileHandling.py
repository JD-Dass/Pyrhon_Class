"""
# File handling
# what is file handling? 
file handling in python means working with files - reading data from a file or writing data into a file
# in this class, focus only on reading a file.

# why do we need to read a file?
we read file to:
get stord data (text, logs, data records)
avoid entring data again and again
work with lorge data efficiently
Example use cases:
reading student details from a file
reading configuration settings
reading notes or content from a .txt file

# steps to read a file in python
open a file 
read a file
close a file

# opening a file (read mode)
file = open("data.txt", "r")
"data,txt" => file name
"r" => read mode
# if the file does not exist, python will give an error.

# methods to read a file
# read() - read entire file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
# read() reads all content at once
# useful fro small files

# read(n - read specific character
file = open("data.txt", "r")
content = file.read(10)
print(content)
file.close()
# read only first 10 characters
# healps when you want limited data

# readline() - read one line
file = open("data.txt", "r")
content = file.readline()
print(content)
file.close()
# reads one line at a time
# cursore moves to next line after reading

# readlines() - read all lines as list
file = open("data.txt", "r")
content = file.readlines()
print(content)
file.close()
# each line becomes an element in a list
# useful for looping line by line

# reading file using for loop
file = open("data.txt" , "r")
for line in file:
    print(line)
file.close()

# Using with statement 
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# Why use with? 
# no need to close the file manually
# safer and cleaner code

"""


"""
# Write and append
Why write and append files?
we use write and append to:
=> save program output permanatly
=> store user input
=> maintain logs
=> update file without database

# file models used
=> W - write(xreate new file or overwrite existing file)
=> a - append ( adds data at the end of file)
=> r+ - read + write

# Write mode ("w")
whate does write mode do? 
=> Create new file the file does not exist
=> Delete old content if file already exists

# Example: write to a file
file = open("data.txt", "w")
file.write("hello data file \n")
file.write("i am python in file handling class")
file.close()
# write() → writes text to file
# \n → moves to next line
# Old data will be erased

# Append Mode ("a")
What does Append Mode do?
# Adds content at the end
# Old content remains safe

# example
file = open("data.txt", "a")
file.write("\nThis line is appended")
file.close()
# Cursor moves to end of file
# New data is added after existing data

# write multiple lins
lines = [
    "Python\n",
    "Java\n",
    "JavaScript\n"
]
file = open("languages.txt", "w")
file.writelines(lines)
file.close()
# Writes list of strings
# Must include \n manually

# Read + Write Mode ("r+")
with open("data.txt", "r+") as file:
    print(file.read())
    file.write("\nNew data added")
# Cursor starts at beginning
# Writing happens after reading

"""