set1={2,-4,6,8,-11,-55,-76,65,45,-100}
set2=set()
set3=set()
for i in set1:
    if i>0:
        set2.add(i)
    else:
        set3.add(i)
print(set1)
print("positiveset",set2,"\nneegative set",set3)
# print(set3)