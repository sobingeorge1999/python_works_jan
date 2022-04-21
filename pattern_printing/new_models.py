# * * * *
# * * *
# * *
# *

# for i in range(4,0,-1): #4,3,2,1
#     for j in range(i): #0-4,0-3,0-2,0-1 #range(5-1)
#         print("*",end=" ")
#     print()


# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
for i in range(5):#0,1,2,3,4
    for j in range(0,5):#0-4,0-4,0-4,0-4,,0-4
        print("*",end=" ")  #just try some changes i*j,i,j,and see the outputs
    print()

# 0 0 0 0 0
# 0 1 2 3 4
# 0 2 4 6 8
# 0 3 6 9 12
# 0 4 8 12 16

for i in range(5):  # 0,1,2,3,4
    for j in range(0, 5):  # 0-4,0-4,0-4,0-4,,0-4
        print(i*j, end=" ")  # just try some changes i*j,i,j,and see the outputs
    print()

