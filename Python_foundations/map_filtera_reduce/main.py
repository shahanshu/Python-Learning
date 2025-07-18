'''Map Higher Order Function'''
def cube(x):
    return x*x*x;
print(cube(3))
'''
# the traditional mehtod is :

lst=[1,2,3,4]
lst2=[]

for i in lst:
    lst2.append(cube(i))
print(lst2)
'''

lst=[1,2,3,4,5,6,7,7,8]
lst2=list(map(cube,lst)) 
#map(function name,that list you want tp apply the function )
print(lst2)
# print(type(lst2))


''' filter'''
#outpust those which are true rest not displayed 
def filter_fun(a):
    '''
    this function should be predictable (T/F)'''
    return a>4 # either true or false 
lst4=list(filter(filter_fun,lst))
print(lst4)

"""Map using the lamda function """
anshu=[2,3,4,5,6,7]
kripa=list(map(lambda x:x-1,anshu))
print(anshu)
print(kripa)

'''Reduce - it needed to be imported '''
from functools import reduce
numbers=[1,2,3,4,5]
summed=reduce(lambda x,y:x+y,numbers)
print(summed)