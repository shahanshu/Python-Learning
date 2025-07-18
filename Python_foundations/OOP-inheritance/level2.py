""" Access Modifiers
1. all the variables and the methods are public by default 


"""

class studets:
    def __init__(self):
        self.__name="Anshu Shah"
s1=studets()
print(s1._studets__name) 
"""
can't be accessed directly but can be indirectly
"""

try:
 print(s1.name)
except Exception as f:
 print(f"errror as: { f}")  # thows error 
print(s1.__dir__())
""" availabe methods on the s1"""
