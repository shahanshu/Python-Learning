dict = {
    123:"anshu shah",
    55:'anshu',
    46:"keipa khatiwada",
    55:"sneha "

}
print(dict[55])
print(dict) #dict are ordered in the latest versions of the python 
print(dict[55])   # this will throw an errror when there is no key  
print(dict.get(557)) # this will not thorow error when the key isn't matched 


# to get all the keys 
print(dict.keys())
# using the loops as well 
for keys in dict.keys():
    print(dict[keys])