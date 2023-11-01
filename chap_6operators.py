#reletional operator.

a = input("enter you age")
a = int(a)

if(a>18):
    print("you can vote")
elif(a>=18):
    print("you can vote")
else:
    print("you can't vote")
    
print(a)

#logical operators

#and operator
age = int(input("enter the number"))   
if(age>34 and age<56):
    print("you can work with us")
else:
    print("notwork with us")
    
#or operator
age = int(input("enter the number"))  
if(age>34 or age>56):
    print("you can work with us")
else:
    print("not work with us")

#not operater
print("The value of 'not True': ", not True)   
print("The value of 'not Frue': ", not False) 