n=input("enter the number")
a="aeiou"
count=0
for i in n:
    if i in a: #or we can use if i in "aeiou" direct we can give instead of a
        count+=1
print(count)
