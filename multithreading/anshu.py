"""

&&&& thread pooling execution is left&&&&
*******************************************
Thread scheduling is non-deterministic. The order in which threads run, sleep, and print depends on the OS scheduler and Python's thread switching.

Without synchronization (like join()), the output can vary between runs.


"""


import threading

import time

def sleep(sec):
    time.sleep(sec)
    print(f"sleeping for {sec} seconds")
    



# start=time.perf_counter()
# sleep(4)
# sleep(3)
# sleep(2)
# end=time.perf_counter()

# print(f"time for normal code execution is {end-start}")
t1=threading.Thread(target=sleep,args=[4])
t2=threading.Thread(target=sleep,args=[3])
t3=threading.Thread(target=sleep,args=[2])
start=time.perf_counter()
t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()


end=time.perf_counter()
print(f"time for the threading counter {end-start}")