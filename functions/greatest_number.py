#1 function without argument
def greater():
    a=int(input("enter the value for a"))
    b=int(input("enter the value for b"))
    if a>b:
        print("a is greater")
    elif a==b:
        print("both are equal")
    else:
        print("b is greater ")
# a=int(input("a"))
# b=int(input("b"))
greater()

#2 function with argument
def greater(a,b):
    if a>b:
        print("a is greater")
    elif a==b:
        print("both are equal")
    else:
        print("b is greater")
greater(-1,-1)
n=int(input("a"))
n1=int(input("b"))
greater(n,n1)

#3 function with argument and return type
def greater(a,b):
    if a>b:
        return "a is greater"
    elif a==b:
        return "a and b are equall"
    else:
        return " b is bigger"
print(greater(2,3))
n=int(input("a"))
n1=int(input("b"))
print(greater(n,n1))