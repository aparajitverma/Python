import re
str="12,123,4534,667757623432,1312313,123214435"
#p="[0-9]+"
#p="[0-9]*"
#p="[0-9]?"
str1="12av!@+_-2"
p="[0-9]?"
#r=re.findall(p,str1)
r=re.search(p,str1)
print(r)