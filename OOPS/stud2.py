# types of variables in oop
# 1.instance variable  related to methods   self keyword is used to access
# 2.static variable    related to class       class name used to acess
class Student:
    college='abc'
    def setvalue(self,name,rollno,department):
        self.name=name
        self.roll=rollno
        self.depart=department
    def printvalue(self):
        print(self.name,self.roll,self.depart,Student.college)
        # print(self.roll)
        # print(self.depart)
        # print(self.college)
stud1=Student()
stud1.setvalue("hai",'33','ece')
stud1.printvalue()
stud2=Student()
stud2.setvalue('kiran',33,'cse')
stud2.printvalue()
