initial = int(input("enter the intial range"))
final = int(input("enter the final  range"))
sum=0
print("sum of odd numbers from",initial,"to",final,"=",)
while initial<=final:
    if initial%2!=0:
        sum=sum+initial
    initial+=1
print(sum)
