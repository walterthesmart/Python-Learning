#Pythom Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last= last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
emp_1 = Employee('Corey', 'Schafer', 60000)
emp_2 = Employee('Walter', 'Nwaugo', 200000)

print(emp_1)
print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.schafer@company.com'
# emp_1.pay = 60000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 50000

print(emp_1.email)
print(emp_2.email)
print("{} {}".format(emp_1.first, emp_1.last))