# name,id,designation,salary,company
class Employee:
    def setvalue(self,name,id,designation,salary,company):
        self.name=name
        self.id=id
        self.des=designation
        self.salary=salary
        self.comp=company
    def print(self):
        print(self.name,self.id,self.des,self.salary,self.comp)
ob1=Employee()
ob1.setvalue('sai',345,'staff',68899,'ecv')
ob1.print()

