#tupples are not changable in a direct way 
# #first change the tupple to list and then manipulate that 
# name=(1,2,3,45,5)
# name2=list(name)
# name2[1]=34
# name2.append(56)
# print("appended",name2)

# name2.pop()
# print("after popped ",name2)
# print("tupples original tupple",name)
# name=tuple(name2)
# print("new tupple with the manipulation ",name)
# print(type(name))

name=("anshu","aman","anu","zun")
print(name.count("anshu")) #occurance of anshu
print(name.index('anshu')) # first ocurance of 
# print(name.index('anshu',1,2)) # this will throw an error when there is no element in the tupple 