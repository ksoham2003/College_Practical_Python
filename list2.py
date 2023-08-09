l1=[1,2,"Hello",3.5]
l1[2]=10
print(l1)
l1[2:4]=[89,36]
print(l1)

#Repetition
l2=l1*3
print(l2)

#concatenation
l3=l1+l2
print(l3)
print(len(l3))

#iterating 
for l in l3:
    print(l)

print(1 in l1)