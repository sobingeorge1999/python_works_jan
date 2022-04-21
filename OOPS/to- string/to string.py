class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.pl=place
    def printvalue(self):
        print(self.name)
        print(self.pl)
        print(self.age)  # to string method is used for object to relate string values
    def __str__(self):     #to string ,return will be used,only string type
        return self.pl       # + self. # if we want to give int(age) str(self.age)
ob=Person('anu',3,'kakkanad')
ob.printvalue()
print(ob)
ob1=Person('amal',33,'thiru')
print(ob1)
# # ex code ,concept

