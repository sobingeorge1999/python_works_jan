# polymorphism
# many forms

# 1.method overloading
# 2.method overriding

# same method name in differnt class has no problem
# but in same method name in one class is problem
# it happens in inheritance also

class A:
    def printa(self):
        print("inside a")
class B(A):
    def printa(self):
        print("inside  b")