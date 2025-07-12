"""
 method over-ridding is a way of over-ridding a method in child what is coming from the parent class 
"""

class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x *self.y


class circle(shape):
    def __init__(self,radius):
        self.radius=radius
     

    def area(self):
        return 3.14 * self.radius


# rect=shape(3,4)
# print(f"area of rectangle with lenght 3 and 4 is {rect.area()}")

c1= circle(5)
print(c1.area())