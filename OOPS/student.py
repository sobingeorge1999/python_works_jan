#student name,roolno,department,college_name
class Student:
    def setvalue(self,name,rollno,department,college):
        self.name=name
        self.roll=rollno
        self.depart=department
        self.college=college
    def printvalue(self):
        print(self.name,self.roll,self.college,self.depart,)
        # print(self.roll)
        # print(self.depart)
        # print(self.college)
ob3=Student()
ob3.setvalue("hai",'33','ece','sxce')
ob3.printvalue()
