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
        self.pay = int(self.pay * self.raise_amount)
#inheritance is a way to create a new class that is a modified version of an existing class
#the new class is called the child class or subclass and the existing class is called the parent class or superclass
class Developer(Employee):
    raise_amount = 1.10
    def __init__(self,fname,lname,pay,prog_lang):
        #super() is a built-in function that returns a temporary object of the superclass
        #that allows us to call its methods and properties
        super().__init__(fname,lname,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,fname,lname,pay,employees=None):
        super().__init__(fname,lname,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Jim', 'Brown', 70000,"Python")
dev_2 = Developer('Sara', 'White', 80000,"Java")

mgr_1 = Manager('Sue', 'Black', 90000, [dev_1])
print(mgr_1.email)
print(mgr_1.print_emps())
mgr_1.add_emp(dev_2)
print(mgr_1.print_emps())
mgr_1.remove_emp(dev_1)
print(mgr_1.print_emps())

#mgr_1 is not an instance of the Developer class
print(isinstance(mgr_1, Developer))
#mgr_1 is an instance of the Employee class
print(isinstance(mgr_1, Employee))
#dev_1 is an instance of the Developer class but not an instance of the Manager class
print(isinstance(dev_1, Manager))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))


# print(dev_1.email)
# print(dev_1.prog_lang)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
