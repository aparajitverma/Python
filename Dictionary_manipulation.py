#x={1:55,2:77,10*8:83}# keys are case sensitive
#x.update({9:50})
#x.setdefault(2,88) #if matching key is already available,value will not change
#m='abc'
#m=x.fromkeys(m)
#m=dict.fromkeys(m)
#print(m)
#print(x)

key=[1,2,3,4]
values=[33,44,55,66]
d=dict.fromkeys(key)
print(d)
i=0
for e in d.keys():
    d[e]=values[i]
    i+=1                #how to make dictionary using list keys and values
print(d)
