# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# # nterm=int(input("enter the limit"))
# for i in range(10):
#     print(fibonacci(i))

def facr(n):
    if n==1:
        return 1
    else:
        return  n*facr(n-1)
print(facr(5))