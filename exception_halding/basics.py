#exception_handling
n1=int(input("enter num1"))
n2=int(input("number2"))
try:
    print(n1/n2)
except Exception as r:
    print("zero division error",r)
finally:
    print("inside finally")


# try
# except
# finally
