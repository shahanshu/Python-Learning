import time
current_time=time.ctime()
print(current_time)


hours=int(time.strftime('%H'))
if (hours<12 ):
    print("good Morning sir ")
else:
    print("Good Evening sir ")

time.sleep(2) # this will checckout thhe cleeping time in seconds for the next code to be executed 

print("thanks for checking out ")
print(" Good Bye ")