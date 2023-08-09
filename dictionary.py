d1 = {1:"Hello", 2:"Hi",'a':"Welcome"}
print (d1.keys())
print(d1.values())
print(d1.items())
print(d1.get('a'))
newd=d1.copy()
print(newd)
print(d1.pop(1))
print(d1)
print(d1.popitem())
print(d1)

d2={4:"Welcome"}
d1.update(d2)
print(d1)

d1.update([(5,"Hi")])
print(d1)

d1.clear()
print(d1)

d3={'a','b','c'}
d4=dict.fromkeys(d3,1)
print(d4)