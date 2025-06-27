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
a=lambda x:x*x #this is a function not a value
b=lambda y:y*y*y #this is a function not a value
sum(a(x),b(y))