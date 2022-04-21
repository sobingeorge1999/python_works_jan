# s=input("ebter the string")
# # n=""
# # p=""
# # for i in s:
# #     if i not in n:
# #         n+=i
# #     else:
# #         p=p+i
# # print(p)
# # print("last recursive",p[-1])
# # print("first recursive",p[0])


# #second recursive
s=input("enter the string")
n=""
r=""
for i in s:
    if i not in n:
        n=n+i
    else:
        if i not in r:
            r=r+i
print("second recursive",r[1])
print("last recursive element",r[-1])
print("first recursive element",r[0])

