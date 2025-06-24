# a ='anshu shah'
# print(len(a))

# #this will make a new string but doesn't change the original strings cause the strings are immutable in nature !
# print(a.upper())

# # to check the validate the immutability of the stirngs 
# print(a[:5].lower())
# print(a)


# #string method to rmovce the trailling characters for an example 

# name ="sylvia!!!!!"
# print(name.rstrip("!"))
# #replacement of the strings

# books=" maths nepali chemisty guide"
# print(books.replace("nepali","rocking"))
# print(books)

# books="kripa kripa zun jenny  "
# print(books.replace("kripa","anshu"))
# # split chnages the stirng to the list 


# print(books.split( ))

# names=' anshu aman zun anu '
# print(names.split())

# #capitalize the first letter of the strings and then rest of the strimgs to the lower case 

# heading="this is the names of the sibling that were together for some times and tHen they go seperated "
# print(heading.capitalize())

# #center the strings to the center 
# n1="welcome to page"
# print(len(n1))
# print(n1.center(50))
# print(len(n1.center(50)))

# #count the string
# name2='anshu shah anshu shah'
# print(name2.count("anshu"))

# #check whether the strings ending with the  pecific or  ot 
# print(name2.endswith("shah"))
# print(name2.endswith("to",4,2))

# # there is variabe over-ridding as well in the python 

#.find is an string mehtod to find the first occurance of the strings
# name3="anshu kumar shah is an engineerig student he's from gaighat and has been a great learner also anshu  and passionate about the inventions as well as the innovotations"
# print(name3.find("anssfdghu"))
# print(name3.find("is"))

#same way index is used for finding the strings word but if !found then exit with the error 
# print(name3.index("anshu"))
# print(name3.index("afewnshu")) #this will thow the error witt exixting the program 

# name4="anshu       \n    nshah\n"
# print(name4.isspace())

# name5=" this is the end \n"
# print(name5.isprintable()) #only returns true if it contains all printable
# n1="anshu shah"
# print(n1.isprintable())

name6=" "
print(name6.isspace())
name6="This is  the end"
print("  " in name6) # this will check the "number of spaces in the strings"
test1="Hellow Guys My name is anshu kumar shah i'm an engineering undergrad student" 
print("  " in test1)
tittle = "Hellow Guys Welcome to  My Blogs"
print(tittle.istitle())
print(tittle.swapcase())
print(tittle.title())
print(tittle.istitle())