#BLL
custid=[]
custname=[]
custage=[]
def addCustomer(ID,NAME,AGE):
    custid.append(ID)
    custname.append(NAME)
    custage.append(AGE)
def searchCustomer(X):
    if(custid.count(X)==0):
        return None
    else:
        index=custid.index(X)
    return index
def showCustomer(ind):                      #kaushikvasu98@gmail.com
    print('customer id:',custid[ind],'\ncustomer name::',custname[ind],'\ncustomer name',custage[index])
def deleteCustomer(X):
    index=custid.index(X)
    custid.pop(index)
    custname.pop(index)
    custage.pop(index)
def modifyCustomer(X,name,age):
    if (custid.count(X) == 0):
        return None
    else:
        index = custid.index(X)
        custname[index]=name
        custage[index]=age


#PL
print('\t\t\tCUSTOMER MANAGEMENT SYSTEM')
while(1):
    print('Choices are:\n1.CREATE OR ADD A NEW CUSTOMER\n2.SEARCH FOR A CUSTOMER\n3.DELETE A CUSTOMER\n4.MODIFY/UPDATE A CUSTOMER')
    print('5.DISPLAY ALL\n6.EXIT')
    ch=input('enter choice(1-7)')
    if ch=='1':
        id=input('Enter customer id::')
        name=input('Enter customer name::')
        age=input('Enter customer age::')
        addCustomer(id,name,age)
        print('customer successfully added!!')
    elif ch=='2':
        x=input('enter id of the customer who is to be searched')
        index=searchCustomer(x)
        if(index==None):
            print('customer not found')
        else:
            showCustomer(index)

    elif ch=='3':
        x=input('enter id who is to be deleted')
        ch1=input('are you sure(y/n)')
        if(ch1=='y'):
             m=deleteCustomer(x)
             print('customer deleted')
        else:
            break
    elif ch=='4':   #modify
        x=input('enter id whose info is to be modified')
        
        name=input('enter new name')
        age=input('enter new age')
        flag=index=modifyCustomer(x,name,age)
        if flag==False:
            print('cust not found:')
        else:
            print('cust modified successfully')
    elif ch=='5':
        for i in range(len(custid)):
            print('Customer id::',custid[i],'Customer name::',custname[i],'customer age::',custage[i])
    elif ch=='6':
        break
    else:
        print('Incorrect choice!!!')
