queue=[]
user=int(input("enter the limit of queue"))
top=0
def enqueue():
    global top,user
    if top>=user:
        print("queue is full")
    else:
        a=int(input("enter the elements"))
        queue.append(a)
        print(queue)
        top+=1
def dequeue():
    global top,user
    if top<=0:
        print("queue is empty")
    else:
        q=queue[0]
        queue.remove(q)
        print(queue)
        top-=1
while True:
    option=int(input("enter the eoption\n1.enqueue\n2.dequeue"))
    if option==1:
        enqueue()
    elif option==2:
        dequeue()
    else:
        print("invalid")

