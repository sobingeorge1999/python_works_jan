# * * * * *
#  * * * * *
#    * * * * *
#     * * * * *
#      * * * * *

space=0
for i in range(5):
    for a in range(space):
        print(end=" ")
    space=space+1
    for j in range(5):
        print("*",end=" ")
    print()