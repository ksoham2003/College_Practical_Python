#list method sorthing
 
l1 = [1,8,7,2,21,15]
print(l1)
l1.sort()
print(l1)

#list method reverse

l2 = [1,8,7,2,21,15]
l2.sort()
l2.reverse()
print(l2)

#list method append

l3 = [1,8,7,2,21,15]
l3.sort()
l3.append(45)
l3.append(83)
print(l3)

#list method insert

l4 = [1,8,7,2,21,15]
print(l4)

#list method pop

l3.pop(2)
print(l3)

#list method remove

l3.remove(15)
print(l3)

l1 = [1,2,"hello",3,4]
l2 = [24,32,"good morning",20,49]
print(type(l1))
print(l1[0:])
print(l1[:])
print(l1[2:4])
print(l1[:4])
print(l1[1:2:4])
print(l1[-1])
print(l1[-3:1])
l1[2] = 10
print(l1)
l1[2:4] = [89,86]
print(l1)

#repectation
l2 = l2 * 2
print(l2)

#concatiation
l3 = l1 + l2
print(l3)

#adding element

l4 :[]
n = int(input("enter the number"))
for i in range(0,n):
    l4.append (input("enter the element"))
for i in l4:
    print(i,end = ' ')
l4.remove(1)
print(l4)
print(len(l4))



