#f-string is used for the string formatting as well as for the variable plugging and populating
'''
name=input("enter your name: ")
country=input("country")
greeting=" Thanks for registrations!\n final review\n name: {} \n country:{} "
print(greeting.format(name,country)) # is cool 
print(greeting.format(country,name))# this doubt aries when we're working with large data set 

'''
#modern approach is like this python 3.6 and onwards
num=int(input('enter a fucking number'))
print(f"you have entered '{{num}}' we appreciate that ")    #use the double {{ }} for diaplying the {} as well 
name=input('enter your name:')
origin=input("enter the country")
print(f"Thanks for registration\n name:{name} \n counttry {origin} \n thanks fore registration ")
