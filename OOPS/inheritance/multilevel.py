# multilevel/hierarachical
class A:
    def seta(self):
        print('INSIDE A')
class B(A):
    def setb(self):
        print("inside b")
class C(B):
    def printc(self):
        print('inside c')
a=C()
a.printc()
a.setb()
a.seta()
b=B()
b.setb()
b.seta()