# strind slicing
s="hello hai how are you"
print(s[2:5])
print(s[:])
print(s[-8:-1]) #decrement must be from smaller range to higher
print(s[:])
print(s[2:9:2])
s1="helloffffff"
print(s1)
print(s[::-1]) #here it will take intial as lager and final as smaller because its decrement
print(s[2:5:-1]) #it will give empty because in decrement the rnge must be larger to smaller
print(s1[8:1:-2])
print(s1[1:5:3])
print(s[::])
p="hello"[0:4]
print(p)
h="hello hai"[::-1]
print(h)
h="hair"
print(h[3:1:-1])