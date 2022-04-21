# fibonacci series
# 0,1,1,2,3  sum of last two numbers
#10 without function

#using while loop
nterms =int(input("enter the count"))
n1=0
n2=1
i=0
while i<nterms: #i<10:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    i=i+1


# using for loop
n1=0
n2=1
n=int(input("enter the numebr"))
for i in range(n): #i=0,1,2,3,4
    print(n1) #0,1,1,2,3,5
    nth=n1+n2 #1,2,
    n1=n2   #1,1
    n2=nth #1,2