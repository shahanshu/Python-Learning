class Animal:
    def msound(self):
        print("make some sounds")
class dog(Animal):
    def msound(self):
        super().msound()
        print("barks")

class cat(Animal):
    def msound(self):
        print("meow !!!")


animal=Animal()
animal.msound()
d1=dog()
d1.msound()



""" 
 we can call the parent method in the child method by using the super().method_name()
"""
