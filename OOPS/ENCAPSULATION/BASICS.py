# encapsulation

# the methods and variables of a class are very well hidden and safe (eg.capsole)
# benefit
# 1 data hiding -user will not have no idea about the inner implimentation of the class
# 2 flexibility
# 3 reusability
# encapsulation is known for wrapping the code
# it  is hiding the internal working

# we can restrict access to methods and variables
# it can be achieved using private variables and private methods
# private variable can be access only within the class
# private method can be access only within the class
# private variable
class Person():
    __name='arun'
    def printvalue(self,age,place):
        self.age=age
        self.p=place
        print(Person.__name,self.age,self.p)
ob=Person()
ob.printvalue(22,'kochi')
print(ob.age)
print(Person.__name)

# # private method
class Stud():
    def __value(self):
        print("value method")
    def print(self):
        print("hello")
        self.__value()
ob=Stud()
ob.print()
# # ob.__value # we cant access bec its private
