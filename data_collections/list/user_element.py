user=int(input("limit "))
odd=[]
even=[]
for i in range(user):
    s=int(input("enter the value "))
    if s%2==0:
        even.append(s)
    else:
        odd.append(s)
print("odd number",odd)
print("even numbers",even)
