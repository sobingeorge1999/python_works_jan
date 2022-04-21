class Employee:
    company='HP'
    def setvalue(self,name,id,designation,salary):
        self.name=name
        self.id=id
        self.des=designation
        self.salary=salary
    def print(self):
        print(self.name,self.id,self.des,self.salary,Employee.company)
ob1=Employee()
ob1.setvalue('sai',345,'staff',68899)
ob1.print()
ob2=Employee()
ob2.setvalue('hari',344,'hr',4444)
ob2.print()