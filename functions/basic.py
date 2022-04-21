#functions used to improve re usability
# 3 types

# 1 function without arguments
# 2 function with arguments
# 3 function with arguments and return value
#def , function definition def is a keyword
# def function_name(): we just providind a function , a function must need () and a : also
#     code
# function_name()
#1 fuctions without arguments

def add():
    num1=int(input("enter the number1"))
    num2=int(input("enter the number2"))
    print(num1+num2)
add()
add() #how many types we want to call function

#2 function with argument

def add(num1,num2): #argument is input value
    print(num1+num2)
initial=int(input("enter value"))
final=int(input("enter the value"))
add(initial,final)
add(1,1)


#3 funnction with arguement and return value

def add(num1,num2):     #only one return can be used in a block
    return num1+num2    #in return type function it wont use print function ,only one operation is done in return
print(add(1,2))         #we have use print function when we call the function
