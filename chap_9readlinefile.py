# here only one single line will print
f = open('sample.txt')
data = f.readline()
print(data)

#here when we repect above step of readline it will print another line
f = open('sample.txt')
data = f.readline()
print(data)
data = f.readline()
print(data)