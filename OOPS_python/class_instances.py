class Employee(): 
    #self is a instance variable which is automatically passed to the instance of the class when it is created
    # instance variable is unique to each instance of the class
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())