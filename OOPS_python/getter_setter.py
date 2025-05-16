class Employee():

    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    @property
    def email(self):
        return self.fname + '.' + self.lname + '@company.com'
    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.fname = first
        self.lname = last
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.fname = None
        self.lname = None
        
emp_1 = Employee('John', 'Doe', 50000)

emp_1.fullname = 'Jane Smith'
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname