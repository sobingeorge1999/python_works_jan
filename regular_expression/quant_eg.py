# import re
# count=0
# rule='a$'
# matcher=re.finditer(rule,'aaaaba abaa aa@11111234a')
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count+=1
# print(count)

#basics
# abcd@123
#1 x='[abc]' -a,b,c=3
#2 x='[^abc]' =d@123
#3 x='[a-z]'  =abcd
#4 x='[A-Z]' =0
#5 x='[a-zA-Z]'=abcd
#6 x='[0-9]'  =123
#7 x='[^a-zA-Z0-9]'=@
#8=x='\s'=0
#9 x='\d'=123
#10 x='\D'=abcd@
#11 x='\w'=abcd123
#12 x='\W'= @


# import re
# count=0
# rule='\W'
# matcher=re.finditer(rule,' abcd@123')
# for i in matcher:
#     print(i.start())
#     print(i.group())
#     count+=1
# print(count)

#quantifiers
 # aaa abcaa@123
 #1 x='a+'  only a
 #2 x='a*'
 #3 x='a?'
 #4 x='a{2}'
 #5 x='a{2,4}
 #6 x='a$'
import re
count=0
rule='a$'
matcher=re.finditer(rule,' aaa abcaa@123')
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print(count)

