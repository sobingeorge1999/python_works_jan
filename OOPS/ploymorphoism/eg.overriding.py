class A:
    def printa(self):  # zero argument
        print("inside parent")
class B(A):  #zero argument
    def printa(self):
        print("inisde child")
ob=B()
ob.printa()

class C:
    def printdata(self):
        print("method 1")
    def printdata(self):  # overriding will work
        print('method 2')
o=C()
o.printdata()

