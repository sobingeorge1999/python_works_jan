def addmin(func):
    def wrap(u,p):
        if u=='admin':
            return func(u,p)
        else:
            raise Exception("only admins")
    return wrap
@addmin
def changepin(username,pin):
    mypin=pin
    return mypin
print(changepin("admin",3135))
# print(changepin("Arun",3135))