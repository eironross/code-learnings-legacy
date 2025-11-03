# Testing and understanding the class variables

class Employee():
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def pay_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)
        
emp_1 = Employee("Eiron", "Flores", 45000)
emp_2 = Employee("Free", "Guy", 45000)

print(Employee.__dict__)
print(emp_1.pay_raise())
print(emp_1.pay)


emp_1.raise_amt = 1.05

print(emp_1.__dict__)
print(emp_1.pay_raise())
print(emp_1.pay)

class Eiron():
    pass


name = Eiron()
name.first = "eiron"
name.last = "flores"

print(name.__dict__)