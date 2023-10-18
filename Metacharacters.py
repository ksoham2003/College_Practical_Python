import re

print("\"Hello\"")

txt = "This is python programming" 
print(re.findall("[p-t]", txt))

print(bool(re.findall("^python",txt)))

print(bool(re.findall("programming$",txt)))

print(re.findall("pyt..n",txt))

print(re.findall("pro*gramming",txt))

print(re.findall("prog+ramming",txt))

print(re.findall("program?ing",txt))