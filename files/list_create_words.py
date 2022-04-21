f1=open('data2.txt','r')
list=[]
for i in f1:
    s=i.rstrip('\n').split()#split(' ')
    list.extend(s)
print(list)