a= "anshu"
b="anshu"
print(a is b) #exact location of object in memory

print(a==b) #value
# immutable are stored in the same memory loications 
anshu={2,3,4}
ansu={2,3,4}
print(anshu is ansu)
print(anshu == ansu)


name1="anshu"
name2="anshu"
print(name1 is name2)
print(name1 == name2)


v1=True
v2=None
print(v1 is v2)
print(v1 == v2)