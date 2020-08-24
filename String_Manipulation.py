x=[1,2,9,77,45,3,9,8,7]
print(type(x))
x.append(43)
m=x.append("cetpa")
print(m)
x.extend("cetpa")
x.extend([1,2,3,4])
print(x)
m=x.append([2,3,4])
print(x[3])
#print(x.index(9,3,8)) #3,8 means 3 to 7(upper bound-1)   #print(x.index(9,3)) #print(x.index(9))
#print(x.sort())             #search for sort and reverse
m= x.reverse()               #iterator sequence or collection
print(m)
#print(x.clear())




#
import time
t=1
while(t==1):
    print('hello')
    time.sleep(2)
    print('cetpa')
    time.sleep(2)       #sleep delays for 2 second
    t=0
#
