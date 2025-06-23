a ='anshu shah'
print(len(a))

#this will make a new string but doesn't change the original strings cause the strings are immutable in nature !
print(a.upper())

# to check the validate the immutability of the stirngs 
print(a[:5].lower())
print(a)


#string method to rmovce the trailling characters for an example 

name ="sylvia!!!!!"
print(name.rstrip("!"))
#replacement of the strings

books=" maths nepali chemisty guide"
print(books.replace("nepali","rocking"))
print(books)