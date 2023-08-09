nameT = ("shriya","chetana","anish");
nameL = list(nameT)
print("List elements : ", nameL)

n = input("Enter the name ")
nameL.append(n)

print("Now list is :",nameL)

nameT=tuple(nameL)
print("Now Tuple is :",nameT)