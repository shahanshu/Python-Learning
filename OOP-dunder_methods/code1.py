class Dog:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"A dog named {self.name}"
        
    def __repr__(self):
        return f"Dog('{self.name}')"

fido = Dog("Fido")
print(fido)        # Uses __str__: A dog named Fido
print(repr(fido))  # Uses __repr__: Dog('Fido')