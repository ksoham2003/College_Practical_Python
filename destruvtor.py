import time
class Employee:
    def __init__(self,nm,sal):
        self.name = nm
        self.salary = sal
    
    def display(self):
        print(f"name is {self.name}\n salary is {self.salary}")

#defining the destructor
    def __del__(self):
        print("Destructor is called")
    
e1 = Employee("Shantanu",50000)
e2 = e1

del e1

time.sleep(5)
        