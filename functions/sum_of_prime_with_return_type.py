#sum of prime number in range
#function wuth argument and return type
#1 to  10 2+3+5+7=17



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
