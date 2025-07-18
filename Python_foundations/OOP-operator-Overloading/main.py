"""
Operator overloading allows you to define how Python operators (like +, -, *, etc.) work with your custom objects

"""

""""
# this is wihout the operator overloading 
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self,other):
        return Vector(self.x + other.x,self.y + other.y)

v1=Vector(2,6)
v2=Vector(2,4)
result= v1.sum(v2)
print(f"{result.x}, {result.y} ")
print(type(result))


"""

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector(self.x + other.x,self.y+other.y)

    def __str__(self):
        return f"{self.x},{self.y}" # this is used instead of the def info()

v1=Vector(4,3)
v2=Vector(2,3)
v3= v1 +v2
print(v3)