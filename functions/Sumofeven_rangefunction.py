#sum of even numbers in a range
#function with argument and return type


def evensum(intial,final):
    sum=0
    for i in range(intial,final+1):
        if i%2==0:
            sum=sum+i
    return sum
print(evensum(10,20))
initial=int(input("enter the intial range"))
final=int(input("enter the intial"))
print(evensum)
