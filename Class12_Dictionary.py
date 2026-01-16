"""
# Dictionary in python
# What is a Dictionary in python?
A dictionary in python is a data type to store data key- value pairs
Key - must be unique and immutable
Value - can be any datatype (int, str, list, float, etc)
dictionary are unordered but insertion order is preserved in modern python


dictionary syntax:

dict_name = {
    "name" : "Esudass",
    "age" : 22, 
    "class" : "Bsc"
}

# Dictionary
Student = {
    "Name" : "Esudass",
    "Age" : 22,
    "class" : "Bsc"
}

# Accessing Dictionary
# use the dictionary name to access the full dictionary
print(Student)

# Accessing Dictionary Values
# use the dictionry key to access the pair of value
# not found the key - Error
print(Student["Name"])
print(Student["class"])
print(Student["Age"])

# Using get() (safer methode):
# not found the value - no Error
print(Student.get("Name"))
print(Student.get("sub"))

# Dictionary
Student = {
    "Name" : "Esudass",
    "Age" : 22,
    "class" : "Bsc"
}

# Chenging Value
Student["Age"] = 21
print(Student["Age"])

# Adding new Key - Value 
Student["city"] = "Coimbatore"
print(Student)

# Removing Element
Student.pop("Age")
del Student["class"]
print(Student)

# looping through a dictionary
Student = {
    "name" : "Esudass",
    "age" : 21,
    "class" : "Bsc",
}

for key, value in Student.items():
    print(f"{key} : {value}")

# nested dictionary
employee = {
    "name": "Esudass",
    "id" : 101,
    "skills" : {
        "language" : {
            "lang1": "python",
            "lang2": "java",
            "lang3": "javascript"
        },
        "level" : "intermediate",
        "exp" : "0 to 1 years"
    }
}

print(employee["skills"])
print(employee["skills"]["language"])
print(employee["skills"]["language"]["lang2"])

for key, value in employee.items():
    print(f"{key} : {value}")

for key, value in employee["skills"].items():
    print(f"{key} : {value}")

for key, value in employee["skills"]["language"].items():
    print(f"{key} : {value}")

marks = {
    "maths": 90,
    "science": 85,
    "english": 88
}

total = 0

for mark in marks.values():
    total += mark

print(total)

keys = ("name", "age", "city")
new_dict = dict.fromkeys(keys, "Unknown")
print(new_dict)


"""