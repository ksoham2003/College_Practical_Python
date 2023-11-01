class Employee:
    company = "google"
    salary = 100
vijay = Employee()
sara = Employee() 
vijay.salary = 300
sara.salary = 400
print(vijay.company)
print(sara.company)

Employee.company = "Youtube"
print(vijay.company)
print(sara.company)
print(vijay.salary)
print(sara.salary)