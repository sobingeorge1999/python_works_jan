# method overriding
# same method name and same number of arguents
# child class method will override parent class
# child class will work

class A:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside parent",self.num1+self.num2)
class Add2(A):
    def sum(self,no1,no2):
        self.n=no1
        self.m=no2
        print("insdie child",self.n+self.m)
ad=Add2()
ad.sum(3,2)