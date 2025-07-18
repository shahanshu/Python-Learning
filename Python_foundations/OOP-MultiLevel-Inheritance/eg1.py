class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def __str__(self):
        return f"animalName: {self.name} animalSpedies: {self.species}"

class Dog(Animal):
    def __init__(self, name, species,breed):
        super().__init__(name,species) #here no needed to specify the self again cause it's auto pushing the self
        self.breed=breed


    def __str__(self):
        return f"{super().__str__()}, Breed: {self.breed}"
    
a1=Animal("tiger","wild")
print(a1)
d1=Dog("animals","domestic","goldenRetriver")
print(d1)