# 1 function without argument
def positive():
    num=int(input("enter the value"))
    if num>0:
        print("positive")
    elif num==0:
        print("zero")
    else:
        print("negative")
positive()
positive()
positive()

#2fuction with argument
def positive(num):
    if num>0:
        print("positive")
    elif num==0:
        print("zero")
    else:
        print("negative")
n=int(input("enter the input"))
positive(n)
positive(-1)
positive(2)

#3 function with argument and return type
def posneg(num):
    if n>0:
        return "postive" #bracket can be used or not
    elif n==0:
        return ("zero")
    else:
        return "negative"
print(posneg(-1))
n1=int(input("value"))
print(posneg(n1))