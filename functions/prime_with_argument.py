#functions with argument
def rangeprime(n,m):
    for i in range(n,m+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
# i=int(input("enter the range"))
# k=int(input("enter the range2"))
# rangeprime(i,k)
rangeprime(2,20)
