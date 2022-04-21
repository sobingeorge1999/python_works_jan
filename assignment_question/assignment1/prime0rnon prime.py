a=[2,6,88,33,55,67,1,-5]
prime=[]
nonprime=[]
for i in a:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                nonprime.append(i)
                break
        else:
            prime.append(i)
    elif i==1:
        nonprime.append(i)
print(prime)
print(nonprime)