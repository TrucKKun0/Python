import sys
import random
import math
import datetime
import calendar
import os

# import my_module as mm this is used to import module as a whole
from my_module import find_index as fi, test #this is used to import specific function from module

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math')

print(index)
print(test)
#print(sys.path)
random_course = random.choice(courses)
print(random_course)
rad = math.radians(90)
print(rad)
print(math.sin(rad))
today = datetime.date.today()
print(today)
print(os.getcwd())
print(calendar.isleap(2020))
print(os.__file__)