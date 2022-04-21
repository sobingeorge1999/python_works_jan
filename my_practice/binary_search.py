a=[3,1,452,52,43,13,563,63,652,5,25,6]
user=int(input("enter the number"))
flag=0
a.sort()
low=0
upper=len(a)-1
while low<=upper:
    mid=(low+upper)//2
    if a[mid]==user:
        flag=1
        break
    elif user<a[mid]:
        upper=mid-1
    elif user>a[mid]:
        low=mid+1
if flag==1:
    print("present")
else:
    print("not present")
