
#using the split 
'''
x,y,z= input("enter three numbers seperated by space").split()
x= float(x)
y=float(y)
z=float(z)
print("sum of the three numbers are: ", int(x+y+z))

'''
'''
# this takes the numbers seperated by the space
x,y,z=map( int, input("enter the numbers:").split())
sum =x+y+z
print(sum)
'''
#this is more optimised version of the code 
numbers=list(map(int,input("enter the numbers ( seperated by spaces").split()))
print(numbers)

#trying my self
x,y=map(int,input("enter the numbers").split())
print("the sum is :",x+y);
