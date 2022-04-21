Students = [('anu', 67), ('amal', 69), ('arun', 65)]


# if i[1]>
    #     print(i[0])
# list=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# lower=0
# upper=len(list)-1
# mid=(lower+upper)//2
# list.remove(list[mid])
# print(list)

#sum odd numbers 40-80

# def oddsum(intial,final):
#     sum=0
#     for i in range(intial,final+1):
#         if i%2!=0:
#             sum=sum+i
#     return sum
# print(oddsum(40,80))

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# nterm=int(input("enter the number terms"))
# for i in range(nterm):
#     print(fibonacci(i))

# reverse
# user=int(input("enter the number"))
# print(str(user)[::-1])
# user=input("enter the number")
# print(user[::-1])

# list=[i for i in range(1,100+1) if i%5==0]
# print(list)

# a=[1,2,3,4,5]
# b=[3,4,5]
# a.append(b)
# print(a)

# n=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# print(list(dict.fromkeys(n)))
# # #
# for i in range(1,6):
#     for j in range(i):
#         print("1",end=" ")
#     print()
# for i in range(5,0,-1):
#     for j in range(i):
#         print("2",end=" ")
#     print()
# for i in range(1,6):
#     for j in range(i):
#         print("3", end=" ")
#     print()
# for i in range(5,0,-1):
#     for j in range(i):
#         print("4",end=" ")
#     print()

#
# list=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# list.sort()
# new=list[1]
# print(new)

# f=open('data.txt','r')
# for j in f:
#     count = {}
#     data = j.split(" ")
#     for i in data:
#         if i not in count:
#             count.update({i: 1})
#         else:
#             value = count[i]
#             value += 1
#             count.update({i: value})
#     print(count)
