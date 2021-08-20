class Employee:

    # class variable
    num_of_emp = 0
    raise_amount = 1.05

    # __init__(self) method is a constructor for class 
    # here self representes the instance
    # thats why every method under a class have self argument
    def __init__(self, fname, lname, age, email, pay):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = email
        self.pay = pay

        Employee.num_of_emp += 1 # it will tell us that how many times __init__() called or instances have been generated

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# declare instances of Employee class
# obj_name = class_name(values want to pass)
emp_1 = Employee('Suaib', 'Mahmud', 24, 'palash@gmail.com', 30000)
emp_2 = Employee('Deloear', 'Hossen', 25, 'deloear@gmail.com', 120000)

print(Employee.num_of_emp)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)