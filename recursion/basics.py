#recursion
#a function call itself
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1) #5*factorial(4)
                                      #4*factorial(3) and so on
print(factorial(5))

# def factorial(n):
#     if n == 0 and 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(0))
