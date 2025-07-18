
'''
import os
if os.path.exists("kripa.txt"):
    os.remove("kripa.txt")


else:
    print("file not found")
'''

# import os

# if os.path.exists("anshu.txt"):
#     os.rename("anshu.txt","kripa")
# else:
#     print("Error!!!")

# import os

# if os.path.exists("anshueddd.py"):
#     os.remove("anshueddd.py")
#     print(f"file develted")

# import os
# stat=os.path.exists("strings")
# print(stat)
# os.rename("strings/anshu.py","strings/kripa.py")

import os

if os.path.exists("strings")==True:
    os.mkdir("strings/anshPart2.py")

else:
    os.mkdir("strings")