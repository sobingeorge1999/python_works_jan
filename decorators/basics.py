# decorators - to add extra conditions

def changevalue(func):  #func=sub(3,5)
    def wrapper(a,b):  #a=3,b=5
        if a<b:
            a,b=b,a    #a=5,b=3
            return func(a,b)  #sub(5,3)
        else:
            return func(a,b)
    return wrapper   # dont need to put brackets
@changevalue
def sub(n1,n2):
    return n1-n2
print(sub(3,5))
print(sub(2,5))

@changevalue
def div(n1,n2):
    return n1/n2
print(div(3,4))

