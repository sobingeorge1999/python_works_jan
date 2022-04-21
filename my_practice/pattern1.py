space=10
for i in range(6):
    for s in range(space):
        print(end=" ")
    space=space-2
    for j in range(i):
        print("*", end=" ")
    print()
