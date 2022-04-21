# list_comprehension
# a=[1,3,2,24]
# cube=[]
# for i in a:
#     cube.append(i**3)
# print(cube)

# instead of this we can use list comprehension
# list comprehension is used only in case of empty list programs

a=[1,2,3,4,5]
cube=[i**3 for i in a]  # we can use if also inside this
print(cube)

# a=[]
# for i in range(10):
#     a.append(i)
# print(a)

a=[i for i in range(10)]
print(a)

