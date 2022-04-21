class Student:
    def __init__(self,name,roll,dep,mark):
        self.name=name
        self.roll=roll
        self.dep=dep
        self.mark=mark
    def printvalue(self):
        print()
        print('my name is',self.name)
        print(self.roll)
        print(self.dep)
        print(self.mark)

f=open('stud.txt','r')
l=[]
for i in f:
    data=i.rstrip('\n').split(',')
    name=data[0]
    roll=data[1]
    de=data[2]
    mark=data[3]
    ob=Student(name,roll,de,mark)
    ob.printvalue()
    print()
    print(ob.roll)  #we can call any variable
    l.append(int(ob.roll))  # textfile in str to int
print(l)

