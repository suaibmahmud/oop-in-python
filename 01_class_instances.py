class Employee:

    # __init__(self) method is a constructor for class 
    # here self representes the instance
    # thats why every method have self argument
    def __init__(self, fname, lname, age, email):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = email

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

# declare instances of Employee class
# obj_name = class_name(values want to pass)
emp_1 = Employee('Suaib', 'Mahmud', 24, 'palash@gmail.com')
emp_2 = Employee('Deloear', 'Hossen', 25, 'deloear@gmail.com')

print(emp_1.age)
print(emp_2.email)
print(emp_1.fullname())