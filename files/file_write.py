# # file writing
# f=open("writ.txt",'w')
# f.write("hai hello how are you")
# #if we didnt create a file it will automaticaly create a file
# f=open("newone.txt",'w')
# f.write("hello hai ")
# f.write("hello are you okke\n""thats okke are you clear")
# print(f)

f=open('newone.txt','w') #in write mode the content will be repalce and add new one
f.write('hello \nhai thats okke now its clear\nhai \n')
f.write('hello ')
print(f)