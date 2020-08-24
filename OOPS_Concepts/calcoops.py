import operator
import math

class calc:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
    def add(self):
        self.z=self.x + self.y
    def mul(self):
        self.z = operator.mul(self.x,self.y)
    def sub(self):
        self.z = operator.sub(self.x,self.y)
    def div(self):
        self.z = self.x/self.y
    def pow(self):
        self.z = math.pow(self.x,self.y)

while(1):
    try:
        ob= calc()
        ob.x = int(input('Enter first no.:'))
        ob.y=int(input('enter second numner::'))
        ch=input('enter choice +, -, *, /, **')
        if(ch=='+'):
            ob.add()
            print(ob.z)
        elif(ch=='-'):
            ob.sub()
            print(ob.z)
        elif(ch=='*'):
            ob.mul()
            print(ob.z)
        elif(ch=='/'):
            ob.div()
            print(ob.z)
        elif(ch=='**'):
            ob.pow()
            print(ob.z)
        else:
            raise NotImplementedError('incorrect choice')
    except NotImplementedError as err:
        print("Error! enter correct choice",err)
    except Exception as err:
        print(err)
    finally:
        ch=input('wanna continue(y/n)')
        if (ch=='y' or ch=='Y'):
            pass
        else:
            break