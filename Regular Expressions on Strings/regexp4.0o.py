import re
#str="aparajitverma@gmail.com,vikas@hello.com"
#p="\w+@\w+[.]\w+"
#r=re.findall(p,str)
#print(r)
tr="[123.5678.34 451.6779.99 [767.1123.67]"
p="\[?\d{3}[.]\d{4}[.]\d{2}[]]?"

r=re.findall(p,tr)
print(r)













