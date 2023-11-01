class Person:
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag
    def display1(self):
        print('the person is diaplay method')
        
class Employee(Person):
    def __init__(self,nm,ag, sal):
        super().__init__(nm,ag)
        self.salary = sal
    def display2(self):
        print('the Employee is diaplay method')
        
class Student(Person):
    def __init__(self, nm, ag,m):
        super().__init__(nm,ag)
        self.marks = m
    def display3(self):
        print('the display is diaplay method') 
        
s1 = Student('jay',20,50000)
e1 = Employee('raj',23,500)
p1 = Person('sara',23)

s1.display1()

        
        
    