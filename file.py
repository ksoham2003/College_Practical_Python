file = open("myfile.txt","w")
L = ["This is lagos \n","this is python \n","This is Ecc \n"]

file.write("Hello There \n")
file.writelines(L)
file = open("myfile.txt","r")
print(file.read())
file.close()