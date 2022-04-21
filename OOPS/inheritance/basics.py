# inheritance .... single inheritance
class A:  # parent class/base class/super class
    def printa(self,num):
        self.num=num
        print("inside A class",self.num)
class B(A):  #child class/sub class,derived class
    def printb(self,num1):
        self.num1=num1
        print("inside B class",self.num1,self.num)
# a=A()
# a.printa(4)
b=B()         #child inheritance one parent class is called single inhritance
b.printa(10)
b.printb(2)
