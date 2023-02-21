# Pyhton Object Oriented Programming

# 2) Classes Variables

class Employee:

    #Create Variable

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# If we want to see the raise amount of Employees then?

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# If we want to change the raise amount of Employee1 then?

emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# If we want to see how many employees ?

print(Employee.num_of_emps)
