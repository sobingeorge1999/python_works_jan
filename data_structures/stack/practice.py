# queue
queue=[]
user=int(input("enter the queue limit"))
top=0
def enqueue():
    global top,user
    if top>=user:
        print("queue is full")
    else:
        n=int(input("enter the element"))
        queue.append(n)
        print(queue)
        top+=1
def dequeue():
    global top,user
    if top<=0:
        print("queue is empty")
    else:
        s=queue[0]
        queue.remove(s)
        print(queue)
        top-=1
while True:
    u=int(input("enter the option\n1.enque\n2.dequeue\n3.stop"))
    if u==1:
        enqueue()
    elif u==2:
        dequeue()
    elif u==3:
        break
    else:
        print("invalid")
