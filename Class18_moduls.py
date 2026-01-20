"""
# Built in modules in python
built in modules are modules that come pre-installed with python.
you don't need to sownload or install them seperately. You can directly use them using the import keyword.
these modules helps you do common tasks like math oprrations , date and time handling , random numbers , system interaction , file handling , etc.

# Why built in modules are important? 
save time (no need to write everything from scrach)
reliable and optimized
used in real projects and interviews
help write clean and short code

How to use a built in module?
example:
import module_name

# Commonly used built in modules:
=> math module
=> random module
=> datetime module
=> time module
=> os module
=> sys module
=> calender module
=> statistics module
=> json module
=> re module

# math module
the math module is a built in python module used to perform mathematical operations
is provides ready made functions for square root, power, trigonometry, logarithms, constants, etc
# you don't neet to install anything just import math

how to use math module?
import math

# commonly used functions in math module
1. sqrt() => Square root
2. pow() => power
3. ceil() => round up
4. floor() => round down
5. fabs() => Absolute value
6. factorial() => factorial
7. trignometric functions
=> sin()
=> cos()
=> tan
8. logarithmic function
=> log()
=> log10()
9. constants in math module
=> math.pi
=> math.e

real world use of math modules
=>calculator
=>Scientific applications
=> game physics
=> data analysis
=> engineering programs

import math

# sqrt() – Square Root
a = 10.53328
b = 3
c =10
print(math.sqrt(a))

# pow() – Power
print(math.pow(a, b))

# ceil() – Round UP
print(math.ceil(a))

# floor() – Round DOWN
print(math.floor(a))

# fabs() – Absolute Value
print(math.fabs(a))

# factorial() – Factorial
print(math.factorial(c))

# Trigonometric Functions
print(math.sin(math.pi / a))
print(math.cos(a))
print(math.tan(a))

# Logarithmic function
print(math.log(a))
print(math.log10(a))

# constrants in math module
print(math.pi)
print(math.e)



# random module
the random module is a built in pyhton module used to genarate random numbers and randome selections
it is commonly used in games, otp ganaration, simulations, quizzes, and testing.
# no install needed just import random

# hou to use random module?
import random

commonly used functions is random module
1. random() => random float (0.0 to 1.0)
2. randint() => random integer(inclusive)
3. randrange() => random number in range
4. choice() => random element from sequence
5. choices() => Multiple random Elements
6. shuffle() => shuffle list
7. sample() => random unique elements

# random() - Random Float (0.0 to 1.0)
import random
print(random.random())
# randint() - Random Integer (inclusive)
print(random.randint(1, 10))
# randrange() - Random Number in Range
print(random.randrange(1, 10, 3))
# choice() - Random Element from Sequence
name = ["esudass", "ganesh", "rame", "some"]
print(random.choice(name))
# choices() - Multiple Random Elements
print(random.choices(name, k = 2))
# shuffle() - Shuffle List
nums = [1, 2, 3, 4, 5, 6,7 ]
random.shuffle(nums)
print(nums)
# sample() - Random Unique Elements
print(random.sample(nums, 3))


# datetime Module
date time module is a bilt in python module used to work with data and time
it helps you get the corrent date, time , perform date calculation, compare date and format date/time
# no installation needed just import datetime

# how to import date time?
import datetime

# main classes in date time module
=> date => only date(year-month-day)
=> time => only time(hours, min, sec)
=> datetime => date + time
=> timedelta => difference between dates/times

# mommonly used operators
# get current date and time
import datetime
now = datetime.datetime.now()
print(now)
# get only date
today = datetime.date.today()
print(today)
# get only time
current_time = datetime.datetime.now().time()
print(current_time)
# create custom date
d = datetime.date(2025, 1, 25)
print(d)
# create custom date and time
dt = datetime.datetime(2025, 1, 25, 10, 30, 59)
print(dt)
# date arithmetic (timedate)
cd = datetime.date.today()
future_date = cd + datetime.timedelta(hours=300)
print(future_date)
# difference between tow dates
d1 = datetime.date(1992,2,23)
d2 = datetime.date.today()
diff = d2 -d1
print(diff.days)
# formate date and time (strftime)
now1 = datetime.datetime.now()
print(now1.strftime("%d-%m-%Y"))
print(now1.strftime("%H:%M:%S"))


# time Module
the time module is a built in python module used to work with time related operations
it helps in pausing program execution, measuring execution time, and working with timestamps
# no installation needed just import time

# how to import time
import time

# commonly used functions in time module

"""

