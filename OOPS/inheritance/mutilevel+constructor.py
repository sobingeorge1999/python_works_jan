class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)
class Parent(Person):
    def __init__(self,name,age,ph,place):
        super().__init__(name,age)
        self.ph=ph
        self.pl=place
    def printv(self):
        print(self.ph,self.pl)
class Employee(Parent):
    def __init__(self,name,age,ph,pl,id,salary):
        super().__init__(name,age,ph,pl)
        self.id=id
        self.sala=salary
    def printe(self):
        print('name',self.name)
        print(self.name,self.age,self.id,self.sala,self.ph,self.pl)

st=Employee('kk',13,90763222,'kakkanad',332,30000)
st.printe()
st.printv()
st.print()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Child(Person):
#     def __init__(self,name,age,school,place):
#         super().__init__(name,age)
#         self.school=school
#         self.place=place
#         print(self.name,self.age,self.school,self.place)
# class Student(Child):
#     def __init__(self,name,age,school,place,dep):
#         super().__init__(name,age,school,place)
#         self.d=dep
#     def printlast(self):
#         print('name',self.name,self.d,self.place,self.age,self.school)
#
# ob=Student('hari',34,'kj','pala','ece')
# ob.printlast()