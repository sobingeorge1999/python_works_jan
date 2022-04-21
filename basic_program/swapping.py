#method 1
# num1=input("enter the num")
# num2=input("enter the second number")
# temp=num1
# num1=num2
# num2=temp
# print("after swap =",num1)
# print("after swap =",num2)
#method_2
# num1= input("enter the 1st =")
# num2= input("enter the 2nd")
# num1 , num2 = num2,num1
# print("after swap =",num1)
# print("after swap =",num2)
#method_3
num1 = int(input("enter the 1st ="))
num2 = int(input("enter 2nd number ="))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("after swapping =",num1)
print("after swapping =",num2)