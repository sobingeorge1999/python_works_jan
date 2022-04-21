#prime numbers
#4 its factors are 1,2,4 its not prime
#5 factors 1,5 its prime
#6 factors 1,2,3,6
#2 factors 1,2
#3 factors 1,3
#the number which has only two factors 1 and its number
  #CONCEPT
  #if "for" has a break and it has a else ,if break doestnt work then only else will work
  #then if break works then else doesnt work
  #if for has else then it must have break
#example
# # num=6
# # for i in range(5):
# #     print(i)
# #     if i==num:
# #         print("inside for and if",i)
# #         break
# # else:
# #     print("iniside else")
#
# # prime numbers =1,2,3,5,7,,11,13,17,19 prime always positive
# #methode 1
num=int(input("enter the number"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("its not prime")
            break
    else:
        print("prime")
else:
    print("not prime")
# #method 2
number=int(input("enter the number"))
flag=0
if number>1:   # if we want 1 as prime then put number>0,otherwise 1 is not prime then number>1
    for i in range(2,number):
        if number%i==0:
            flag=1
            break
    if flag == 1:
        print("not prime")
    else:
        print("prime")
else:
    print("invalid")


