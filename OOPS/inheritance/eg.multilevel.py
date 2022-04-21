class Person:
    def setvalue(self,name,age):
        self.n=name
        self.ag=age
class Child(Person):
    def childv(self,school,place):
        self.s=school
        self.p=place
        print(self.n,self.ag)
class Student(Child):
    def stud(self,dep):
        self.d=dep
    def printlast(self):
        print(self.d,self.ag,self.p)
ob=Student()
ob.setvalue('hari',33)
ob.childv('ss','pk')
ob.stud('ece')
ob.printlast()

ob2=Child()
ob2.setvalue('ee',33)
ob2.childv('ee',33)