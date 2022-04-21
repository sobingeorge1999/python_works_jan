# from packagename.modulename import functionname
#from packagename.subdirectery.modulename import functionname
# from packageexample.mod1 import add,sun      #user defined functions are calling like this
from pakageexample.module1 import *    #(for total function we use *,so it will call all the functions in the module)
print(add(3,4))

from pakageexample.module1 import add,sub  #(we add functions by comma or use '*')
print(add(3,2))
print(add(4,3))
print(sub(3,2))