# 0 1 1 2 3 5 8 13...
def fibonacci(n):#0,1,2,3,..
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
                # fibonacci(1)+fibonacci(0)
nterm=int(input("enter the number terms"))
for i in range(nterm):#i=0,1,2,3,..
    print(fibonacci(i))