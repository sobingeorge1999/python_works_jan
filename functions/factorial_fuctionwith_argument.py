#function with argument  factorial
#
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
n=int(input("enter the number")) #user input
factorial(n)
# factorial()


# #my program
# def factorial(num):
#     if num>=0:
#         fact=1
#         for i in range(1,num+1):
#             fact=fact*i
#         print(fact)
#     else:
#         print("invalid")
# n=int(input("enter the number")) #user input
# factorial(n)
# factorial(-1)