import re
#str="wlcome to cepta. award winning trainingg inss"
#p="\w\w\w\w"
#r=re.findall(p,str)
#print(r)
str="12,34,123,9811177975,9988775566,Ph98339620565"
#p="\d{10}"
#p="[0-9]{,12}"     #{}matches quantity
p="[0-9]{1,12}"
r=re.findall(p,str)
print(r)





