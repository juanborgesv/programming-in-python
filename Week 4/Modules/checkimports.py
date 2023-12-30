import sys
sys.path.insert(1, r"C:\Users\Juan\Documents\Courses\Programming in Python\Week 1\Week 4\Modules")

# Importing my defined test module 'names'.
import names
print(names.names)

'''
Different ways to import a module as a whole and 
the functions and variables from that module.
'''
# import math
# print(math.sqrt(9))

# import math as m
# print(m.sqrt(9))

# from math import sqrt
# print(sqrt(9))

# from math import sqrt as sqrtt
# print(sqrtt(9))

# from math import sqrt, log2
# print (log2(sqrt(100)))

from math import *
print(sqrt(9))

