# constructor
class Person:
    def __init__(self,name,age,place): #constructor method
        self.name=name         # method
        self.age=age
        self.place=place     # we cant use print in constuctor
    def printvalue(self):
        print(self.name,self.age,self.place)

ob1=Person('arun',34,'kochi')     # instance varible intialization
ob1.printvalue()