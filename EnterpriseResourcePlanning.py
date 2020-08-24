class mains:
    listerp=[]
    def __init__(self):
        self.age=0
        self.name=0
        self.id=0
        self.area=0
        self.share=0
        self.course=0


class director(mains):
    def addDirc(self):
        mains.listerp.append(self)
    def searchDirc(self):
        for e in mains.listerp:
            if e.id==self.id:
                self.name=e.name
                self.age=e.age
                self.share=e.share
                return 1
            else:
                return 0
    def modifyDirc(self):
        for e in mains.listerp:
            if e.id==self.id:
                self.name=e.name
                self.age=e.age
                self.share=e.share
                return 1
        else:
            return 0
    def delDirc(self):
        for e in mains.listerp:
            if e.id==self.id:
                mains.listerp.pop(self)
                return 1
            else:
                return 0
    def dispDirc(self):
        for e in mains.listerp:
            print(e.name,e.id,e.age,e.share)

class trainer(mains):
    def addTrn(self):
        mains.listerp.append(self)

    def searchTrn(self):
        for e in mains.listerp:
            if e.id == self.id:
                self.name = e.name
                self.age = e.age
                self.course = e.course
                return 1
            else:
                return 0

    def modifyTrn(self):
        for e in mains.listerp:
            if e.id == self.id:
                self.name = e.name
                self.age = e.age
                self.course = e.course
                return 1
        else:
            return 0

    def delTrn(self):
        for e in mains.listerp:
            if e.id == self.id:
                mains.listerp.pop(self)
                return 1
            else:
                return 0

    def dispTrn(self):
        for e in mains.listerp:
            print(e.name, e.id, e.age, e.course)

class manager(mains):
    def addMng(self):
        mains.listerp.append(self)

    def searchMng(self):
        for e in mains.listerp:
            if e.id == self.id:
                self.name = e.name
                self.age = e.age
                self.area = e.area
                return 1
            else:
                return 0

    def modifyMng(self):
        for e in mains.listerp:
            if e.id == self.id:
                self.name = e.name
                self.age = e.age
                self.area = e.area
                return 1
        else:
            return 0

    def delMng(self):
        for e in mains.listerp:
            if e.id == self.id:
                mains.listerp.pop(self)
                return 1
            else:
                return 0

    def dispMng(self):
        for e in mains.listerp:
            print(e.name, e.id, e.age, e.area)


while(1):
    print('\t\t\tEnterprise resource planning')

    print('Enter choice of occupation\n1.DIRECTOR\n2.TRAINER\n3.MANAGER\n4.EXIT')
    ch=input('enter choice(1-4):')
    print('ENTER CHOICE\n1.ADD\n2.SEARCH\n3.MODIFY\n4.DELETE\n5.DISPLAY ALL')
    ch1=input('enter choice(1-6):')
    if ch=='1':
        dir= director()
        if ch1=='1':
            name=input('enter name:')
            age=input('enter age:')
            id=input('enter id:')
            share=input('enter amount of shares:')
            dir.addDirc()
            print('director added successfully')
        if ch1=='2':
            id=input('enter id to search:')
            flag = dir.searchDirc()
            if flag==1:
                print('name::',dir.name,'age:',dir.age,'share:',dir.share)
            else:
                print('id doesnt exist!!  enter valid id')
        if ch1=='3':
            id=input('enter id to be modified')
            new_name=input('enter new name:')
            new_age=input('enter new age:')
            new_share=input('enter new share:')
            flag=dir.modifyDirc()
            if flag==1:
                print('Director modified successfully')
            else:
                print('id is not found!! enter valid id')
        if ch1=='4':
            id=input('enter id to be deleted:')
            flag=dir.delDirc()
            if flag==1:
                print('director deleted successfully')
            else:
                print('invalid id')
        if ch1=='5':
            dir.dispDirc()





    if ch=='2':
        trn= trainer()
        if ch1=='1':
            name=input('enter name:')
            age=input('enter age:')
            id=input('enter id:')
            course=input('enter name of course:')
            trn.addTrn()
            print('trainer added successfully')
        if ch1=='2':
            id=input('enter id to search:')
            flag = trn.searchTrn()
            if flag==1:
                print('name::',trn.name,'age:',trn.age,'course:',trn.course)
            else:
                print('id doesnt exist!!  enter valid id')
        if ch1=='3':
            id=input('enter id to be modified')
            new_name=input('enter new name:')
            new_age=input('enter new age:')
            new_course=input('enter new course:')
            flag=trn.modifyTrn()
            if flag==1:
                print('Trainer modified successfully')
            else:
                print('id is not found!! enter valid id')
        if ch1=='4':
            id=input('enter id to be deleted:')
            flag=trn.delTrn()
            if flag==1:
                print('trainer deleted successfully')
            else:
                print('invalid id')
        if ch1=='5':
            trn.dispTrn()




    if ch=='3':
        mng=manager()
        if ch1=='1':
            name=input('enter name:')
            age=input('enter age:')
            id=input('enter id:')
            area=input('enter area:')
            mng.addMng()
            print('manager added successfully')
        if ch1=='2':
            id=input('enter id to search:')
            flag = mng.searchDirc()
            if flag==1:
                print('name::',mng.name,'age:',mng.age,'area:',mng.area)
            else:
                print('id doesnt exist!!  enter valid id')
        if ch1=='3':
            id=input('enter id to be modified')
            new_name=input('enter new name:')
            new_age=input('enter new age:')
            new_area=input('enter new area:')
            flag=mng.modifyMng()
            if flag==1:
                print('Manager modified successfully')
            else:
                print('id is not found!! enter valid id')
        if ch1=='4':
            id=input('enter id to be deleted:')
            flag=mng.delMng()
            if flag==1:
                print('manager deleted successfully')
            else:
                print('invalid id')
        if ch1=='5':
            mng.dispMng()

    if ch=='4':
        break


