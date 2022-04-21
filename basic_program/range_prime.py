initial=int(input("enter the range"))#1
final=int(input("enter the range1"))#10
for i in range(initial,final+1):#i=1,2,3,4,5,6,7,8,9,10
    if i>1:
        for j in range(2,i):#j=2,3,4
            if i%j==0:
                break
        else:
            print(i)