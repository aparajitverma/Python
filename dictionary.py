cust={'1234567891':['aparajit','20'],'18':['rush','21'],'0987654321':['adi','22']}


def searchcust(phn):
    if cust.get(phn)==None:
        print('phone number doesnt exist')
    else:
        print('phone number:',phn,'name and age',cust.get(phn))


def delcust(phn):
    cust.pop(phn)


def modcust(phn):
    pass



def discust():
    print('phone number ,name and age',cust.items())



















while(1):
    ch=input('enter choice:')
    if ch=='1':
        addcust()
    elif ch=='2':
        phn=input('Enter id whose info is to be searched')
        searchcust(phn)
    elif ch=='3':
        phn = input('Enter id whose info is to be deleted')
        delcust(phn)
        print('cus deleted successfully')
    elif ch=='4':
        phn=input('enter id who is to be modified')
        modcust(phn)
    elif ch=='5':
        discust()
    elif ch=='6':
        break
    else:
        print('wrong choice')


def searchcust(phn):
    print('phone number:',phn,'name and age',cust.values)