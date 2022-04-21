# n=input("eneter the word")
# s="aeiou"
# new_string=""
# for i in n:
#     if i not in s: #direct we can give for i not in "aeiou"
#         new_string=new_string+i
# print(new_string)

n=input("eneter the string")
s=input("enter the word to be removed")
new_string=""
for i in n:
    if i not in s:
        new_string=new_string+i
print(new_string)