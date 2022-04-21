class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)
class Parent:
    def __init__(self,ph,palace):
        self.ph=ph
        self.pl=palace
    def printv(self):
        print(self.ph,self.pl)
class Employee(Person,Parent):
    def __init__(self,name,id,salary,age,ph,pl):
        Person.__init__(self,name,age)
        Parent.__init__(self,ph,pl)
        self.id=id
        self.sala=salary
    def printe(self):
        print(self.name)
        print(self.name,self.age,self.id,self.sala,self.ph,self.pl)

st=Employee('hari',333,32422,22,1331344,'kott')
st.printe()
st.printv()
st.print()