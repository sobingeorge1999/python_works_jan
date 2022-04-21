intial=int(input("range1"))
final=int(input("range2"))
for i in range(intial,final):
    if i%2==0:
        for a in range(5,0,-1):
            for b in range(a):
                print(i,end=" ") # end is used to continue in same line
            print()
    else:
        for a in range(1,5+1):
            for b in range(a):
                print(i,end=' ')
            print()