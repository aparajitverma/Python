import pickle
import pymysql
#   BLL
class customer:
    listcus=[]
    con=pymysql.connect(host='localhost',user='root',password='root123',database='db1')
    def __init__(self):
        self.id=0
        self.age=0
        self.name=0
    def addcustomer(self):

        customer.listcus.append(self)
        qry='insert into cust values("%s","%s","%s")'
        customer.mycur.execute(qry)
    def searchcustomer(self):
        qry='select * from cust where id= "%s"%(self.id)

        for e in customer.listcus:
            if(e.id==self.id):
                self.age=e.age
                self.name=e.name
                return 1
        return 0
    @staticmethod   #use of static vmethod
    def deleteCustomer(id):
        #for e in customer.listcus:
         #   if e.id==id:
          #      customer.listcus.(e)
        for i in range(len(customer.listcus)):
            if(customer.listcus[i].id==id):
                customer.listcus.pop(i)     #if static less memory will be used as object need not be created

    def modifyCustomer(self):
        for e in customer.listcus:
            if(e.id==self.id):
                e.age=self.age
                e.name=self.name
    @staticmethod
    def func1(ob):
        return ob.name
    @staticmethod
    def sortData():
        customer.listcus.sort(key=customer.func1)
    @staticmethod
    def savetoPickle():
        f=open("Z://cmspickle.txt",'wb')
        pickle.dump(customer.listcus, f)
        f.close()

    @staticmethod
    def loadfromPickle():
        f = open("Z://cmspickle.txt", 'rb')
        customer.listcus=pickle.load(f)
        for e in customer.listcus:

            print(e.name,e.age,e.id)

#PL
def showCustomer(cus):
    qry='select * from cust'
    customer.mycur.execute(qry)
    data=customer.mycur.fetchall
    heading=customer.mycur.description
    print("cust id:",cus.id,'cust age:',cus.age,'cust name:',cus.name)

while(1):
    print('CMS')
    print('Enter choice::')
    print('1 for add  2. for search  3. for delete  4. for modify  5. display  6. exit 7. sort\n 8 for save in pickle,  9  for load in pickle')
    ch=input('enter choice:')
    if ch=='1':
        cus=customer()
        cus.id=input('enter id:')
        cus.age=input('enter age:')
        cus.name=input('enter name:')
        cus.addcustomer()
        print('Customer added succesfully')
    elif ch=='2':
        cus=customer()
        cus.id=input('enter cus id to search')
        flag=cus.searchcustomer()
        if flag==1:
            showCustomer(cus)
        else:
            print('Customer not found')
    elif ch=='3':
        id=input('enter customer id to delete:')
        customer.deleteCustomer(id)     #only one variable needed not three
    elif ch=='4':
        cus=customer()
        cus.id=input('enter customer id')
        cus.age=input('enter cus updated age:')
        cus.name=input('enter updatted name:')
        cus.modifyCustomer()
        print('customer update successfully')
    elif ch=='5':
        for e in customer.listcus:
            showCustomer(e)
    elif ch=='6':
        break
    elif ch=='7':
        customer.sortData()
        print('customer data sorted successfully')
    elif ch=='8':
        customer.savetoPickle()
    elif ch=='9':
        x=customer.loadfromPickle()
        print(x)
    else:
        print('incorrect choice')
