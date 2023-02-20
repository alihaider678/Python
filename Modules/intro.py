
# import my_module

# courses = ['Math', 'Computer', 'Chemistry', 'Physics']

# index = my_module.find_index(courses, 'Chemistry')
# print(index)

#  Another method to import module
# we don't need to import my_module(In this we import only those things which we want to display) e.g;


# from my_module import find_index as fi, test  

# courses = ['Math', 'Computer', 'Chemistry', 'Physics']

# index = fi(courses, 'Chemistry')
# print(index)
# print(test)



# Another example
# In which we grab the random values from through import random library(In each time print random value)
# import random
# courses = ['Math', 'Computer', 'Chemistry', 'Physics']
# random_course = random.choice(courses)
# print(random_course)



# Another example
# In which we solve the math problem through import math library(e.g radius, sin, etc)
# 1)
import math

rads = math.radians(90)
print(rads)

# 2)

import math

rads = math.radians(90)
print(math.sin(rads))


# 3)

import datetime

today = datetime.date.today()
print(today)


# 4)

import calendar

print(calendar.isleap(2013))


import os

print(os.__file__)