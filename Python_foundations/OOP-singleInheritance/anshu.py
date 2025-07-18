class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return " SOund"

class dog(Animal):
    def speak(self):
      
        return "barking"
    
    def __str__(self):
        
        return f"doggy name: {self.name}"
    def test(self):
         return super().speak()
s1=dog("bittu")
print(s1.speak())
print(s1.test())
print(s1)