#recursive repeating words

s=input("enter the string")
n=""
for i in s:
    if i not in n:
        n=n+i
    else:
        print("first recursive element ",s,"is",i)
        break

