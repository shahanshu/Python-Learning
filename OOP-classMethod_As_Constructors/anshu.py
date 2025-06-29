'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def info(self):
        print(f"name: {self.name} salary: { self.salary}")
e1=Employee("anshu shah",12)
e1.info()
string="kripa-1200"
e2=Employee(string.split("-")[0],string.split("-")[1])
e2.info()

'''
#using the classMethod as an constructor alternative

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def info(self):
        print(f"name: { self.name} salary : {self.salary}")


# '''Alternative Constructor '''
    @classmethod
    def clean(cls,inputString):
        name,salary =inputString.split("-")
        return cls(name,salary)
        """ shorter way of returing is 
         return cls(string.split("-)[0],string.split("-")[1])
        """

         

e1=Employee.clean("kripa-5600")
e2=Employee.clean("anshu shah-2344")
e1.info()
e2.info()

