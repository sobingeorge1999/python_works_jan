# calculator
def add(m, n):
    print(m + n)
def mult(m, n):
    print(m * n)
def div(m, n):
    print(m / n)
def sub(m, n):
    print(m-n)
while True:
    option=int(input("select option\n1.add\n2.sub\n3.div\n4.mult\n5.stop"))
    if option==5:
        break
    elif option>5:
        print("invalid")
    else:
        num1 = float(input("enter the value of m"))
        num2 = float(input("enter the value of n"))
        if option == 1:
            add(num1,num2)
        elif option==2:
            sub(num1,num2)
        elif option==3:
            div(num1,num2)
        elif option==4:
            mult(num1,num2)



