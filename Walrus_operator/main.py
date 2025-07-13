
"""
The walrus operator (:=), introduced in Python 3.8, allows you to assign values to variables as part of an expression. 

while True:
    user_input=input("enter a quit to exit")
    if user_input =='quit' or user_input=="Quit":
     print(f"you have entred {user_input}")
     break

   
print("Have a nice Day")

"""


# while( userInput :=input("enter quit to quit")) != 'quit':
#     print(f"you have entered :{userInput}")



'''

def name():
   print(userName:=input("enter your name "),f"your name is {userName}")
name()
'''

# data =[2,3,46,76,78]
# while ( n:=len(data)) >0:
#     pass
    # print(data.pop())
    # print(data)
""" the break and the continue works on the parent condition """
# foodList=list()
# while True:
#     foods=input("foods: ")
#     if foods == 'quit':
#         break 
#     elif foods=="chicken":
#         print("non -veg foods are not allowed")
#         continue
#     foodList.append(foods)

# print(foodList)


"""Combined input and condition check using walrus operator:"""

foodList=[]
while(enteredFood:=input("enter the food you wanna have ")) !="exit":
    if enteredFood =='chicken':
        print("non-veg not allowed")
        continue
    foodList.append(enteredFood)

print(foodList)