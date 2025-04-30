#dictionary is a collection of key value pairs. It is unordered and mutable. It is used to store data in key value pairs. It is used to store data in a structured way. It is used to store data in a way that is easy to access. It is used to store data in a way that is easy to modify. It is used to store data in a way that is easy to delete. It is used to store data in a way that is easy to

student = {'name': 'Bishow', 'age': 25, 'courses': ['Math', 'CompSci']}
student.update({'name': 'Bishow Rai', 'age': 26, 'phone': '555-5555'})

print(student)
print(student['name'])
print(student.get('courses'))
print(student.get('phone', 'Not Found')) #returns the value of the key if it exists else returns the default value
age = student.pop('age') #removes the key value pair and returns the value
print(age)
print('-----------')
print(student.keys())#returns the keys of the dictionary
print(student.values())#returns the values of the dictionary
print(student.items())#returns the key value pairs of the dictionary

for key, value in student.items(): #loops through the dictionary
    print(key, value)

