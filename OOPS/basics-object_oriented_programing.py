# oop object oriented programing
# to reuse we use objects
# class is like a design
# object is real world entity
# reference

# self is known as instance keyword

class Person: #first letter must be capital in class
    def reading(self): #method 1   #attributes
        print("reading books")
    def writing(self):  #method  2
        print("hello hai")
p=Person()  #object1
p.reading()
p.writing()

p2=Person()  # object2
p2.reading()
p2.writing()

