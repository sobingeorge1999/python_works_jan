stack=[]
size=int(input("enter the size of stack"))
top=0
def push():
    global size,top
    if top>=size:
        print("stack is full")
    else:
        e=int(input("enter the element to add"))
        stack.append(e)
        print(stack)
        top=top+1
def pop():
    global top,size
    if top<=0:
        print("stack is empty")
    else:
        stack.pop()
        top=top-1
        print(stack)
while True:
    option=int(input("enter the eoption\n1.push\n2.pop"))
    if option==1:
        push()
    elif option==2:
        pop()
    else:
        print("invalid")

