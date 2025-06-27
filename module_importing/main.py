import time
anshu = time.ctime()
import math

'''
 from math import *

 for all the importing the things which is not recommended

 
 there is also a "as" for the convienece of developing the project
 '''
'''
from math import pi as poo
root=math.sqrt(45)
print("the root of 45 is ",root)
r1=root*poo
print(f"the square root of {r1}:  ", r1)
print(anshu)

'''
#dir funcctions helps to know all the functions inside the module
import math as m
from kripa  import greet
anshu=dir(m)
print(anshu)
print(" ")
import statistics as ss
print(dir(ss))
r1=45
r2=34
mean= ss.mean([r1,r2])
print(mean)
print(type(ss))
welcome= greet()
print(welcome)