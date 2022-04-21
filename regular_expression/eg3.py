#string no numbers count exactly=5
# import re
# s = input("enter the string")
# rule='\D{5}'
# matcher = re.fullmatch(rule, s)
# if matcher is not None:
#     print("valid")
# else:
#     print('invalid')


# string start and end with a number count 5
# import re
# s = input("enter the string")
# rule='\d[\w\W]{3}\d'  # count 6-3=3
# matcher = re.fullmatch(rule, s)
# if matcher is not None:
#     print("valid")
# else:
#     print('invalid')

#start with lowercase,end with uppercase ,lenth min=5,max=10

# import re
# s = input("enter the string")
# rule='[a-z][\w\W]{3,8}[A-Z]'
# matcher = re.fullmatch(rule, s)
# if matcher is not None:
#     print("valid")
# else:
#     print('invalid')

#string count=5
# first 4 elements numbers,
# last one a-z or special char
import re
s = input("enter the string")
rule='\d{4}[a-z\W]'
matcher = re.fullmatch(rule, s)
if matcher is not None:
    print("valid")
else:
    print('invalid')
