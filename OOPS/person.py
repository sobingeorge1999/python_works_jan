class Person:
    def setvalue(self,name,age,place):# instance varible ,self is used to instance
        self.firstname=name  # now it become instance variable
        self.age=age         # we use it outside function also
        self.place=place     # arguments is also known as attributes
    def printvalue(self):
        print(self.firstname)
        print(self.place)
        print(self.age)
ob1=Person()
ob1.setvalue("arun",30,"delhi")
ob1.printvalue()
ob2=Person()
ob2.setvalue("sai",29,'kochi')
ob2.printvalue()


