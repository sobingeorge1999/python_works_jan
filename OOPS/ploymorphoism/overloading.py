# method overloading
# same method name but differnt number of arguments
# in same parent and child class
class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class Add3(Add):
    def sum(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)
ad=Add3()
ad.sum(3,5)   #add sum
ad.sum(4,5,3)  #add3 sum
# python doesnot support method overloading
