# import re
# s=input("enter the number")
# rule='\d{10}'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print("valid")
# else:
#     print('invalid')
#
# indian numbers +91
# import re
# s = input("enter the number")
# rule = '[+][9][1]\d{10}'
# matcher = re.fullmatch(rule, s)
# if matcher is not None:
#     print("valid")
# else:
#     print('invalid')


#kerala vechil numbers
# KL78SF1234
# import re
# s = input("enter the vechile number")
# rule='[K][L]\d{2}[A-Z]{2}\d{4}'
# matcher = re.fullmatch(rule, s)
# if matcher is not None:
#     print("valid")
# else:
#     print('invalid')

# starting with a and ending with b
import re
s = input("enter ")
rule='[a]b$'
matcher = re.fullmatch(rule, s)
if matcher is not None:
    print("valid")
else:
    print('invalid')

# gmail
