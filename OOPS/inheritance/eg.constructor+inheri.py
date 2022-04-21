class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printv(self):
        print(self.name,self.age)
class Employee(Person):
    def __init__(self,name,id,salary,age):
        super().__init__(name,age)
        self.id=id
        self.sala=salary
    def printe(self):
        print(self.name)
        print(self.name,self.age,self.id,self.sala)

s=Employee('hari',22,333,3333)
s.printe()
s.printv()