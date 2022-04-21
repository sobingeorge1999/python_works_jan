# def sumofpositive(intia,final):
#     sum=0
#     for i in range(intial,final+1):
#         if i>0:
#             sum=sum+i
#         print(sum)
# print(sumofpositive(-5,10))
def fact(initial,final):
    fact1=1
    for i in range(initial,final):
        fact1=fact1*i
initial=int(input("intial value"))
final=int(input("final"))
print(fact(initial,final))