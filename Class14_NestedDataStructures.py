"""
# Nested data structure

Nested data stuctures in Python means one data structure stored inside 
another data structures.
# in simple words:
=> A list inside a list
=> A dictionary inside a dictionary
=> A list inside a dictionary or vice- vetsa

# Nested list
number = [
    [1,1,1,1,1],
    [2,2,2,2,2],
    [3,3,3,3,3],
    [
        [11,11,11,11],
        [22,22,22,22],
        [33,33,33,33],
        [
            [111,111,111],
            [222,222,222],
            [333,333,333]
        ]
    ]
]

print(number)   #all values
print(number[1])   # 2,2,2,2,2
print(number[3][1])   # 22,22,22,22
print(number[3][3][1])   # 222,222,222
print(number[3][3][1][1])   # 222
# => first index selects the inner list
# =>Second index selects the value inside that lits

# Nested dictionary
# => A nested dict is a dict that contains another dict as a value
student = {
    "name":"esudass",
    "age":21,
    "address": {
        "city": "coimbatore",
        "state": "Tamilnaadu"
    }
}
print(student)          #all keys and values
print(student["address"])    #address key in values
print(student["address"]["city"])    #coimbatore

#List inside a Dictionary
# =>This structure is very common in real-world programs.
employee = {
    "name": "Alice",
    "skills": ["Python", "HTML", "CSS"],
    "experience": 3
}
print(employee["skills"])      # ['Python', 'HTML', 'CSS']
print(employee["skills"][1])   # HTML

# Dictionary inside a List
# =>A list can store multiple dictionaries.
students = [
    {"name": "Sam", "age": 21},
    {"name": "Raj", "age": 22}
]
print(students[0]["name"])  # Sam
print(students[1]["age"])   # 22

# Complex Nested Structure
# =>This type of structure is commonly used in JSON and API data.
company = {
    "name": "TechSoft",
    "employees": [
        {
            "name": "Kumar",
            "skills": ["Python", "Django"]
        },
        {
            "name": "Priya",
            "skills": ["JavaScript", "React"]
        }
    ]
}
print(company["employees"][1]["skills"][0])  # JavaScript

"""
