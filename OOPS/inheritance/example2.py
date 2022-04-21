class Person:
    def printp(self,name,age,place):
        self.n=name
        self.age=age
        self.pl=place
        print(self.n,self.age,self.pl)
class Stud(Person):
    def printB(self,roll,dep,clg):
        self.r=roll
        self.d=dep
        self.c=clg
        print(self.n,self.r,self.d,self.c)
stud1=Stud()
stud1.printp('aa',33,'kakkanad')
stud1.printB(22,'ece','cc')


