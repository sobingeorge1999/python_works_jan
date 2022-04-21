# binary searching
# first the list should be sorted and find the middle element,then check for greater or lower
# a=[1,4.,7,9,444,24,35,3,5,3,6,3,35,3,45,5,324,4,-3]
# e=int(input("enter the element"))
# flag=0
# a.sort()
# lower=0
# upper=len(a)-1
# while lower<=upper:
#     mid=(lower+upper)//2
#     if a[mid]==e:
#         flag=1
#         break
#     elif e<a[mid]:
#         upper=mid-1
#     elif e>a[mid]:
#         lower=mid+1
# if flag==1:
#     print("present")
# else:
#     print("not")
a=[1,4,2,0.3,444,.33,34,4,2,3,4,22,44,688,35]
user=float(input("enter the number"))
flag=0
a.sort()
lower=0
upper=len(a)-1
while lower<=upper:
    mid=(lower+upper)//2
    if a[mid]==user:
        flag=1
        break
    elif user<a[mid]:
        upper=mid-1
    elif user>a[mid]:
        lower=mid+1
if flag==1:
    print("yes")
else:
    print('no')