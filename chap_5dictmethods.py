mydict ={"vijay":"shete",
         "everything":" is fair in love and war",
         "Marks":[0,1,2],
         "anotherdic":{'vijay':'player'},
         1:2 #only integer we can write without "".
         
} 
# dict method key (keys) it will print all the keys present in code
print(mydict.keys())

#dict  method key (value) it will print all the values present in code
print(mydict.values())

#dict method key (items) it will print all the contant that is p;resent in table.
print(mydict.items())

#dict method key (update) it will update the code which we are written in above {}code. 
#it will also update the eariler key than udated value.
updatedict = { "lovish":"friends",
               "vijay": "coder"}  
mydict.update(updatedict)
print(mydict)

#dict method key (get)
print(mydict.get("vijay")) # print value associated with key "vijay" 
print(mydict["vijay"]) #print value assoicated with key "vijay" 

# differnce between   
print(mydict.get("vijay2")) #return none as vijay2 is not present in the dict
print(mydict["vijay2"]) #throw an error as vijay2 is not present in dict