#3 addition by constructor

# class Add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def printvalue(self):
#         print(self.a+self.b)
#
# ob=Add(2,4)
# ob.printvalue()

#4

# class Pet:
#     def __init__(self,name,age,colour):
#         self.n=name
#         self.age=age
#         self.cl=colour
# class Cat(Pet):
#     def __init__(self,name,age,colour,owner):
#         super().__init__(name,age,colour)
#         self.owner=owner
#     def printvalue(self):
#         print('pet name ',self.n)
#         print('age is',self.age,'colour is',self.cl)
#         print('owner name is ',self.owner)
# ob=Cat('pappi',22,'black','kiran')
# ob.printvalue()

#5
#
# class Employess:
#     def __init__(self,name,id,role,salary):
#         self.n=name
#         self.id=id
#         self.role=role
#         self.sala=salary
#     def printvalue(self):
#         print(self.n,self.id,self.role,self.sala)
# ob=Employess('arun',1,'developer',45000)
# ob1=Employess('amal',2,'Tester',34000)
# ob2=Employess('Alan',3,'developer',50000)
# ob3=Employess('Anaga',4,'Tester',30000)
# ob4=Employess('Maya',5,'developer',67000)
# ob.printvalue()
# ob1.printvalue()
# ob2.printvalue()
# ob3.printvalue()
# ob4.printvalue()

#6
# import re
# user=input("enter the string")
# r='\d[\w\W]{1,10}[A-Z]'
# matcher=re.fullmatch(r,user)
# if matcher  is not None:
#     print("valid")
# else:
#     print('not valid')

#8
# print(4+3%5)  #ans7

#9
# print(min(max(False,-3,-4),2,7))

#7
# f1=open('count.txt','r')
# count={}
# for i in f1:
#    d=i.split(' ')
#    for word in d:
#        if word not in count:
#            count.update({word:1})
#        else:
#            value=count[word]
#            value+=1
#            count.update({word:value})
# print(count)

#10
  # ['G', 'F', 'G']
# temp = ['Geeks', 'for', 'Geeks']
# arr = [i[0].upper() for i in temp]
# print(arr)

#11
# user=input("enter your full name")
# d=user.split(' ')
# print(d[::-1])


#12
# def rotate1(m):
#     user1=m[-1]+m[:-1]
#     print(user1)
# user=input('enter the string')
# rotate1(user)

#14
# power of 2 or not
# user=int(input("enter the number"))
# if ==0:
#     print('yes')
# else:
#     print('no')

