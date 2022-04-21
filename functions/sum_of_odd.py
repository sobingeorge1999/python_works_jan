def odd_sum(n,m):
    sum=0
    for i in range(n,m+1):
        if i%2!=0:
            sum=sum+i
    print(sum)
odd_sum(20,30)