#word count dict
s=input("enter the string")
count={}
data=s.split(" ")
for i in data:
    if i not in count:
        count.update({i:1})
    else:
        value=count[i]
        value+=1
        count.update({i:value})
print(count)
