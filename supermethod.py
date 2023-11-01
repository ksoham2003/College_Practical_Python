class Person:
    country = 'India'
    
    def takebreak(self):
        print("i'm breating")
        
class Employee(Person):
    company = 'honda'
    
    def getsalary(self):
        print(f'the salary is {self.salary}')
        
    def takebreak(self):
        super().takebreak()    
        print('im breating so luckkly')
        
class Programmer(Employee):
    company = 'fiveer'
    
    def getsalary(self):
        super().takebreak()     
        print(f'no salary to programmer')
        
p = Person()
p.takebreak()
e = Employee()
print(e.company)
e.salary = 1000
e.getsalary()
e.takebreak()
f = Programmer()        
f.getsalary()
            