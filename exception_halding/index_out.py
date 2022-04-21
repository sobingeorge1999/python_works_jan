# a=[1,3,6,8]
# i=int(input("enter index"))
# try:
#     print(a[i])
# except:
#     print("exception occured")

# to know the error we use Exception as
a=[1,3,6,8]
i=int(input("enter index"))
try:
    print(a[i])
except Exception as ero:
    print("exception occured",ero)

