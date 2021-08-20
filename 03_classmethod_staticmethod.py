class Employee:

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

    # class method is decorated by @classmethod
    # method_name(cls, other arguments...)
    # it passes class as the first argument
    @classmethod
    def strToemp(cls, emp_str):
        fname, lname, age, email, pay = emp_str.split('-')
        return cls(fname, lname, age, email, pay) 

    # static method is decorated by @staticmethod
    # method_name(arguments...)
    @staticmethod
    def is_workday(day):
        if day.lower() == 'friday' or day.lower() == 'saturday':
            return 'Holiday'
        return 'Workday'

# declare instances of Employee class
# obj_name = class_name(values want to pass)
emp_1 = Employee('Suaib', 'Mahmud', 24, 'palash@gmail.com', 30000)
emp_2 = Employee('Deloear', 'Hossen', 25, 'deloear@gmail.com', 120000)
emp_3 = Employee.strToemp('Nazmul-Haque-26-nazmul@gmail.com-80000')

print(emp_3.fullname())
print(Employee.is_workday('friday'))

