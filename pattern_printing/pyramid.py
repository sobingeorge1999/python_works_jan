  #    *
  #   * *
  #  * * *
  # * * * *
space=5
for i in range(6):#0,1,2,3,4,5
    for a in range(space):#0,1,2,3,4
        print(end=" ")
    space=space-1
    for j in range(i):
        print("*",end=" ")
    print()
