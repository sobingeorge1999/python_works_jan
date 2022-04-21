user=input("enter the string")
new_string=""
for i in user:
    if i not in "aeiou":
        new_string=new_string+i
print(new_string)
