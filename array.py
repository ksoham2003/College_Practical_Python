import array as arr
a=arr.array('i',[1,2,3])
print("New array")
for i in range(0,3):
    print(a[i],end="")

a1=arr.array('d',[2,5,1.5,3.5])
print("float array")
for i in range(0,3):
    print(a1[i],end="")
a.insert(1, 4)

print(a)

a.append(5)

for i in range(0,5):
    print(a[i],end=" ")
    
a.remove(2)

a.pop()

for i in range (0,3):
    print(a[i],end=" ")

print(a[2])
