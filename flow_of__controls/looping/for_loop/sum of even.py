#1
#10
#2+4+6+8+10=even sum
initial=int(input("enter the value1"))
final=int(input("enter the value2"))
sum=0
for i in range(initial,final+1):
    if i%2==0:
        sum=sum+i
print("the sum of even numbers from",initial,"to",final,"=",sum)