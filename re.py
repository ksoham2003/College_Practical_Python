import re
s = "This is a python program"

match = re.search('program',s)
print('Start index', match.start())
print('End Index ',match.end())
print(match)

str = "Hello my no. is 1234567890 & another no. is 9876543210"

regex = '\d+'
match = re.findall(regex,str)
print(match)
