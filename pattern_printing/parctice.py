# * * * * *
#  * * * * *
#   * * * * *
#    * * * * *
#     * * * * *
space=0
for i in range(6):
    for s in range(space):
        print(end=" ")
    space+=1
    for j in range(5):
        print("*",end=" ")
    print()