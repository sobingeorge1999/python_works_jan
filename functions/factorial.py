def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
n=int(input("enter the numebr"))
factorial(n)
