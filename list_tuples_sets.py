#List (mutable)


courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Nepali','English']
courses.append('Art')
courses.insert(0, 'Education')
courses.extend(courses_2)#extends the list at the end of list without creating a new list
courses.remove('Math')#removes the element from the list
popped = courses.pop()#pops the last element of the list and retruns the poped value
courses.reverse()#reverses the list
courses_2.sort()#sorts the list
sorted_courses = sorted(courses) #doesnt change the acutal list it reqires extra varibale to store the sorted list
nums = [1,5,2,4,3]
# nums.sort() #sorts the list
nums.sort(reverse=True)#sorts the list in reverse order

print(courses.index('CompSci')) #returns the index of the element in the list

print('Art' in courses)#returns boolean value if the element is in the list
print(popped)
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses_2)
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))

for item in courses: #loops through the list
    print(item)

for index, course in enumerate(courses, start=1): #loops through the list with index using enumerate function
    print(index, course)


courses_2_str = ', '.join(courses_2) #joins the list with the given string
print(courses_2_str)
new_course = courses_2_str.split(', ') #splits the string into list with the given string
print(new_course)
print('------------')

#Tuples (immutable)

#mutable values can be changed throughout the program by using insert,pop,remove,append and more.It is useful when you want to make sure that the values are not changed throughout the program.it uses [] instead of ().
list_1 = ['bihsow','dip','rai','is','god']
list_2 = list_1

print(list_1)
print(list_2)
list_1[0] = 'Bishow'
print(list_1)
print(list_2)
print('------------')

#immutable values cannot be changed throughout the program. It is useful when you want to make sure that the values are not changed throughout the program.it uses () instead of [].

tuple_1 = ('GOd','Damn','Good','Shit')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Bishow' it doesnt allow to change the value of the tuple and throws error

print('------------')

#Sets (unordered and no duplicates) it removes dublicate values automatically. It uses {} instead of [] or ().

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)
print('Math' in cs_courses) #checks if the element is in the set
print(cs_courses.intersection(art_courses)) #checks the intersection of the two sets
print(cs_courses.difference(art_courses)) #checks the difference of the two sets
print(cs_courses.union(art_courses)) #checks the union of the two sets