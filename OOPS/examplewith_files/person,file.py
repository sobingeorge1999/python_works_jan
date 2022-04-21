class Person1():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print("......")
        print(self.name)
        print(self.age)
        print(self.place)
        print("....")
f=open('person.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    name=data[0]
    age=data[1]
    place=data[2]
    pe=Person1(name,age,place)
    pe.printvalue()