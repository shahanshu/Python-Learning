class Employee:
    def __init__(self,name):

        self.name=name;

    def show(self):
        print(f"the name is {self.name}")


class Dancer:
    def __init__(self,dance):
        self.dance=dance

    def show(self):
        print(f"the dance name is {self.dance}")

        


class DancerEmployee(Dancer, Employee):

    def __init__(self,dance,name):
        self.dance=dance
        self.name=name
    def __str__(self):
        return f" name of dancerEmployee: {self.name} dance type: {self.dance}"


d1=DancerEmployee("rock","kripa")
print(d1)
d1.show()
Employee.show(d1)   
print(DancerEmployee.mro())

"""
in heritance there isn't implicitly calling of the methods from the desired parent class nevertheless we call the method from the desired function by 

className_.funName(objectName)

"""