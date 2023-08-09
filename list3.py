#Adding element in list
l4=[]
n = int(input("Enter the no. of element"))
for i in range(0,n):
    l4.append(input("Enter element :"))
for i in l4:
    print(i,end=" ")

print(l4)
print(len(l4))
print(min(l4))
print(max(l4))