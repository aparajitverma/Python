class Mains:
    listerp = []

    def __init__(self, name="", age=0, id=0, area=0, share=0, course=0):
        self.name = name
        self.age = age
        self.id = id
        self.area = area
        self.share = share
        self.course = course


class Director(Mains):
    def addDirc(self):
        Mains.listerp.append(self)

    def searchDirc(self):
        for e in Mains.listerp:
            if e.id == self.id:
                self.name = e.name
                self.age = e.age
                self.share = e.share
                return 1
        return 0

    def modifyDirc(self):
        for e in Mains.listerp:
            if e.id == self.id:
                e.name = self.name
                e.age = self.age
                e.share = self.share
                return 1
        return 0

    def delDirc(self):
        for e in Mains.listerp:
            if e.id == self.id:
                Mains.listerp.remove(e)
                return 1
        return 0

    def dispDirc(self):
        for e in Mains.listerp:
            print(f"Name: {e.name}, ID: {e.id}, Age: {e.age}, Share: {e.share}")


class Trainer(Mains):
    def addTrn(self):
        Mains.listerp.append(self)

    def searchTrn(self):
        for e in Mains.listerp:
            if e.id == self.id:
                self.name = e.name
                self.age = e.age
                self.course = e.course
                return 1
        return 0

    def modifyTrn(self):
        for e in Mains.listerp:
            if e.id == self.id:
                e.name = self.name
                e.age = self.age
                e.course = self.course
                return 1
        return 0

    def delTrn(self):
        for e in Mains.listerp:
            if e.id == self.id:
                Mains.listerp.remove(e)
                return 1
        return 0

    def dispTrn(self):
        for e in Mains.listerp:
            print(f"Name: {e.name}, ID: {e.id}, Age: {e.age}, Course: {e.course}")


class Manager(Mains):
    def addMng(self):
        Mains.listerp.append(self)

    def searchMng(self):
        for e in Mains.listerp:
            if e.id == self.id:
                self.name = e.name
                self.age = e.age
                self.area = e.area
                return 1
        return 0

    def modifyMng(self):
        for e in Mains.listerp:
            if e.id == self.id:
                e.name = self.name
                e.age = self.age
                e.area = self.area
                return 1
        return 0

    def delMng(self):
        for e in Mains.listerp:
            if e.id == self.id:
                Mains.listerp.remove(e)
                return 1
        return 0

    def dispMng(self):
        for e in Mains.listerp:
            print(f"Name: {e.name}, ID: {e.id}, Age: {e.age}, Area: {e.area}")


# Main loop
while True:
    print('\t\t\tEnterprise Resource Planning')
    print('Enter choice of occupation\n1. DIRECTOR\n2. TRAINER\n3. MANAGER\n4. EXIT')
    ch = input('Enter choice (1-4): ')
    print('ENTER CHOICE\n1. ADD\n2. SEARCH\n3. MODIFY\n4. DELETE\n5. DISPLAY ALL')
    ch1 = input('Enter choice (1-5): ')

    if ch == '1':
        dir = Director()
        if ch1 == '1':
            dir.name = input('Enter name: ')
            dir.age = int(input('Enter age: '))
            dir.id = int(input('Enter ID: '))
            dir.share = float(input('Enter amount of shares: '))
            dir.addDirc()
            print('Director added successfully')
        elif ch1 == '2':
            dir.id = int(input('Enter ID to search: '))
            if dir.searchDirc() == 1:
                print(f"Name: {dir.name}, Age: {dir.age}, Share: {dir.share}")
            else:
                print('ID doesn\'t exist! Enter a valid ID')
        elif ch1 == '3':
            dir.id = int(input('Enter ID to modify: '))
            dir.name = input('Enter new name: ')
            dir.age = int(input('Enter new age: '))
            dir.share = float(input('Enter new share amount: '))
            if dir.modifyDirc() == 1:
                print('Director modified successfully')
            else:
                print('ID not found! Enter a valid ID')
        elif ch1 == '4':
            dir.id = int(input('Enter ID to delete: '))
            if dir.delDirc() == 1:
                print('Director deleted successfully')
            else:
                print('Invalid ID')
        elif ch1 == '5':
            dir.dispDirc()

    elif ch == '2':
        trn = Trainer()
        if ch1 == '1':
            trn.name = input('Enter name: ')
            trn.age = int(input('Enter age: '))
            trn.id = int(input('Enter ID: '))
            trn.course = input('Enter course name: ')
            trn.addTrn()
            print('Trainer added successfully')
        elif ch1 == '2':
            trn.id = int(input('Enter ID to search: '))
            if trn.searchTrn() == 1:
                print(f"Name: {trn.name}, Age: {trn.age}, Course: {trn.course}")
            else:
                print('ID doesn\'t exist! Enter a valid ID')
        elif ch1 == '3':
            trn.id = int(input('Enter ID to modify: '))
            trn.name = input('Enter new name: ')
            trn.age = int(input('Enter new age: '))
            trn.course = input('Enter new course: ')
            if trn.modifyTrn() == 1:
                print('Trainer modified successfully')
            else:
                print('ID not found! Enter a valid ID')
        elif ch1 == '4':
            trn.id = int(input('Enter ID to delete: '))
            if trn.delTrn() == 1:
                print('Trainer deleted successfully')
            else:
                print('Invalid ID')
        elif ch1 == '5':
            trn.dispTrn()

    elif ch == '3':
        mng = Manager()
        if ch1 == '1':
            mng.name = input('Enter name: ')
            mng.age = int(input('Enter age: '))
            mng.id = int(input('Enter ID: '))
            mng.area = input('Enter area: ')
            mng.addMng()
            print('Manager added successfully')
        elif ch1 == '2':
            mng.id = int(input('Enter ID to search: '))
            if mng.searchMng() == 1:
                print(f"Name: {mng.name}, Age: {mng.age}, Area: {mng.area}")
            else:
                print('ID doesn\'t exist! Enter a valid ID')
        elif ch1 == '3':
            mng.id = int(input('Enter ID to modify: '))
            mng.name = input('Enter new name: ')
            mng.age = int(input('Enter new age: '))
            mng.area = input('Enter new area: ')
            if mng.modifyMng() == 1:
                print('Manager modified successfully')
            else:
                print('ID not found! Enter a valid ID')
        elif ch1 == '4':
            mng.id = int(input('Enter ID to delete: '))
            if mng.delMng() == 1:
                print('Manager deleted successfully')
            else:
                print('Invalid ID')
        elif ch1 == '5':
            mng.dispMng()

    elif ch == '4':
        break
