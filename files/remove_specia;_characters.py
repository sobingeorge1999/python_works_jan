f=open('data.txt','r')
special="""'!@#$%^&*~`:;"<>:|}{?'"""
for i in f:
    n=''
    d=i.rstrip('\n')
    for j in d:
        if j not in special:
            n=n+j
print(n)

f=open('data.txt','r')
a="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
for i in f:
    n=''
    d=i.rstrip('\n')
    for j in d:
        if j in a:
            n=n+j
    print(n)