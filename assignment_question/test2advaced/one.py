# class Vechile:
#     def details(self,colour,model,number):
#         self.colour=colour
#         self.model=model
#         self.num=number
#     def print(self):
#         print(self.num,self.colour,self.model)
# class Bus(Vechile):
#     def partb(self,owner):
#         self.owner=owner
#         print(self.model,self.colour,self.num,self.owner)
# ob=Bus()
# ob.details('blue','busxr','KL22FF22')
# ob.partb('babu')
# ob.print()

#2
# class Person:
#     def print(self,name,age):
#         self.name=name
#         self.age=age
#     def printdetails(self):
#         print(self.name,self.age)
# class Man:
#     def mandetails(self,child):
#         self.ch=child
# class Mans(Person,Man):
#     def printva(self):
#         print(self.name,self.age,self.ch)
# class Student(Person):
#     def printstd(self,school,place):
#         self.school=school
#         self.pl=place
#         print(self.name,self.school,self.pl,self.age)
# class Child(Student):
#     def childdetails(self,year):
#         self.y=year
#     def printc(self):
#         print(self.name,self.age,self.school)
# ob1=Mans()
# ob1.print('anu',33)
# ob1.mandetails('kiran')
# ob1.printva()
# ob=Child()
# ob.print('arun',33)
# ob.printstd('sxccce','chry')
# ob.childdetails(1997)
# ob.printc()

#3
# evenorodd=lambda n1:n1%2==0
# print(evenorodd(22))
#4
# class Animal:
#     def __init__(self,name,gender,age):
#         self.n=name
#         self.g=gender
#         self.age=age
# class Dog(Animal):
#      def __init__(self,name,gender,age,food):
#         super().__init__(name,gender,age)
#         self.food=food
#      def print(self):
#         print(self.n)
#         print(self.g,self.age,self.food)
# ob=Dog('jacky','male',4,'chicken')
# ob.print()

#5
# class Books:
#     def bookdet(self,name,author):
#         self.num1=name
#         self.num2=author
#         print('inside parent book',self.num2,self.num2)
# class Book2(Books):
#     def bookdet(self,name,author):
#         self.n=name
#         self.m=author
#         print("insdie child book",self.n,self.m)
# obj=Book2()
# obj.bookdet('python','Allen B.Downey')

#7
# import re
# x='[+][9][1]\d{10}'
# f1=open('number.txt','r')
# f2=open('newnumber.txt','w')
# for i in f1:
#     num=i.rstrip('\n')
#     matcher = re.fullmatch(x, num)
#     if matcher is not None:
#         f2.write(num)
#         f2.write('\n')

#9
# import re
# s = input("enter the string")
# rule='[A-Z]\w{3,8}[A-Z]'
# matcher = re.fullmatch(rule, s)
# if matcher is not None:
#     print("valid")
# else:
#     print('invalid')

#10
# import re
# s = input("enter the string")
# rule='[A-Z][a-z\W]'
# matcher = re.fullmatch(rule, s)
# if matcher is not None:
#     print("valid")
# else:
#     print('invalid')

#11
# import re
# s = input("enter the string")
# rule='[a]\d{5}[b]'
# matcher = re.fullmatch(rule, s)
# if matcher is not None:
#     print("valid")
# else:
#     print('invalid')

#12
# def valid(func):
#     def wrap(num):
#         import re
#         rule='[+][9][1]\d{10}'
#         matcher=re.fullmatch(rule,num)
#         if matcher is not None:
#             return func(num)
#         else:
#             raise Exception('invalid')
#     return wrap
# @valid
# def chane_number(phone):
#     new_num=phone
#     return new_num
# print(chane_number("+911294567890"))

