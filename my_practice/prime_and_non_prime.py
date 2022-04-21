a=[1,5,8,99,34,21,56,76,98,11,24,65,78] #5,11
prime=[]
non_prime=[]
for i in a:
    if i>1:
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==1:
            non_prime.append(i)
        else:
            prime.append(i)
print("prime nuumbers are",prime)
print("non prime numbers are",non_prime)

