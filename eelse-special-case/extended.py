# the else block gets only executed only when the for loop executes normally if it gets broken ( break statement) the else part never gets reached and thus exist the program 
'''
for i in range(1,7):
    if i ==4:
        break 
    print(i)
else:
    print("sorry there is no i ")
'''
i=0
while i <12:
    print(i)
    i+=1
    if i==5:
        print("broken")
        break
else:
    print("Loop Executed Successfully")