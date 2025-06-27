#lamda are single expression functions
def double(x):
    return x*2
print(double(45))

sum= lambda a: a*a  #transforms the way we write smaller functions
print(sum(3))

mean= lambda a,b:print(f"the sum of {a} and {b} is :",a+b)

tsum=lambda a,b,c:(a+b+c)
print(tsum(1,2,3))
mean(2,3)

def sum(sqr,cube):
    print(f"the sum of {sqr} and the cubes {cube} : ",sqr + cube)
x=2
y=1
'''
 a=lambda x:x*x #this is a function not a value
 b=lambda y:y*y*y #this is a function not a value
 sum(a(x),b(y))
'''
sum((lambda x: x*x)(45), (lambda y: y*y*y)(55))

'''

def appl(fx, value):
    return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x  # Fixed typo (lowercase 'x' and missing '=')
avg = lambda x, y, z: (x + y + z) / 3  # Fixed indentation and division

print(double(5))       # Output: 10 (5 * 2)
print(cube(5))         # Output: 125 (5³)
print(avg(3, 5, 10))   # Output: 6.0 ((3+5+10)/3)
print(appl(lambda x: x * x, 2))  # Output: 10 (6 + 2²)

'''