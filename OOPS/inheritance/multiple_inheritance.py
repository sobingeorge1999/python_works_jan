# multiple inherticane
# more than one parent class
class A:
    def printa(self):
        print("inside a")
class B:
    def printb(self):
        print("inside b")
class C(A,B):   # we add number of parent class here
    def printc(self):
        print("inside c")
c=C()
c.printb()
c.printa()
c.printc()

