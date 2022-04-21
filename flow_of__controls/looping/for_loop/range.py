intial = int(input("enter the value"))
final = int(input("enter the value"))
print("the even numbers between",intial,"to",final,"are")
for i in range(intial,final+1):
    if i%2==0: #for odd number if i%2!=o:
        print(i)
