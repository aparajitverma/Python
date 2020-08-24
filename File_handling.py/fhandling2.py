def mystr(l3):
    L4=[]
    for e in l3:
        L4.append(str(e)+'\n')
    return L4
f=open('Z://asd.xls','w')
f.write('98117865')
f.write('\n798456123')
f.write('\t6459879123')
L1=[1234667,12334655,2437697134]
L2=mystr(L1)
print(L2)