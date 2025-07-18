import time
oprions="""
1. anshu shah
2. aman shah 
3. anu shah
4. zun shah
"""
print(oprions)
num = int(input('enter your options: '))
match num:
    case 1:
        print("you have seleted anshu shah")
    case 2:
        print('you have selected aman shah')
    case 3:
        print("you have selected Anu shah")
    case 4:
        print(' you have selected zun shah ')
    case _ if num < 0:
        print("error ! you have entered negative number")
    case _:

        # Additional logic inside the default case
        if num == 0:
            print("Zero is not a valid option.")
        elif num > 4:
            print("Number is too high.")
        else:
            print("Invalid input.")

 
time.sleep(2)
print(' Thanks for Voting')