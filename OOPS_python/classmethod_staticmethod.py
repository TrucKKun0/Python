class Employee():
# class variable
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
        Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)
#class method is a method that is bound to the class and not the instance of the class it passes the class as the first argument instead of the instance
# class method can be called on the class itself or on the instance of the class
#employee is a class when we use class method set_raise_amount it changes the class variable raise_amount which is shared by all instances of the class
# Employee.set_raise_amount(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Jane-Smith-80000'



# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)

#static method is a method that does not pass the class or instance as the first argument
# static method can be called on the class itself or on the instance of the class
# static method is used to perform a task that does not require access to the class or instance

import datetime

my_date = datetime.date(2023, 10, 1)
print(Employee.is_workday(my_date))