def natural(n):
    if n==0:    #we can give n==1
        return 1 #return n both are same
    else:
        return n+natural(n-1)
print(natural(0))