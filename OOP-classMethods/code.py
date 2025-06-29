class Employee:
    companyName="samsung"

        
    def info(self):
        print(f"name of employee : { self.name} works at : { self.companyName}")

    @classmethod
    def ccname(cls,companyName):
     cls.companyName=companyName


e1=Employee()
e1.name="Rdhika"
e1.info()


# e1.companyName="tesla"
e1.info()

e1.ccname(" Apple")
e1.info()

print(Employee.companyName)
e1.info()