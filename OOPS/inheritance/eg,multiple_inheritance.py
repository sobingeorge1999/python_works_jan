class Person:
    def setvalue(this,name,age):  # we can use any charactors instant of self
        this.name=name
        this.age=age
class Parent:
    def setvaluepa(self,place,phone):
        self.place=place
        self.ph=phone

class Employee(Person,Parent):
    def emp(self,id,desgnation,salary):
        self.id=id
        self.des=desgnation
        self.sala=salary
    def printem(self):
        print(self.name,self.age,self.place,self.ph,self.id,self.des,self.sala)
ob=Employee()
ob.setvalue('abu',44)
ob.setvaluepa('chry',656577339)
ob.emp('12ff','clerk',34463)
ob.printem()
