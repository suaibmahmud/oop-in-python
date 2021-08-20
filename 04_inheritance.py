class Employee:

    # class variable
    raise_amount = 1.05

    # regular method
    # __init__(self) method is a constructor for class 
    # here self representes the instance
    # thats why every method under a class have self argument
    def __init__(self, fname, lname, age, email, pay):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = email
        self.pay = pay

    # regular method
    # it passes instance as the first argument
    # method_name(self, other arguments...)
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self): # regular method
        self.pay = int(self.pay * self.raise_amount)

# here Developer() is a child class and Employee is a parent class
# child_class_name(parent_class_name)
class Developer(Employee):
    raise_amount = 1.10 # override the parent class value

    def __init__(self, fname, lname, age, email, pay, prog_lang):

        # super().__init__(keywords) is used to call parent __init__() method
        # the keywords that passed through super().__init__() will be handled by parent __init__() method
        super().__init__(fname, lname, age, email, pay) # or parent_class_name.__init__(self, keywords...)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, fname, lname, age, email, pay, employees=None): # here employees keyword will take a list of employees that the manager will supervise  
        super().__init__(fname, lname, age, email, pay)
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
            print('=> ', emp.fullname())

# declare instances of Employee class
# obj_name = class_name(values want to pass)
emp_1 = Employee('Suaib', 'Mahmud', 24, 'palash@gmail.com', 30000)
dev_1 = Developer('Deloear', 'Hossen', 25, 'deloear@gmail.com', 30000, 'Java')

emp_1.apply_raise()
dev_1.apply_raise()
print(emp_1.pay) # it will increase the pay according Emplyee raise_amount
print(dev_1.pay) # it will increase the pay according Developer raise_amount

print(dev_1.prog_lang)

mgr_1 = Manager('Shihab', 'Shahriar', 35, 'shihb@gmail.com', 90000, [emp_1, dev_1])

print(mgr_1.print_emps())

emp_2 = Employee('Nazmul', 'Haque', 26, 'nazmul@gmail.com', 30000)
mgr_1.add_emp(emp_2)

print(mgr_1.print_emps())

mgr_1.remove_emp(emp_2)

print(mgr_1.print_emps())