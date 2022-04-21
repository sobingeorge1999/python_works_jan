# a=[8,3,2,44,5,1,44,5,6] #sorting is possible with same data type
# a.sort()
# print(a)
b=["s","s","e","f"]
b=b.sort()
print(b)
# c=[0.3,0.4,2,44,5,5,.04,333,2222,444]
c=[2,3,1]
c.sort()
print(c)
#sorting

a=[2,3,1]
new_list=[]
while a: #while loop gets true when it has a content in the "a",if the list "a" gets empty the while loop wont work
    min=a[0]
    for i in a:
        if i<min:
            min=i
    new_list.append(min)
    a.remove(min)
print(new_list)


