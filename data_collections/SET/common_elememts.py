A={1,2,3,4,5}
B={1,3,5,6,7,8,9}
setcommom=set()
for i in A:  #if IN is support in for loop then it will support in if also
    if i  in B:
        setcommom.add(i)
print(setcommom)