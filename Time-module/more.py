

import time

def usingFor():
    for i in range(0,5000):
        pass

def usingWhile():
    i =0
    while i<5001:
        pass

cal= time.time()
usingFor()
t1=time.time()-cal





for i in range(0,100):
    formattedTime= time.strftime("%Y-%m-%d %I:%M:%S %p",time.localtime())
    print(f" current time:{formattedTime}", end='\r')
    time.sleep(1)



for i in range(100):
    print(time.strftime("%Y-%m-%d %H:%M:%S"), end='\r')  # '\r' overwrites the line
    time.sleep(1)