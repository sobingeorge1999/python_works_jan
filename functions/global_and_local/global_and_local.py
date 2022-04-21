#global_and_local
def printx():
    global x,a #if we give a variable inside the function it will take it as local but if we given it as global we can use ouside the function also
    x=100
    a=10
    print(x)
printx()
print(x)
print(a)
