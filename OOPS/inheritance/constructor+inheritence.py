class Person:
    def __init__(self,name,age,place):
        self.n=name
        self.age=age
        self.pl=place
    def printvalue(self):
        print(self.n,self.age,self.pl)
class Student(Person):
    def __init__(self,rollno,dep,clg,name,age,place):
        super().__init__(name,age,place)
        self.r=rollno
        self.dep=dep
        self.cld=clg
    def printstudent(self):
        print(self.r,self.dep,self.cld)

st=Student(1,'cse','dd','hari',44,'haripaddu')
st.printstudent()
st.printvalue()

