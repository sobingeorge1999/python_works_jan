# regular expression
# re pattern matching
# finditer fullmatch
# import re
# count =0
# s='ababababbbbabbababaababababbaba'
# matcher=re.finditer('ab',s)
# for i in matcher:
#     print(i.group())
#     print(i.start()) # to know the index
#     count+=1
# print(count)

import re
count =0
rules='[A-Z]'
matcher=re.finditer(rules,'abc @ Abjfjsk234')
for i in matcher:
    print(i.group())
    print(i.start()) # to know the index
    count+=1
print(count)