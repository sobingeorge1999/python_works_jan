s=input("enter the string")
n=''
for i in s:
    if i not in 'aeiou':
        n=n+i
print(n)