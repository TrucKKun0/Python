#if conditions

language = 'java'
if language =='python':
    print('Language is python')
elif language =='java':
    print('Language is java')
else:
    print('No match')
print('------------')
#boolean
#and
#or
#not

#And
user = 'Admin'
logged_in = False
if user =='Admin' and logged_in:
    print("Admin Page")
else:
    print("Bad Creds")
#OR
print('------------')

if user =='Admin' or logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

#Not
print('------------')
if not logged_in:
    print("Please Log In")
else:
    print("Welcome")

#is
print('------------')
a=[1,2,3]
b=[1,2,3]

print(a==b)#check the value of a and b in the list
print(a is b)#check the id of a and b in the list
c=a
print(c is a)#check the id of a and c in the list
print(id(a))
print(id(b))
print(id(c))

#False Values:
    #False
    #None
    #Zero of any numeric type
    #Any empty sequence. For example, '', (), [].
    #Any empty mapping. For example, {}.

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')