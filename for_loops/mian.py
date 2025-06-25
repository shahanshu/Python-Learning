#for loops can iterate over a sequence of iterable objects

# name=['anshu','aman','zun','anna']
# for i in name :
#     print(i)
#     if(i=="anshu"):
#         print(" welcome to the programming world anshu shah\n")

# color=["Red","Green","Yellow","Purple"]
# for col in color:  
#     print(col)
#     for i in col:
#         print(i)
# # numerals
# for num in range(5):
#     print(num+1)
# for val in range( 1,9,2):
#     print(val)
# # for number in range(1,20001):
# #     print(number)

# for char in "anshu shah\n":
#     print(char)
# for even in range(2,10,2):
#     print(even)

for num in range(1,20):
    if num==10:
        break
    print(num)
print("\n")
for i in range(10):
    if i %2== 0:
        continue
    print(i ,end=" ")