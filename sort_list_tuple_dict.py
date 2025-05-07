#Sorting List
li = [9,2,3,4,5,6,7,8,1]
s_li = sorted(li)  # Sort the list in ascending order
ds_li = sorted(li, reverse=True)  # Sort the list in descending order
print("Sorted list in descending order ",ds_li)  # This will print the sorted list in descending order
print("Sorted list ",s_li)  # This will print the sorted list
li.sort(reverse=True)  # Sort the list in place
# The original list remains unchanged because sorted() returns a new sorted list.
print("Original list ",li)  # This will print the original list

#Sorting Tuple
tup = (9,2,3,4,5,6,7,8,1)
s_tup = sorted(tup)  # Sort the tuple in ascending order
ds_tup = sorted(tup, reverse=True)  # Sort the tuple in descending order
print("Sorted tuple in descending order ",ds_tup)  # This will print the sorted tuple in descending order
print("Sorted tuple ",s_tup)  # This will print the sorted tuple

#Sorting Dictionary
dict = {'name': 'John', 'age': 30, 'city': 'New York'}
s_dict = sorted(dict)  # Sort the dictionary by keys in ascending order
print("Sorted dictionary ",s_dict)  # This will print the sorted dictionary by keys

abs_list = [1, -2, 3, -4, 5]
s_abs_list = sorted(abs_list, key=abs)  # Sort the list by absolute values
print("Sorted list by absolute values ",s_abs_list)  # This will print the sorted list by absolute values

#Example
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({}, {}, {})'.format(self.name, self.age, self.salary)

e1 = Employee('John', 30, 50000)
e2 = Employee('Jane', 25, 60000)
e3 = Employee('Doe', 35, 70000)

Employees = [e1, e2, e3]
def e_sort(emp):
    return emp.name  # Sort by name
sort_emp = sorted(Employees, key=e_sort,reverse=True)  # Sort the list of employees by salary
print("Sorted Employees by salary ",sort_emp)  # This will print the sorted list of employees by salary