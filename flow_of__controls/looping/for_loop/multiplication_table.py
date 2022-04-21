num=int(input("enter the number"))
print("the multiplication table for",num,'is')
for i in range(1,10+1):
        print(num,"*",i,"=",i*num)

# num=int(input("enter the number"))
# print("the multiplication table for",num,'is')
for j in range(1,11):
        for i in range(1,10+1):
                print(j,"*",i,"=",i*j)

        print("\n")