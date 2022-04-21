# * * * * *
#  * * * * *
#   * * * * *
#    * * * * *
#     * * * * *
#
#
# space=0
for i in range(5):
    for k in range(i):
        print(end=" ")
    # space=space+1
    for j in range(5):
        print("*",end=" ")
    print()
#    *
#   * *
#  * * *
# * * * *
# space=5
# for i in range(5):
#     for k in range(space):
#         print(end=" ")
#     space=space-1
#     for j in range(i):
#         print("*",end=" ")
#     print()

