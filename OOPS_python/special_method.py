class Employee():

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
        self.pay = int(self.pay * Employee.raise_amount)
    def __repr__(self):
        return f"Employee('{self.fname}', '{self.lname}', {self.pay})"
    def __str__(self):
        return f"{self.fname} {self.lname} - {self.email}"
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)
print(emp_1 + emp_2)
print(len(emp_1))
print(emp_1)
print(repr(emp_1))
print(str(emp_1))