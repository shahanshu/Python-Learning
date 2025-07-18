'''Generators is like a vending machine such that it doesn the following things

ON THE FLY

#This is how generators work in Python:

1.They produce values one at a time when requested

2.They remember their state between requests

3.They don't produce all values at once, saving memory
'''
"""

4.Generators use yield instead of return

5.They produce values one at a time when you call next() on them
"""

def anshu(n):
    for i in range(1,n+1,2):
     
        yield i 
       

userInput=anshu(5000)
for i in range(30):
    print(next(userInput))