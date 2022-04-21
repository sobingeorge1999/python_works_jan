def vacc(func):
    def wrap(n,a):
        if a>=18:
            return func(n,a)
        else:
            raise Exception("not eligibla")
    return wrap
@vacc
def vaccination(name,age):
    return "vaccinated successfully"
print(vaccination("ani",1))
print(vaccination("ani",18))
print(vaccination("ani",1))
