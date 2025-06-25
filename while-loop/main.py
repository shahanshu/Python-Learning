#while is used in the complex conditions 


# import time
# i=int(input("Guess a number"))
# while i != 34:
#     print("loading...")
#     time.sleep(2)
#     print(" wrong guess")
#     i = int( input("guess again"))
# print(" You won \nthanks for playing")



# name =input("enter you name : ")
# while name != "anshu":
#     print("incorrect name ")
#     name =input("try agian - enter name : ")
# print("thanks for joining")




#decrementing while loop 
num= int(input("enter a number"))
if num>30:
    print("Number is too high")
else:
    while num <30:
        print(num,ends=" ")
        num=num-1
        if( num <0):
            break
print("thanks for entering")