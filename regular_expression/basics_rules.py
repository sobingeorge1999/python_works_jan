# basic rules
rules=''  # rules given in quotes

x='[abc]' # either a,b,or c
x='[^abc]'# except abc
x='[a-z]'  # a to z
x='[A-Z]'  # A to Z
x='[a-zA-Z]' # both upper and lower cases are checked
x='[0-9]'   # check digits
x='[^a-zA-Z0-9]' # special symbols
x='\s' # check space
x='\d'  # check digits
x='\D'   # except digits
x='\w'  # all words except special characters
x='\W'  # for special characters