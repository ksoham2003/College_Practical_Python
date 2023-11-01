
f = open("sample.txt",'r')
text = f.read() 
print(text)
f.close() 

# it reads only 5 char.
f = open("sample.txt",'r')
text = f.read(7)
print(text)
f.close()

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

#with function
with open('another.txt','r') as f:
    a = f.read()
print(a)

with open('another.txt','w') as f:
    a = f.write("good morning here im we have to go.")
print(a)


#append function
f = open('another.txt','a')
data = f.write(".im appending here\n")
f.close

#readline function
file = open("another.txt",'r')
print(file.readline(8))
file.seek(0)
print(file.readline())
file.close()

