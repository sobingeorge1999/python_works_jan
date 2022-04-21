f1=open('data.txt','r')
f2=open('data2.txt','w')
for i in f1:
    d=i.rstrip("\n")
    f2.write(d) # f2.write(i)
    f2.write('\n')

