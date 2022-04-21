class Employee:
    company='volvo'
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.sala=salary
    def print(self):
        print(self.name,self.id,self.sala,Employee.company)
ob1=Employee('binu',231414,33333)
ob1.print()
ob2=Employee('bb',231,4477474)
ob2.print()