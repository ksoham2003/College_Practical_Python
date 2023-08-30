import re
s = "This is a python program"

match = re.search('program',s)
print('Start index', match.start())
print('End Index ',match.end())
print(match)