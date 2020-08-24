class class1:
    def __init__(self):
        self.a=5
        self.b=6
    def showdata(self):
        print('in class 1  a:',self.a,'b:',self.b)
class class2:
    def __init__(self):
        self.c=1
        self.d=2

    def showdata(self):
        print('in class 2',self.c,self.d)
class class3:
    def __init__(self):
        self.e=3
        self.f=4

    def showdata(self):
        print('in class 3',self.e,self.f)
class class4(class1,class2,class3):
    def __init__(self):
        self.g=7
        self.h=8
        super().__init__()
        class2.__init__(self)
        class3.__init__(self)ob1.showdata()

    def showdata(self):
        print('in clss 4',self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h)

ob1=class1()
ob2=class2()
ob2.showdata()
ob3=class3()
ob4=class4()
ob4.showdata()
class1.showdata(ob4)
x=[1,2,3]
x.append(5)     # two ways of calling class functions
list.append(x, 5)
print(x)
print(class4.__mro__)
