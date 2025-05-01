#Function 

#this function doesnt return anything
def hello_fun():
    print('Hello Function1!')

hello_fun()

#this function returns a value
def hello_fun():
    return 'Hello Function2!'

print(hello_fun())

#this fuction requires a parameter
def hello_fun(greeting,name='You'): #name is a default parameter. if there is no parameter passed it will use the default parameter
    print('{}, {}!'.format(greeting,name))

hello_fun('Hi',name='Bishow')

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

#student_info('Math','Art',name='Bishow',age=25)

courses = ['Math','Art']
info = {'name':'Bishow','age':25}

student_info(*courses,**info)

#exmaple of function calculation of is it a leap year or not
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    '''Return True for leap years, False for non-leap years.'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year,month):
    '''Return number of days in that month in that year.'''
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2020))
print(days_in_month(2012,2))
