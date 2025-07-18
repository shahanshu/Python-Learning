"""
Function Caching in Python


Function caching is a technique to store the results of expensive function calls and return the cached result when the same inputs occur again, rather than recomputing the result. This can significantly improve performance for functions that are called repeatedly with the same arguments.

*****When you have pure functions (output depends only on input)*****

where not to use 
1. when the functions calls is happening only once or rarely

2. since this takes memory so not to use it recklessly 
"""

from functools import lru_cache
import time

@lru_cache(maxsize=None) #maxsize = number of functions that are cached now
def fx(n):
 print("waiting 2 sec...")
 time .sleep(2)
 return n*n


print("simulation started")
print(fx(4))
print('done for 4 ')
print(fx(56))
print("done for 5 ")

print("simulation started")
print(fx(4))
print('done for 4 ')
print(fx(56))
print("done for 5 ")

print(f" this done cached{fx(40)}")