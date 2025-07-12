class cars:
    def __init__(self,name,model):
        self.name=name
        self.model=model


    def __str__(self):
        return f"name: {self.name} model: {self.model}"

car1=cars("toyota",46748)
print(car1)