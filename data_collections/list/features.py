# keep order
# heterogeneous
# support duplication
# mutable
# it support indexing and slicing
# support nesting
# elementwise updation possible


a=[999,444,2244,213,3,4,2,9,44,0000,11,0]
b=[]
while a:
    min=a[0]
    for i in a:
        if i<min:
            min=i
    b.append(min)
    a.remove(min)
print(b)


