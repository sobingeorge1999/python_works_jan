# pattern printing
# *
# * *
# * * *
# * * * *


for i in range(5): #its for the raw
    for j in range(i): #its for the *
        print("*",end=" ")  #end keyword is used for the spacing after the star*
    print()   #or we can use print("\r") \r is used for next line


# 0
# 0 1
# 0 1 2
# 0 1 2 3

# for i in range(5):
#     for j in range(i):
#       print(j,end=" ")
#     print()

# 0
# 1 1
# 2 2 2
# 3 3 3 3
#
# for i in range(5):
#     for j in range(i):
#         print(i-1,end=" ")
#     print()
#

# 0
# 1 2
# 3 4 5
# 6 7 8 9
# num=0
# for i in range(5):
#     for j in range(i):
#         print(num,end=" ")
#         num=num+1
#     print()

# * * * *
# * * *
# * *
# *
# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()