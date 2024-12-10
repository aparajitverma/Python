# BLL
custid = []
custname = []
custage = []

def addCustomer(ID, NAME, AGE):
    custid.append(ID)
    custname.append(NAME)
    custage.append(AGE)

def searchCustomer(X):
    if custid.count(X) == 0:
        return None
    else:
        index = custid.index(X)
    return index

def showCustomer(ind):
    print('Customer id:', custid[ind])
    print('Customer name:', custname[ind])
    print('Customer age:', custage[ind])

def deleteCustomer(X):
    index = searchCustomer(X)
    if index is not None:
        custid.pop(index)
        custname.pop(index)
        custage.pop(index)
        print('Customer deleted successfully.')
    else:
        print('Customer not found.')

def modifyCustomer(X, name, age):
    index = searchCustomer(X)
    if index is not None:
        custname[index] = name
        custage[index] = age
        print('Customer modified successfully.')
    else:
        print('Customer not found.')

# PL
print('\t\t\tCUSTOMER MANAGEMENT SYSTEM')
while True:
    print('\nChoices are:')
    print('1. CREATE OR ADD A NEW CUSTOMER')
    print('2. SEARCH FOR A CUSTOMER')
    print('3. DELETE A CUSTOMER')
    print('4. MODIFY/UPDATE A CUSTOMER')
    print('5. DISPLAY ALL')
    print('6. EXIT')
    
    ch = input('Enter choice (1-6): ')
    
    if ch == '1':
        id = input('Enter customer id: ')
        name = input('Enter customer name: ')
        age = input('Enter customer age: ')
        addCustomer(id, name, age)
        print('Customer successfully added!')
    
    elif ch == '2':
        x = input('Enter id of the customer to be searched: ')
        index = searchCustomer(x)
        if index is None:
            print('Customer not found.')
        else:
            showCustomer(index)
    
    elif ch == '3':
        x = input('Enter id of the customer to be deleted: ')
        deleteCustomer(x)
    
    elif ch == '4':
        x = input('Enter id of the customer whose info is to be modified: ')
        name = input('Enter new name: ')
        age = input('Enter new age: ')
        modifyCustomer(x, name, age)
    
    elif ch == '5':
        print('Displaying all customers:')
        for i in range(len(custid)):
            showCustomer(i)
    
    elif ch == '6':
        print('Exiting the system...')
        break
    
    else:
        print('Incorrect choice! Please enter a valid option.')
