  # * args

# def printvalue(*numbers):
#     print(numbers)
# printvalue(4,24,24,2)   # *arguments out will be tuple

# def printvalue(n1,n2):
#     print(n1,n2)
# printvalue(4,24,24,2)  # to avoid this we use * arguments

def sum_n(*argu):  #it doesnt depand on inputs
    sum=0
    for i in argu:
        sum=sum+i
    print(sum)
sum_n(2,3,1)
sum_n(2,3,1,3,4,34,0.7)