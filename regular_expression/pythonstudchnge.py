import re
x='[P][Y]\d{2}'
f1=open('regnumbers.txt','r')
f2=open('newone.txt','w')
for i in f1:
    reg=i.rstrip('\n')
    matcher =re.fullmatch(x,reg)
    if matcher is not None:
        f2.write(reg)
        f2.write('\n')
# vs code
