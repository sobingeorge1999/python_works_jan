import re
count=0
rule='\W'
matcher=re.finditer(rule,'abc 2@akHKjk J')
for i in matcher:
    print(i.start())
    print(i.group())
    count+=1
print(count)