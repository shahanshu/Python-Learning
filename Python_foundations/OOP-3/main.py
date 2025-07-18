""" Decorators """

'''
#are the functions that takes the other functions and return the function by modifying that function with the minor improvements 
def greet(fx):
    def hell():
        print("hellow this is coding- python")
        fx(pin)
        print("thanks for uisng vs code ")
    return hell

pin=int(input("enter the pincode "))
@greet
def anshu(pin):
    print(f" the pin code is : {pin}")

anshu()



'''

#using the arguments

def decor(fun):
    def anshu(*args,**kargs):
        print("Welccome to the Expo Labs")
        fun(*args,**kargs)
        print("see you soon")
    return anshu

@decor
def sum(a,b):
    print(f" { a } + { b } = { a+b } \n")
sum( b=67,a=47) # keywords arguments 
sum( 34,67)  #positional arguments

# @decor
def greeting():
    print("hellow world")
decor(greeting)() # optimised way of writtting codes 