lst=[0,1,2,3,4,5]
rst=lst.copy()
print("copied",rst)
rst[0]=45 # the 0th position will be replaced by the new element 

print("after inserting",rst)
print('original',lst)

# lst.clear()
# print(lst)
# anshu=[45,45,45]
# lst.extend(anshu)
anshu=[56,435]
kripa=anshu +lst
print(kripa)
kripa.sort()
print(kripa)