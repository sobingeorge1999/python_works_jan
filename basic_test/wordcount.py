count={}
f=open('data.txt','r')
for i in  f:
    s=i.upper()
    d=s.rstrip('\n').split(' ')
    for word in d:
        if word not in count:
            count.update({word:1})
        else:
            value=count[word]
            value+=1
            count.update({word:value})
print(count)

